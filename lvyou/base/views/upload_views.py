# -*- coding: utf-8 -*-
from base.models.sys_material import SysMaterial
from mycenter.models.img_material import ImgMaterial
from base.models.new_user import NewUser
from django.contrib.contenttypes.models import ContentType
from community.models.comment import Comment
from django.http import HttpResponse, Http404, StreamingHttpResponse
from django.conf import settings
import traceback, json, os, base64, uuid
from utils import switch_path_relative

try:
    from django.apps import apps
except ImportError:  # django < 1.7
    from django.db import models as apps


class Upload(object):
    def edit_upload_image(self, request):
        result = None
        try:
            page = request.POST.get("page")
            if page == "user_home":
                file_obj = request.FILES.get("home_img")
            elif page == "user_title":
                file_obj = request.FILES.get("user_title")
            else:
                file_obj = request.FILES.get("wangEditorH5File")
            if not file_obj:
                raise Exception("没有获取到文件对象！")
            path_obj = SysMaterial.objects.filter(key="image_path")
            if not path_obj:
                raise Exception("没有配置文件上传路径！")

            if not request.user.is_authenticated:
                raise Exception("登录用户才可以上传文件！")
            user = request.user
            file_name = str(uuid.uuid1()) + "_" + user.username + '.' + str(file_obj.name.split('.')[-1])

            folder = os.path.join(settings.BASE_DIR, path_obj[0].value, "media", "editor")
            if not os.path.exists(folder):
                os.makedirs(folder)
            path = os.path.join(folder, file_name)

            # 保存文件
            b64_folder = os.path.join(settings.BASE_DIR, path_obj[0].value, "media", "editor", "b64")

            if not os.path.exists(folder):
                os.makedirs(b64_folder)
            b64_path = os.path.join(b64_folder, file_name)

            fobj = open(b64_path, 'wb')
            for ck in file_obj.chunks():
                f = base64.b64encode(ck)
                fobj.write(f)
            fobj.close()  # 文件保存完毕

            new_obj = open(path, 'wb')
            with open(b64_path) as f:
                new_obj.write(base64.b64decode(f.read()))
            new_obj.close()
            f.close()
            img_obj = ImgMaterial(
                name=file_obj.name,
                alias=file_name,
                old_path=b64_path,
                new_path=path,
                file_size=file_obj.size,
                source="user_upload",
                create_user=user,
                write_user=user
            )
            img_obj = ImgMaterial.objects.bulk_create([img_obj])
            static_path = switch_path_relative(path, path_obj[0].value)
            result = static_path.encode("utf8")
            if page == "user_home":
                user_obj = NewUser.objects.get(id=request.user.id)
                user_obj.home_path = result
                user_obj.save()
            elif page == "user_title":
                user_obj = NewUser.objects.get(id=request.user.id)
                user_obj.avatar_path = result
                user_obj.save()

        except Exception as e:
            err_msg = e.message
            if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
               err_msg = e.faultCode
            result = "error|" + err_msg
        finally:
            return HttpResponse(result)

    def create_comment(self, request):
        result = {}
        try:
            parent_type = request.POST.get("parent_type")
            parent_id = request.POST.get("parent_id")
            content = request.POST.get("content")
            try:
                parent_id = int(parent_id)
            except:
                raise Exception("数据类型不正确")
            # parent_type_obj = SysMaterial.objects.filter(key=parent_type)
            # if not parent_type_obj:
            #     raise Exception("parent_type不正确！")
            # c_type = json.loads(parent_type_obj[0].value)
            # app_label = c_type["app_label"]
            # app_model = c_type["model"]
            #
            # model = ContentType.objects.get(app_label=app_label, model=app_model)
            # new_obj = model.model_class().objects.filter(id=parent_id)
            comment_obj = Comment(
                content=content,
                parent_id=parent_id,
                parent_type=parent_type,
                target_user=request.user,
                is_active=True,
                create_user=request.user,
                write_user=request.user,
            )
            comment_obj.save()
            result["successful"] = True
        except Exception as e:
            err_msg = e.message
            if not err_msg and hasattr(e, 'faultCode') and e.faultCode:
                err_msg = e.faultCode
            result = "error|" + err_msg
        finally:
            return HttpResponse(json.dumps(result))
