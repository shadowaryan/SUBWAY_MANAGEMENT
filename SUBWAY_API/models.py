from datetime import datetime
from django.db import models

# Create your models here.
class Record(models.Model):
    user_id = models.CharField(max_length=300,blank=False)
    station_id = models.CharField(max_length=300,blank=False)
    action = models.CharField(max_length=64)   #swipe_in, swipe_out
    datetime = models.DateTimeField(blank=False) 