from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('email',)
