from tkinter import CASCADE
from django.db import models
from django.utils import timezone


class Post(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    avatar = models.ImageField()
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    parent_comment = models.ForeignKey('self', on_delete=CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
