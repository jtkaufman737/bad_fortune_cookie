import uuid
from django.db import models
from .apps import FortunesConfig

# Create your models here.
class Fortune(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    genre = models.CharField(max_length=100)
    fortune = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    app_label = FortunesConfig
