from django.urls import path

from .views import *

urlpatterns = [
    path('post/', PostListAPIview.as_view(), name='api_post_list'),
    path('post/<int:pk>/', PostDetailAPIview.as_view(), name='api_post_detail'),
    path('create-category/', CategoryCreateAPIview.as_view(), name='api_create_category'),
    path('category/', CategoryListAPIview.as_view(), name='api_ategory_list'),
]