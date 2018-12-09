from django.db import models

# Create your models here.
class Fortune(models.Model):
    genre = models.CharField(max_length=100)
    fortune = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    app_label = FortunesConfig
