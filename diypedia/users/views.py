from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, UpdateView

from posts.models import *

from .forms import RegisterUserForm
from .models import *


class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UpdateProfileView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'profile_photo']
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


def my_profile(request):
    user = request.user
    my_posts = Post.objects.filter(author=user)
    context = {
        'posts': my_posts,
        'profile': user
    }
    return render(request, 'registration/profile.html', context=context)