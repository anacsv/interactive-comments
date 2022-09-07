from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField()
    comment = models.CharField(max_length=280)
    created_date = models.DateTimeField(default=timezone.now)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
