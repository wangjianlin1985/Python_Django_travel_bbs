# -*- coding: utf-8 -*-
from django.db import models


class TempTelCode(models.Model):
    telphone = models.BigIntegerField(u'手机号', null=True, db_index=True)
    code = models.IntegerField(u'验证码', null=True, db_index=True)
    write_date = models.DateTimeField(u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'临时手机号验证码表'
        verbose_name_plural = u'临时手机号验证码表'
        db_table = 'temp_tel_code'
