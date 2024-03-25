from django.contrib import admin
from documents import models

admin.site.register(models.Document)
admin.site.register(models.DocumentShare)

