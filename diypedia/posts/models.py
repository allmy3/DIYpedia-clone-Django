from django.db import models
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField("URL для категории", unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Post(models.Model):
    slug = models.SlugField("URL")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор', related_name='author_of_post')
    poster = models.ImageField("Постер", upload_to='post_posters/')
    title = models.CharField("Название статьи", max_length=70)
    content = RichTextUploadingField(blank=True, null=True)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория поста')
    likes_count = models.PositiveIntegerField(default=0, verbose_name="Лайки")
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='post_for_like')

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
