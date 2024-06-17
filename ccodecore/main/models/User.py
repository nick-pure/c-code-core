import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nickname = models.CharField(max_length=63, blank=False, unique=True)
    first_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=15, blank=False)
    photo = models.ImageField(upload_to='uploads/', blank=True, )

    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=False, blank=False)

    last_login = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username} {self.nickname}'

