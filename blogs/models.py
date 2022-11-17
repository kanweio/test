from django.db import models


# Create your models here.


class Category(models.Model):
    post = models.ImageField
    Hashtag = models.ManyToManyField


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    quality = models.DecimalField(max_digits=10, decimal_places=1)
