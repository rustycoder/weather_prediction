from django.db import models
from datetime import datetime    

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    joined_datetime = models.DateTimeField(default=datetime.now, blank=True)