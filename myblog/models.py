from django.db import models


# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=255)
    images = models.ImageField(upload_to='images/')
    descr = models.TextField()
    postdate = models.DateTimeField()
