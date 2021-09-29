from django.conf import settings
from django.db import models

# from django.utils import timezone


# Create your models here.
class Post(models.Model):
  pass

class UserImage(models.Model):
  image = models.ImageField(verbose_name='画像', upload_to='images/')