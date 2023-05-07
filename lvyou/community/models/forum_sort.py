# -*- coding: utf-8 -*-
from django.db import models



class ForumSort(models.Model):
    name = models.CharField(u'分类标题', max_length=256)
    describe = models.TextField(u'分类描述', null=True)
    source = models.CharField(u'源数据', max_length=256, null=True)
    url = models.CharField(u'url', max_length=256, null=True)
    icon = models.CharField(u'图标', max_length=256, null=True)
    a_public = models.BooleanField(u'是否公开', default=True)
    create_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='创建人', on_delete=models.CASCADE)
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    write_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='更新人', on_delete=models.CASCADE)
    write_date = models.DateTimeField(u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'论坛分类'
        verbose_name_plural = u'论坛分类'
        db_table = 'comm_forum_sort'
