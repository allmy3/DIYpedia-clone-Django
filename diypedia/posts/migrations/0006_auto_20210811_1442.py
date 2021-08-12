# Generated by Django 3.2.6 on 2021-08-11 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_auto_20210811_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post_en',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post_ru',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user_en',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user_ru',
        ),
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_of_post', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]