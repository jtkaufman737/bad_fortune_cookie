from django.db import models
from .apps import FortunesConfig

# Create your models here.
class Fortune(models.Model):
    id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=100)
    fortune = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    app_label = FortunesConfig
