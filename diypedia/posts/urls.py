from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('popular/', PopularPostsView.as_view(), name='popular_posts'),
    path('posts-by-category/<slug:category_slug>/', PostsByCategoryView.as_view(), name='category'),
    path('post-detail/<slug:slug>/', post_detail_view, name='post_detail'),
    path('create-post/', new_post_view, name='new_post'),
    path('delete-post/<slug:slug>/', DeletePostView.as_view(), name='delete_post'),
    path('update-post/<slug:slug>/', UpdatePostView.as_view(), name='update_post'),
    path('like-post/', like, name='like'),
]