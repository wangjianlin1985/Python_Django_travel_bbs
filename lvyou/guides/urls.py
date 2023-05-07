# -*- coding: utf-8 -*-

from django.conf.urls import url
# import views
#import views.guide as guide_view
from .views import guide
# guide =views.guide
urlpatterns = [
    url(r'^(?P<page>\w+)/$', guide.Guide),
    url(r'^view/(?P<id>\w+)/$', guide.view_essay)
]

urls = urlpatterns
