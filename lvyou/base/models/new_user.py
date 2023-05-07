# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, UserManager


class NewUser(User):
    '''
    这两种方法都可以对user表进行重写
    '''
    show_name = models.CharField(u'显示名称', max_length=255, null=True)
    avatar = models.ForeignKey(u'mycenter.ImgMaterial', related_name='+', verbose_name=u'用户头像', null=True,on_delete=models.CASCADE)
    avatar_path = models.CharField(u'头像路径', max_length=255, null=True)
    telephone = models.CharField(u'电话', max_length=255, null=True)
    auth_code = models.CharField(u'验证码', max_length=255, null=True)
    signatrue = models.CharField(u'签名', max_length=255, null=True)
    send_date = models.DateTimeField(u'发送时间', null=True)
    home_path = models.CharField(u'主页路径', max_length=255, null=True)
    home_img = models.ForeignKey(u'mycenter.ImgMaterial', related_name='+', verbose_name=u'主页图片', null=True,on_delete=models.CASCADE)
    sex = models.BooleanField(u'性别', default=True)
    abstract = models.TextField(u'简介', null=True)
    objects = UserManager()

# class NewUser(models.Model):
#     user = models.OneToOneField(User)
#     show_name = models.CharField(u'显示名称', max_length=255, null=True)
#     telephone = models.CharField(u'电话', max_length=255, null=True)
