import uuid
from django.contrib.auth import get_user_model
from django.db import models


class Friend(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(get_user_model(), related_name='friends', on_delete=models.CASCADE)
    friend = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255) # Исправить это на наследование из класса со статусами