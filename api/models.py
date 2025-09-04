from django.contrib.auth.models import User
from django.db import models


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

    def __str__(self):
        return self.full_name


class ViewHistory(models.Model):  # История
    viewer = models.ForeignKey(Profile, related_name="viewer", on_delete=models.CASCADE)
    viewed_profile = models.ForeignKey(
        Profile, related_name="viewed", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)


class Likes(models.Model):  # Лайки
    liker = models.ForeignKey(Profile, related_name="liker", on_delete=models.CASCADE)
    liked_profile = models.ForeignKey(
        Profile, related_name="liked", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)


class Dislikes(models.Model):  # Дизлайки
    disliker = models.ForeignKey(
        Profile, related_name="disliker", on_delete=models.CASCADE
    )
    disliked_profile = models.ForeignKey(
        Profile, related_name="disliked", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)
