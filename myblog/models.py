from django.db import models


# Create your models here.
class Blog (models.Model):
    descr = models.TextField()
    images = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
