from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class PostAdminForm(forms.ModelForm):
    content_ru = forms.CharField(label='Содержание', widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label='Content', widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ['title', 'slug', 'category', 'author', 'likes_count', 'views', 'date']
    list_editable = ['likes_count', 'views']
    list_display_links = ['title', 'author']
    search_fields = ['title']
    list_filter = ['category']


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name', 'slug']
    list_editable = ['slug']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']
    list_display_links = ['user', 'post']
    search_fields = ['user']