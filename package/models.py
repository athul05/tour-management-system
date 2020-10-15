from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='imgs')
    minprize = models.IntegerField("Miniumum 4 persons")
    maxprize = models.IntegerField("Maximum 15 persons")
    season = models.CharField(max_length=50)
    duration = models.IntegerField()
    food = models.BooleanField(default=False)

    

