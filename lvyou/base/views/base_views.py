# -*- coding: utf-8 -*-
from base.models.sys_material import SysMaterial
from django.contrib.auth.models import User
from django.db import models
from mycenter.models.img_material import ImgMaterial
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


class UserView(object):
    def get_user_data(self, users):
        data = {}
        user_icon_obj = SysMaterial.objects.filter(key="user_default_icon_path")
        user_home_img_obj = SysMaterial.objects.filter(key="user_home_img")

        def get_data(user, user_icon_obj):
            user_data = {"username": user.username}
            user_icon_path = ""
            if user_icon_obj:
                user_icon_obj = user_icon_obj[0]
                user_icon_path = user_icon_obj.value
            if user_home_img_obj:
                user_home_path = user_home_img_obj[0].value
            user_data["signatrue"] = u"这家伙很懒，什么都没说"
            if hasattr(user, "newuser"):
                new_user = user.newuser
                user_data["user_path"] = new_user.avatar_path if new_user.avatar_path else user_icon_path
                user_data["show_name"] = new_user.show_name if new_user.show_name else new_user.username
                user_data["telephone"] = new_user.telephone
                user_data["auth_code"] = new_user.auth_code
                user_data["send_date"] = new_user.send_date
                user_data["home_path"] = new_user.home_path if new_user.home_path else user_home_path
                user_data["abstract"] = new_user.abstract if new_user.abstract else ""
                user_data["sex"] = new_user.sex
                user_data["signatrue"] = new_user.signatrue if new_user.signatrue else ""

            else:
                user_data["show_name"] = user.first_name + user.last_name
                user_data["user_path"] = user_icon_path
                user_data["home_path"] = user_home_path
            return user_data

        if isinstance(users, models.Model):
            data = get_data(users, user_icon_obj)
        else:
            user_obj = User.objects.filter(id__in=users)
            data = {}
            for item in user_obj:
                u_data = get_data(item, user_icon_obj)
                data[item.id] = u_data
        return data
