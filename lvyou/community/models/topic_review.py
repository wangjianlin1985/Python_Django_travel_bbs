# -*- coding: utf-8 -*-
from django.db import models



class TopicReview(models.Model):
    review_text = models.TextField(u'评论内容', null=True)
    topic_text = models.ForeignKey('community.TopicText', blank=True, null=True, related_name='+', verbose_name='帖子名称', on_delete=models.CASCADE)
    forum_sort = models.ForeignKey('community.ForumSort', blank=True, null=True, related_name='+', verbose_name='分类名称', on_delete=models.CASCADE)

    create_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='创建人',on_delete=models.CASCADE)
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    write_user = models.ForeignKey('auth.User', blank=True, null=True, related_name='+', verbose_name='更新人',on_delete=models.CASCADE)
    write_date = models.DateTimeField(u'更新时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'评论表'
        verbose_name_plural = u'评论表'
        db_table = 'comm_topic_review'
