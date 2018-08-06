from django.contrib import admin
from .models import BlogSettings


@admin.register(BlogSettings)
class BlogSettingsAdmin(admin.ModelAdmin):
    list_display = ('num_pages',)
