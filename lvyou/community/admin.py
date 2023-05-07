from django.contrib import admin

from .models.topic_text import TopicText
from .models.comment import Comment
# Register your models here.

admin.site.register([TopicText,Comment])
