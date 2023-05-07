# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from guides.models.guide_title import GuideTitle
from guides.models.guide_content import Guidebody
from utils import switch_path_relative
import datetime, pytz, math, json, os
from PIL import Image


try:
    from django.apps import apps as models
except ImportError:  # django < 1.7
    from django.db import models


def Guide(request, *args, **kwargs):
    page = kwargs.get("page")
    page = int(page)
    page_size = 10
    essay_count = GuideTitle.objects.all().count()
    new_obj = GuideTitle.objects.all().order_by("-write_date")[((page - 1) * page_size):(page * page_size)]
    essay_data = []
    t_ids = []
    for item in new_obj:
        t_ids.append(item.id)

    def get_img_path(ids):
        body_obj = Guidebody.objects.filter(title_id__in=t_ids).exclude(image_path=None, image_name=None)
        path_dict = {}
        for id in ids:
            for item in body_obj:
                if os.path.isfile(item.image_path):
                    img_size = Image.open(item.image_path).size
                    if img_size[0] > 400 and img_size[1] > 300 and item.title_id == id:
                        path_dict[id] = switch_path_relative(item.image_path, "static")
                        break;
        return path_dict

    path_dict = get_img_path(t_ids)
    for item in new_obj:
        assay_dict = {}
        assay_dict["title"] = item.title[0:50]
        utc_date = item.write_date
        new_date = utc_date.astimezone(pytz.timezone('Asia/Shanghai'))
        assay_dict["date"] = str(new_date)[0:19]
        assay_dict["user"] = item.write_user.username if item.write_user else u"不详"
        assay_dict["abstract"] = item.abstract[0:500] if item.abstract else ""
        id = str(item.id)
        url = '/guide/view/' + id + "/"
        assay_dict["url"] = url
        #assay_dict["img_path"] = path_dict[item.id] if path_dict.has_key(item.id) else ''
        assay_dict["img_path"] = path_dict[item.id] if item.id in path_dict else ''
        essay_data.append(assay_dict)
    all_page = math.ceil(float(essay_count) / page_size)
    context = {
        'essay_data': essay_data,
        'page': page,
        'all_page': int(all_page),
    }
    if page > 1:
        context["previous_page"] = page - 1
    if page < all_page:
        context["next_page"] = page + 1
    return render(request, 'guide_index.html', context)


def view_essay(request, *args, **kwargs):
    id = kwargs.get("id")
    title = {}
    title_obj = GuideTitle.objects.filter(id=id)
    if not title_obj:
        # 重定向到404
        pass
    title["name"] = title_obj[0].title
    title["abstract"] = title_obj[0].abstract
    title["user"] = title_obj[0].write_user.username if title_obj[0].write_user else u"不详"
    utc_date = title_obj[0].write_date
    new_date = utc_date.astimezone(pytz.timezone('Asia/Shanghai'))
    title["date"] = str(new_date)[0:19]
    img_obj = title_obj[0].title_img
    if not img_obj:
        # 写一个默认标题图
        pass
    else:
        title_path = os.path.join(img_obj.new_path, img_obj.alias)
        title_path = switch_path_relative(title_path, "static")
        title["title_path"] = title_path

    body_obj = Guidebody.objects.filter(title_id=title_obj[0].id).order_by("numbers")
    bodys = []
    for item in body_obj:
        body_dict = {
            "id": item.id,
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
    return render(request, 'view_essay.html', context)
