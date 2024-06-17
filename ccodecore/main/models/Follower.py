import uuid
from django.contrib.auth import get_user_model
from django.db import models


class Follower(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    follower = models.ForeignKey(get_user_model(), related_name='followings', on_delete=models.CASCADE)
    following = models.ForeignKey(get_user_model(), related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)