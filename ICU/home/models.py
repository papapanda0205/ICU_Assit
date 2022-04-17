from email.mime import image
from turtle import title
from django.db import models

# Create your models here.
class picture(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField()

