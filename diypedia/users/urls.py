from django.urls import path

from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('edit-profile/', UpdateProfileView.as_view(), name='edit_profile'),
    path('my-profile/', my_profile, name='my_profile'),
]