# -*- coding: utf-8 -*-
import os
from django.conf import settings
#from models.sys_material import SysMaterial
from utils import sql_get_pgsql
import json


class Material(object):
    def __init__(self, model):
        super(Material, self).__init__()
        self.model = model
        self.node_dict = {}
        topic_text_obj = sql_get_pgsql("SELECT app_label,model FROM django_content_type WHERE model='topictext'")
        TopicText = {"app_label": topic_text_obj[0][0], "model": topic_text_obj[0][1]}
        guide_title_obj = sql_get_pgsql("SELECT app_label,model FROM django_content_type WHERE model='guidetitle'")
        GuideTitle = {"app_label": guide_title_obj[0][0], "model": guide_title_obj[0][1]}
        GuideTitle = json.dumps(GuideTitle)
        TopicText = json.dumps(TopicText)
        self.data = [
            {'key': 'user_default_icon_path',
             'value': '/static/media/icon/sysicon/yangwangtiankong.jpg',
             'note': u'默认的用户头像'
             },
            {'key': 'user_images_default',
             'value': '/static/media/icon/sysicon/user_images_ default_160x160.jpg',
             'note': u'评论页的默认用户头像'
             },
            {'key': 'user_home_img',
             'value': '/static/media/images/sysimg/default_user_home_images.jpg',
             'note': u'用户主页默认头像'
             },
            {"key": "comm_page_size", "value": "10", "note": u"社区首页展示的帖子的条数"},
            {"key": "sort_page_size", "value": "10", "note": u"分类展示帖子的页数"},
            {"key": "image_path", "value": "static", "note": u"文件默认上传的路径"},
            {"key": "TopicText", "value": TopicText, "note": u"TopicText的app_label和model"},
            {"key": "GuideTitle", "value": GuideTitle, "note": u"GuideTitle的app_label和model"},
        ]

    def write_data(self):
        data = {}
        for item in self.data:
            key = item.get('key')
            data['value'] = item.get('value')
            data['note'] = item.get('note')
            new_obj = self.model.objects.get_or_create(key=key, defaults=data)[0]
            new_obj.save()


def make_data():
    from .models.sys_material import SysMaterial
    Material(SysMaterial).write_data()
