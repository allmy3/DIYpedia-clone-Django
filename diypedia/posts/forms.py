from django import forms

from .models import *


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['slug', 'category', 'poster', 'title', 'content']


class ChangePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['slug', 'category', 'poster', 'title', 'content']