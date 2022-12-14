from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=280)
    created_date = models.DateTimeField(default=timezone.now)
    parent_post = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True,
        blank=True,
        related_name="replies"
        )

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    avatar = models.ImageField(upload_to='avatars', validators=[validate_image])        

    def publish(self):
        self.published_date = timezone.now()
        self.save()

