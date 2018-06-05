from django.contrib import admin
from .models import  Cook


class CookAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Cook, CookAdmin)