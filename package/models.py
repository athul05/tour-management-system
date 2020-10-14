from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='imgs')
    prize1 = models.IntegerField()
    prize2 = models.IntegerField()
    season = models.CharField(max_length=50)
    duration = models.IntegerField()
    food = models.BooleanField(default=False)

    

