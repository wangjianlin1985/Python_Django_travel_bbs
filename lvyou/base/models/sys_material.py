# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class SysMaterial(models.Model):
    key = models.CharField('key', max_length=256, null=True)
    value = models.TextField('value', null=True)
    note = models.TextField(u'备注', null=True)
    group = models.CharField('分组', max_length=256, null=True)

    create_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='创建人', on_delete=models.CASCADE)
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    write_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='更新人', on_delete=models.CASCADE)
    write_date = models.DateTimeField(u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'系统素材表'
        verbose_name_plural = u'系统素材表'
        db_table = 'base_sys_material'
