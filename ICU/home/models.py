from email.mime import image
from turtle import title
from django.db import models

# Create your models here.
class picture(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField()

    def __str__(self) -> str:
        return super().__str__()

    def save(self, *arg, **kwargs):
        super().save(*arg, **kwargs)