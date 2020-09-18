from django.db import models


# Create your models here.
class Job (models.Model):
    images = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=150)
    # postdate = models.DateTimeField()
    # date = models.DateTimeField()
