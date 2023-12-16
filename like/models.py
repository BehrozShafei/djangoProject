from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
# from django.contrib.contenttypes.models import
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Like(models.Model):
    title = models.CharField(max_length=255)


class LikeItem(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_Object = GenericForeignKey()
