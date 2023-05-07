# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import mycenter_vilews

urlpatterns = [
    url(r'^$', mycenter_vilews.Center),
    url(r'^note/create/$', mycenter_vilews.CreateNote),
    url(r'^note/create/upload_title_img/$', mycenter_vilews.title_img),
    url(r'^note/create/show_title_img/$', mycenter_vilews.show_title_img),
    url(r'^note/create/create_title/$', mycenter_vilews.create_title),
    url(r'^note/create/upload_img/$', mycenter_vilews.upload_img),
    url(r'^note/create/edit_text/$', mycenter_vilews.edit_text),
    url(r'^note/create/edit_text_get/$', mycenter_vilews.edit_text_get),
    url(r'^note/create/section/title/$', mycenter_vilews.section_title),
    url(r'^note/create/save_note/$', mycenter_vilews.save_note),
    url(r'^note/create/save_note/public/(?P<title_uuid>\w+)/$', mycenter_vilews.set_public),
    url(r'^note/create/view/(?P<title_uuid>\w+)/$', mycenter_vilews.get_save_view),

]

urls = urlpatterns
