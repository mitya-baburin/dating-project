from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    hobbies = models.TextField()
    status = models.CharField(max_length=20)
    gallery = models.JSONField()  # Ссылки на фотографии
    likes_count = models.PositiveIntegerField(default=0)
    privacy_settings = models.JSONField()  # Приватность