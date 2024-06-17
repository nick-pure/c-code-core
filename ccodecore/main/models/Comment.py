from django.contrib.auth import get_user_model
from .Post import Post
from django.db import models
import uuid


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    author = models.ForeignKey(get_user_model(), related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)