import uuid
from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=63)
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, blank=False, null=False, editable=False)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=False, blank=True)
    creation_data = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_login = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)

