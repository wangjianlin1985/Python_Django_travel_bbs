/**
 * Created by frowlwood on 2016/11/25.
 */
var fileUpload = Vue.extend({
    template: '<div><span class="fileinput-button">' +
    '<i class="glyphicon glyphicon-folder-open"></i>' +
    '<span>上传文件</span>' +
    '<input id="fileupload" type="file" name="fileupload" multiple>' +
    '</span></div>' +
    '<div id="fileupload_file_name"></div>',
    props: ['options', "csrftoken"],
    ready: function () {
        $(this.$el).attr('id', this.id);
        this._make_options(this.options);
    },
    methods: {
        _make_options: function (options) {
            this.url_prefix = '';
            if (this.options && this.options.url_prefix)
                this.url_prefix = this.options.url_prefix;  //url
            this.singleFile = this.options.singleFile ? this.options.singleFile : false;    //一次上传多个文件
            this.autoUpload = this.options.autoUpload ? this.options.autoUpload : false;     //是否立即上传
            this.file_size = this.options.file_size ? this.options.file_size : false;       //文件大小限制
            this.file_count_size = this.options.file_count_size ? this.options.file_count_size : false;     //同时上传数量限制
            this.show_file_name = this.options.show_file_name ? this.options.show_file_name : false;      //是否显示需要上传的文件名字
            this.start_upload_button = this.options.start_upload_button ? this.options.start_upload_button : "default_uoload_button";   //上传文件按钮id
            this._init_file(function (initFile) {
            });
        },
        _init_file: function (init_File) {
            var self = this;
            var uploader = $('#fileupload');
            uploader.fileupload(
                {
                    url: self.url_prefix,
                    singleFileUploads: self.singleFile, //一次上传多个文件
                    autoUpload: self.autoUpload,
                    start: function (e) {
                        // 开始上传后不能再选文件了

                    },
                    processdone: function (e, data) {
                        // if (self.datafile == undefined) {
                        //     self.datafile = data;
                        // }
                    },
                    always: function (e, data) {
                        // $("#fileupload").removeAttr("disabled");
                        //上传完成之后移除file的disabled属性
                        //    回调结束（成功，中止或错误）上传请求。这个回调相当于所提供的完整的回调

                    },
                    progressall: function (e, data) {
                        //进度条。
                        //     var progress = parseInt(data.loaded / data.total * 100, 10);
                        //     $('#progresss').css(
                        //         'width',
                        //         progress + '%'
                        //     );
                        //     $('#progresss').html(progress + '%')
                    },
                    add: function (e, data) {
                        if (self.file_upload_add == false) {
                            data.files = self.files;
                            if (self.autoUpload == true && self.file_validation == true) {
                                data.submit().success(function (result, textStatus, jqXHR) {
                                    console.log(result)
                                })
                            } else if (self.autoUpload == false && self.file_validation == true) {
                                $('#' + self.start_upload_button).click(function (e) {
                                    data.submit().success(function (result, textStatus, jqXHR) {
                                        console.log(result)
                                    })
                                })
                            }
                            self.file_upload_add = true
                        }

                    },
                    always: function (e, data) {
                        console.log(data);
                        console.log(e)
                    }
                })
                .bind('fileuploadchange', function (e, data) {
                    if (self.singleFile == true) {
                        self.files = self.files == undefined ? data.files : []
                        self._merge_files(data)
                    } else {
                        self.files = data.files;
                    }
                    if (self.show_file_name == true) {
                        self._show_file_name(self.files)
                    }
                    self._file_verification();
                    self.file_upload_add = false;
                })
        },
        _file_verification: function () {
            var self = this;
            var err_msg = {};
            err_msg.file_size = self.file_size;
            err_msg.file_count_size = self.file_count_size;
            if (self.file_size != false) {
                err_msg.err_file_fize = [];
                for (var i = 0; i < self.files.length; i++) {
                    if (self.files[i].size > parseInt(self.file_size) * 1024 * 1024) {
                        err_msg.err_file_fize.push(self.files[i].name)
                    }
                }
            }
            if (self.file_count_size != false) {
                if (self.files.length > self.file_count_size)
                    err_msg.err_file_count_size = true;
            }
            if (err_msg.err_file_fize.length == 0 && self.err_file_count_size != true) {
                err_msg.success = true;
                self.file_validation = true;
            } else {
                console.log(err_msg);
                err_msg.success = false;
            }
            self.$emit('upload_validation', err_msg)
        },
        _merge_files: function (data) {
            //合并多次选中的文件
            this.files = this.files.concat(data.files);
            data.files = this.files;
            var file_arr = [];
            var temp = {};
            for (var i = 0; i < data.files.length; i++) {
                if (!temp[data.files[i].name]) {
                    temp[data.files[i].name] = 1;
                    file_arr.push(data.files[i])
                }
            }
            this.files = file_arr;
        },
        _show_file_name: function (files) {
            //此函数把被选中的文件名字显示到指定区域
            var self = this;
            var datetime = new Date().getTime();
            if (files.length > 0) {
                $('#fileupload_file_name').html('');
                for (var i = 0; i < files.length; i++) {
                    var show_file_name = '<div  name="div' + String(files[i].name) + '"><p class="col-lg-9"> ' + files[i].name + '</p><p class="col-lg-3"><span name="del_' + datetime + '" title="' + files[i].name + '" style="cursor: pointer"><i class="glyphicon glyphicon-remove"></i></span></p></div>'
                    $('#fileupload_file_name').prepend(show_file_name);
                }
                $('[name="del_' + datetime + '"]').click(function (e) {
                    for (var i = files.length - 1; i >= 0; i--) {
                        if (self.files[i].name == this.title)
                            self.files.splice(i, 1)
                    }
                    $('[name="div' + this.title + '"]').remove();
                    self._file_verification()
                })
            }
        },

    }
});
Vue.component('fileUpload', fileUpload);