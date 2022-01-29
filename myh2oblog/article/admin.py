from django.contrib import admin
from . import models

admin.site.register(models.Categories)
admin.site.register(models.Tags)
admin.site.register(models.Articles)
