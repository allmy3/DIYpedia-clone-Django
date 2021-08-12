from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ['name', 'slug']


@register(Post)
class PostTranslationOption(TranslationOptions):
    fields = ['slug', 'title', 'content', 'category']
