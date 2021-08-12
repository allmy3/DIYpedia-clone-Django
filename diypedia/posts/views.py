from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, View
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .utils import CheckAuthorMixin
from .forms import NewPostForm, ChangePostForm
from .models import *


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        search_query = self.request.GET.get('q', '')
        if search_query:
            posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
        else:
            posts =  Post.objects.order_by('-date')
        context['posts'] = posts
        return context


class PostsByCategoryView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'])
    

def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Временная система просмотров
    if request.user.is_authenticated:
        if request.user != post.author:
            post.views += 1
            post.save()

    context = {'post': post}
    return render(request, 'post_detail.html', context)


class PopularPostsView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-views')


def new_post_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('post_detail', args=[new_post.slug]))
    else:
        form = NewPostForm()

    return render(request, 'new_post.html', {'form': form})


class DeletePostView(CheckAuthorMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')


class UpdatePostView(CheckAuthorMixin, UpdateView):
    model = Post
    form_class = ChangePostForm
    context_object_name = 'post'
    template_name = 'update_post.html'
    success_url = reverse_lazy('index')


@login_required(login_url = reverse_lazy('login'))
def like(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)

        current_post_likes = post.likes_count
        liked = Like.objects.filter(user=user, post=post)

        if not liked:
            like = Like.objects.create(user=user, post=post)
            current_post_likes = current_post_likes + 1
            post.liked.add(user)
        else:
            Like.objects.filter(user=user, post=post).delete()
            current_post_likes = current_post_likes - 1
            post.liked.remove(user)

        post.likes_count = current_post_likes
        post.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))