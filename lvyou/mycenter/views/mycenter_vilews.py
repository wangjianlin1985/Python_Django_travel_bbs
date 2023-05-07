# -*- coding: utf-8 -*-
from django.shortcuts import render
from mycenter.models.img_material import ImgMaterial
from elasticsearch import Elasticsearch
from guides.models.guide_title import GuideTitle
from guides.models.guide_content import Guidebody
from django.http import HttpResponse, Http404
from django.conf import settings
from django.contrib.auth.decorators import login_required  # 登陆装饰器
import json, uuid, shortuuid, os, base64, travel.settings, traceback
from django.views.decorators.csrf import csrf_exempt
from utils import switch_path_relative
from utils import write_es, sql_get_es


def Center(request):
    return render(request, 'center.html')


# 登陆验证
@login_required
@csrf_exempt
def CreateNote(request):
    uuid = shortuuid.uuid()
    edit_uuid = shortuuid.uuid()
    context = {
        'uuid': uuid,
        "edit_uuid": edit_uuid,
        'action': 'create',
    }
    return render(request, 'create_note.html', context)


def title_img(request):
    models = ImgMaterial
    method = request.method.lower()

    if method == 'post':
        result = {}
        try:

            f = request.FILES.get('files[]')

            uuid_name = shortuuid.uuid()
            image_name = uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid_name))
            file_dir = os.path.join(settings.MEDIA_ROOT, 'OldImgFile')
            if os.path.exists(file_dir) == False:  # 如果文件夹不存在就创建它
                os.makedirs(file_dir)

            img_alias = str(image_name) + str('.') + str(f.name.split('.')[-1])

            file_path = os.path.join(file_dir, img_alias)
            fobj = open(file_path, 'wb')
            for chrunk in f.chunks():
                filecontent = base64.b64encode(chrunk)
                fobj.write(filecontent)
            fobj.close()  # 文件保存完毕

            # 把文件信息写到数据库
            img_d_obj = {
                'name': f.name, 'file_size': f.size, 'old_path': file_dir, 'alias': img_alias
            }
            new_obj = models.objects.get_or_create(alias=img_alias, defaults=img_d_obj)[0]
            new_obj.save()  # 把上传的图片信息保存到数据库中

            title_uuid = request.POST.get('uuid')
            title = request.POST.get('guide_title')
            title_obj = GuideTitle.objects.filter(uuid=title_uuid)
            if len(title_obj) == 0:
                title_obj = GuideTitle(uuid=title_uuid, source='user create', title_img_id=new_obj.id)
                if title != '':
                    title_obj.title = title
                title_obj.create_user = request.user if request.user else ""
                title_obj.write_user = request.user if request.user else ""
                title_obj.save()
            else:
                title_obj[0].title_img_id = new_obj.id
                if title != '':
                    title_obj.title = title
                title_obj[0].save()
            result['alias'] = new_obj.alias
            result['old_path'] = file_dir
        except Exception as e:
            _trackback = traceback.format_exc()
            err_msg = e.message
            if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
                err_msg = e.faultCode
            result['error_msg'] = err_msg
            result['trackback'] = _trackback
        finally:
            return HttpResponse(json.dumps(result))

    if method == 'get':
        return HttpResponse(json.dumps('对不起没有get请求的的后台'))


# @csrf_exempt
def show_title_img(request):
    models = ImgMaterial
    method = request.method.lower()
    if method == 'post':
        result = {}
        try:
            image_alias = request.POST.get('alias')
            image_old_path = os.path.join(request.POST.get('old_path'), image_alias)
            relative_path = os.path.join('static', 'media', 'images', image_alias)
            image_new_path = os.path.join(settings.BASE_DIR, relative_path)
            with open(image_old_path) as f:
                temporary_file = open(image_new_path, 'wb')
                temporary_file.write(base64.b64decode(f.read()))
                temporary_file.close()

            new_obj = models.objects.filter(alias=image_alias)[0]
            new_obj.new_path = os.path.join(settings.BASE_DIR, 'static', 'media', 'images')
            new_obj.save()
            result['path'] = relative_path
        except Exception as e:
            _trackback = traceback.format_exc()
            err_msg = e.message
            if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
                err_msg = e.faultCode
            result['error_msg'] = err_msg
            result['trackback'] = _trackback
        finally:
            return HttpResponse(json.dumps(result))

    elif method == 'get':
        pass


def create_title(request):
    method = request.method.lower()
    if method == 'post':
        result = {}
        try:
            title_uuid = request.POST.get('uuid')
            title = request.POST.get('title')
            title_obj = GuideTitle.objects.filter(uuid=title_uuid)
            if title != '':
                if len(title_obj) == 0:
                    title_obj = GuideTitle(uuid=title_uuid, source='user create', title=title)
                    title_obj.create_user = request.user if request.user else ""
                    title_obj.write_user = request.user if request.user else ""
                    title_obj.save()
                else:
                    title_obj[0].title = title
                    title_obj.create_user = request.user if request.user else ""
                    title_obj.write_user = request.user if request.user else ""
                    title_obj[0].save()
                result['success'] = title
            else:
                result['success'] = u'标题未做改变'

        except Exception as e:
            _trackback = traceback.format_exc()
            err_msg = e.message
            if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
                err_msg = e.faultCode
            result['error_msg'] = err_msg
            result['trackback'] = _trackback
        finally:
            return HttpResponse(json.dumps(result))

    elif method == 'get':
        pass


def upload_file(f):
    res_and_obj = {}
    result = {}
    uuid_name = shortuuid.uuid()
    image_name = uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid_name))
    file_dir = os.path.join(settings.MEDIA_ROOT, 'OldImgFile')
    if os.path.exists(file_dir) == False:  # 如果文件夹不存在就创建它
        os.makedirs(file_dir)

    img_alias = str(image_name) + str('.') + str(f.name.split('.')[-1])

    file_path = os.path.join(file_dir, img_alias)
    fobj = open(file_path, 'wb')
    for chrunk in f.chunks():
        filecontent = base64.b64encode(chrunk)
        fobj.write(filecontent)
    fobj.close()  # 文件保存完毕

    # 把文件信息写到数据库
    img_d_obj = {
        'name': f.name, 'file_size': f.size, 'old_path': file_dir, 'alias': img_alias
    }
    new_obj = ImgMaterial.objects.get_or_create(alias=img_alias, defaults=img_d_obj)[0]
    # 解码到static文件下
    relative_path = os.path.join('static', 'media', 'images', img_alias)
    image_new_path = os.path.join(settings.BASE_DIR, relative_path)
    with open(file_path) as f:
        temporary_file = open(image_new_path, 'wb')
        temporary_file.write(base64.b64decode(f.read()))
        temporary_file.close()
    new_obj.new_path = os.path.join(settings.BASE_DIR, 'static', 'media', 'images')
    new_obj.save()
    result['path'] = relative_path
    res_and_obj['result'] = result
    res_and_obj['file_obj'] = new_obj
    return res_and_obj


@csrf_exempt
def upload_img(request):
    result = {}
    method = request.method.lower()
    if method == 'post':
        try:
            f = request.FILES.get('files')
            res_and_obj = upload_file(f)
            img_obj = res_and_obj['file_obj']

            uuids = request.GET.get("uuid").split("_")
            title_uuid = uuids[0]
            img_uuid = uuids[1]
            title_obj = GuideTitle.objects.get_or_create(uuid=title_uuid)[0]
            title_obj.source = 'user create'
            title_obj.create_user = request.user if request.user else ""
            title_obj.write_user = request.user if request.user else ""
            title_obj.save()
            result["old_uuid"] = img_uuid
            if img_uuid:
                Guidebody.objects.filter(uuid=img_uuid, title_id=title_obj.id)
                if Guidebody:
                    img_uuid = shortuuid.uuid()
                    img_path = os.path.join(img_obj.new_path, img_obj.alias)
                    body_text = Guidebody(uuid=img_uuid, title_id=title_obj.id, image_path=img_path,
                                          image_name=img_obj.name)
                    body_text.image_location = 'all'
                    body_text.save()
                else:
                    body_text = Guidebody(uuid=img_uuid, title_id=title_obj.id, image_path=img_obj.new_path,
                                          image_name=img_obj.name)
                    body_text.image_location = 'all'
                    body_text.save()
                result["path"] = "/" + "/".join(res_and_obj['result']["path"].split("\\"))
                result["img_uuid"] = body_text.uuid

        except Exception as e:
            _trackback = traceback.format_exc()
            err_msg = e.message
            if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
                err_msg = e.faultCode
            result['error_msg'] = err_msg
            result['trackback'] = _trackback
        finally:
            return HttpResponse(json.dumps(result))

    if method == 'get':
        img_uuid = request.GET.get("img_uuid")
        path = request.GET.get("path")
        old_uuid = request.GET.get("old_uuid")
        edit_uuid = shortuuid.uuid()
        context = {
            'action': 'create',
            'edit_uuid': edit_uuid,
            'img_uuid': img_uuid,
            'path': path,
            "old_uuid": old_uuid
        }

        return render(request, 'edit_form_img.html', context)


def edit_text_post(request):
    result = {}
    try:
        title_uuid = request.POST.get("title_uuid")
        text_val = request.POST.get("text")
        body_uuid = request.POST.get("body_uuid")

        title_obj = GuideTitle.objects.get_or_create(uuid=title_uuid)[0]
        title_obj.source = 'user create'
        title_obj.create_user = request.user if request.user else ""
        title_obj.write_user = request.user if request.user else ""
        title_obj.save()
        result["old_uuid"] = body_uuid
        if body_uuid:
            body_obj = Guidebody.objects.filter(uuid=body_uuid, title_id=title_obj.id)
            if body_obj:
                uuid = shortuuid.uuid()
                body_obj = Guidebody(uuid=uuid, s_body=text_val, title_id=title_obj.id)
                body_obj.save()

                result["body_uuid"] = uuid
                result["text"] = body_obj.s_body
            else:
                body_obj = Guidebody(uuid=body_uuid, s_body=text_val, title_id=title_obj.id)
                body_obj.save()
                result["body_uuid"] = body_obj.uuid
                result["text"] = body_obj.s_body
    except Exception as e:
        _trackback = traceback.format_exc()
        err_msg = e.message
        if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
            err_msg = e.faultCode
        result['error_msg'] = err_msg
        result['trackback'] = _trackback
    finally:
        return HttpResponse(json.dumps(result))


@csrf_exempt
def edit_text_get(request):
    text_str = request.POST.get("text")
    body_uuid = request.POST.get("body_uuid")
    old_uuid = request.POST.get("old_uuid")
    context = {
        'action': 'create',
        'text_str': text_str,
        'body_uuid': body_uuid,
        'edit_uuid': shortuuid.uuid(),
    }

    return render(request, 'edit_form_text.html', context)


def edit_text(request, *args, **kwargs):
    method = request.method.lower()
    if method == 'post':
        return edit_text_post(request)


def section_title(request, *args, **kwargs):
    '''
    添加文章标题页
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    method = request.method.lower()
    if method == 'post':
        return _section_title_post(request)
    elif method == 'get':
        return _section_title_get(request)


def _section_title_post(request):
    result = {}
    try:
        body_uuid = request.POST.get("body_uuid")
        section_title = request.POST.get("section_title")
        title_uuid = request.POST.get("title_uuid")
        title_obj = GuideTitle.objects.get_or_create(uuid=title_uuid)[0]
        title_obj.source = 'user create'
        title_obj.create_user = request.user if request.user else ""
        title_obj.write_user = request.user if request.user else ""
        title_obj.save()
        result["old_uuid"] = body_uuid
        if body_uuid:
            body_obj = Guidebody.objects.filter(uuid=body_uuid, title_id=title_obj.id)
            if body_obj:
                uuid = shortuuid.uuid()
                body_obj = Guidebody(uuid=uuid, s_title=section_title, title_id=title_obj.id)
                body_obj.save()
                result['section_uuid'] = uuid
                result['section_title'] = body_obj.s_title
            else:
                body_obj = Guidebody(uuid=body_uuid, s_title=section_title, title_id=title_obj.id)
                body_obj.save()
                result['section_uuid'] = body_obj.uuid
                result['section_title'] = body_obj.s_title
    except Exception as e:
        _trackback = traceback.format_exc()
        err_msg = e.message
        if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
            err_msg = e.faultCode
        result['error_msg'] = err_msg
        result['trackback'] = _trackback
    finally:
        return HttpResponse(json.dumps(result))


def _section_title_get(request):
    section_uuid = request.GET.get("section_uuid")
    section_title = request.GET.get("section_title")
    context = {
        'action': 'create',
        'section_title': section_title,
        'section_uuid': section_uuid,
        'edit_uuid': shortuuid.uuid(),
    }
    return render(request, 'edit_form_s_title.html', context)


@csrf_exempt
def save_note(request):
    '''
    保存草稿的函数
    :param request:
    :return:
    '''
    result = {}
    try:
        uuids = request.POST.get("uuids")
        title_uuid = request.POST.get("title_uuid")
        if uuids:
            uuids = json.loads(uuids)
        number = {}
        for idx, item in enumerate(uuids):
            number[item] = idx
        title_obj = GuideTitle.objects.filter(uuid=title_uuid)
        if not title_obj:
            raise Exception(u"要保存的草稿不存在")
        new_obj = Guidebody.objects.filter(title_id=title_obj[0].id, uuid__in=uuids)
        body_all = []
        for item in new_obj:
            if item.s_body:
                body_all.append(item.s_body)
            item.numbers = number[item.uuid]
            item.save()
        str_body = ''.join(body_all)
        if len(str_body) > 200:
            abstract = str_body[200:]
        else:
            abstract = str_body
        title_obj[0].abstract = abstract
        title_obj.create_user = request.user if request.user else ""
        title_obj.write_user = request.user if request.user else ""
        title_obj[0].save()
        result["title_uuid"] = title_uuid
    except Exception as e:
        _trackback = traceback.format_exc()
        err_msg = e.message
        if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
            err_msg = e.faultCode
        result['error_msg'] = err_msg
        result['trackback'] = _trackback
    finally:
        return HttpResponse(json.dumps(result))


def set_public(request, *args, **kwargs):
    '''
    发表文章
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    result = {}
    try:
        title_uuid = kwargs.get("title_uuid")
        title_obj = GuideTitle.objects.filter(uuid=title_uuid)
        if not title_obj:
            raise Exception(u"您要发表的文章不存在")
        title_obj[0].u_public = True
        title_obj.write_user = request.user if request.user else ""
        title_obj[0].save()
        # TODO:把文章内容加到es中可以在此处设置
        body_objs = Guidebody.objects.filter(title_id=title_obj[0].id).order_by("numbers")
        t_img_obj = title_obj[0].title_img
        if t_img_obj:
            t_img_name = t_img_obj.name
            t_img_path = os.path.join(t_img_obj.new_path, t_img_obj.alias)
            t_img_describe = t_img_obj.describe
        data = {}
        data["title"] = title_obj[0].title
        data["t_uuid"] = title_obj[0].uuid
        data["t_id"] = title_obj[0].id
        data["abstract"] = title_obj[0].abstract
        data["priority"] = title_obj[0].priority
        data["t_img_id"] = title_obj[0].title_img_id
        data["t_img_name"] = t_img_name
        data["t_img_path"] = t_img_path
        data["t_img_describe"] = t_img_describe
        data["title"] = {}
        data["title"]["title_path"] = t_img_path
        data["title"]["name"] = t_img_name
        data["title"]["title_uuid"] = title_obj[0].uuid
        data["title"]["abstract"] = title_obj[0].abstract
        search_text = []
        body_text = []
        for item in body_objs:
            body_dict = {
                "body_uuid": item.uuid,
            }
            if item.s_title:
                body_dict["action"] = "s_title"
                body_dict["text"] = item.s_title
                if item.s_title:
                    search_text.append(item.s_title)
            elif item.image_path:
                body_dict["action"] = "b_img"
                body_dict["path"] = switch_path_relative(item.image_path, "static")
                body_dict["image_msg"] = item.image_msg
                body_dict["image_name"] = item.image_name
            elif item.s_body:
                body_dict["action"] = "s_body"
                body_dict["text"] = item.s_body
                if item.s_body:
                    search_text.append(item.s_body)
            body_text.append(body_dict)
        data["bodys"] = body_text
        data["search_text"] = "\n".join(search_text)
        # 写数据到es
        sql_get_es("se")
        res = write_es(data, 'travel', 'note')
        if res["errors"] == False:
            result["issucces"] = True

    except Exception as e:
        _trackback = traceback.format_exc()
        err_msg = e.message
        if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
            err_msg = e.faultCode
        result['error_msg'] = err_msg
        result['trackback'] = _trackback
    finally:
        return HttpResponse(json.dumps(result))


def get_save_view(request, *args, **kwargs):
    title_uuid = kwargs.get("title_uuid")
    title = {}
    title_obj = GuideTitle.objects.filter(uuid=title_uuid)
    if title_obj:
        title["name"] = title_obj[0].title
        title["abstract"] = title_obj[0].abstract
        title["title_uuid"] = title_uuid
        img_obj = title_obj[0].title_img
        if img_obj:
            title_path = os.path.join(img_obj.new_path, img_obj.alias)
            title_path = switch_path_relative(title_path, "static")
            title["title_path"] = title_path
        body_obj = Guidebody.objects.filter(title_id=title_obj[0].id).order_by("numbers")
        bodys = []
        for item in body_obj:
            body_dict = {
                "body_uuid": item.uuid,
            }
            if item.s_title:
                body_dict["action"] = "s_title"
                body_dict["text"] = item.s_title
            elif item.image_path:
                body_dict["action"] = "b_img"
                body_dict["path"] = switch_path_relative(item.image_path, "static")
                body_dict["image_msg"] = item.image_msg
                body_dict["image_name"] = item.image_name
            elif item.s_body:
                body_dict["action"] = "s_body"
                body_dict["text"] = item.s_body
            bodys.append(body_dict)
    context = {
        'title': title,
        "bodys": bodys,
    }
    return render(request, 'view_note.html', context)
