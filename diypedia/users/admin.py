from django.contrib import admin

from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'last_name', 'first_name', 'email']
    list_display_links = ['id', 'username']
    search_fields = ['username']
    list_filter = ['first_name', 'last_name']
