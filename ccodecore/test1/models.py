import uuid

from django.db import models


class User(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    gmail = models.CharField(max_length=255, null=False, blank=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.identifier} : {self.name} : {self.gmail}"


class Post(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField()

    def __str__(self):
        return f"{self.identifier} : {self.created_by} : {self.text}"

