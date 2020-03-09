from django.db import models
from django.contrib.postgres.fields import JSONField
import uuid


class MyUsers(models.Model):
    email = models.EmailField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    api_key = models.UUIDField(primary_key=True, default=uuid.uuid4())

    def __str__(self):
        return self.email


class Albums(models.Model):
    name = models.CharField(max_length=40)
    user_id = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
    metadata = JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tracks(models.Model):
    name = models.CharField(max_length=40)
    album_id = models.ForeignKey(Albums, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
