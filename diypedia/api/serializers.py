from rest_framework import serializers

from posts.models import *
from users.models import *


class PostListSerializer(serializers.ModelSerializer):
    ''' Серилизатор постов '''
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'category', 'author', 'title', 'date', 'slug', 'views', 'likes_count']


class PostDetailSerializer(serializers.ModelSerializer):
    ''' Серилизатор Детального поста '''
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        exclude = ['liked', 'content_ru', 'content_en', 'content', 'category_ru', 'category_en', 'slug', 'title']


class CategoryCreateSerializer(serializers.ModelSerializer):
    ''' Добавление категории '''
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    ''' Сирилизатор категории '''
    class Meta:
        model = Category
        exclude = ['name', 'slug']


