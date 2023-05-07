"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from views import User
from . import views
import guides.urls as guides_urls
import mycenter.urls as cemter_urls
import home.urls as home_urls
import community.urls as commun_urls
import base.urls as base_urls

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.get_login),
    url(r'^user/login/$', views.alogin),
    url(r'^loginout/$', views.loginout),
    url(r'^to_register/$', views.to_register),
    url(r'^register/$', views.register),
    url(r'^get_tel_code/$', views.get_tel_code),

    url(r'^guide/', include(guides_urls.urls)),
    url(r'^mycenter/', include(cemter_urls.urls)),
    url(r'^home/', include(home_urls.urls)),
    url(r'^community/', include(commun_urls.urls)),
    url(r'^base/', include(base_urls.urls)),

]
