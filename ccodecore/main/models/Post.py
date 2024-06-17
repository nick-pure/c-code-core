import uuid
from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    header = models.CharField(max_length=127)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts', null=True, blank=True)


