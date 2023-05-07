# -*- coding: utf-8 -*-
from django.db import models


class Comment(models.Model):
    content = models.TextField(u'评论内容', null=True)
    like_count = models.IntegerField(u'点赞数量', default=0, null=True)
    parent_id = models.IntegerField(u'目标id', null=True, db_index=True)
    parent_type = models.CharField(u'目标类型', max_length=256, null=True, db_index=True)
    parent_comment = models.IntegerField(u'上级评论', null=True, db_index=True)
    target_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='评论目标用户id', on_delete=models.CASCADE)
    is_active = models.BooleanField(u'是否显示', default=True)
    create_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='创建人',on_delete=models.CASCADE)
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    write_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='更新人',on_delete=models.CASCADE)
    write_date = models.DateTimeField(u'更新时间', auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = u'评论表'
        verbose_name_plural = u'评论表'
        db_table = 'base_comment'
