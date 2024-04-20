from django.contrib import admin
from . import models

admin.site.register(models.CustomUser)
admin.site.register(models.Package)
admin.site.register(models.BookATour)
admin.site.register(models.Destination)
