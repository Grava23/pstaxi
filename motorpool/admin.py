from django.contrib import admin
from . import models

@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
  pass
# Register your models here.
