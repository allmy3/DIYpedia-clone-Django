from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, blank=False, null=False, default=uuid.uuid4, editable=False)
    profile_photo = models.ImageField(upload_to='avatars/', default='avatar.png/')

