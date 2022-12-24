from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100, default=None)
    detail = models.CharField(max_length=5000, default=None)
    icon = models.CharField(max_length=200, default=None)