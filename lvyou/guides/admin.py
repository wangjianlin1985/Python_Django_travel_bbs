from django.contrib import admin
from guides.models.guide_content import Guidebody
from guides.models.guide_title import GuideTitle
# Register your models here.

admin.site.register([Guidebody, GuideTitle])