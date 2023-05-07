# -*- coding: utf-8 -*-
from django.conf.urls import url
# import views
# import views.guide as guide_view
from .views import community_view as communitys

# guide =views.guide
community_view = communitys.Community()
urlpatterns = [
    url(r'^(?P<sort>\w+)/(?P<page>\w+)/$', community_view.get_community),
    url(r'^get_qlist/$', community_view.get_question_list),
    url(r'^view/(?P<category>\w+)/(?P<action>\w+)/$', community_view.get_probem_list),
    url(r'^create/$', community_view.create),
    url(r'^comm/view/(?P<sort>\w+)/(?P<page>\w+)/$', community_view.sort_comm_list),
    url(r'^comm/text_view/(?P<topic>\w+)/$', community_view.view_topic_text),
    url(r'^create_focus/$', community_view.create_focus),
    url(r'^collect_comment/$', community_view.collect_comment),

]

urls = urlpatterns
