from django.contrib import admin
from . import models

admin.site.site_header = '吾水后台管理'
admin.site.site_title = '吾水后台管理'
admin.site.index_title = '吾水后台管理'

admin.site.register(models.Categories)
admin.site.register(models.Tags)
admin.site.register(models.Articles)
