from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='imgs')
    car = models.IntegerField("Car Prize (4 people)")
    van = models.IntegerField("Mini-Van Prize (12 people)")
    trav = models.IntegerField("Traveller Prize (24 people)")
    bus = models.IntegerField("Air Bus Prize (42 people)")
    description = models.TextField()
    season = models.CharField(max_length=50)
    duration = models.IntegerField()
    food = models.BooleanField(default=False)
    style = models.CharField("style1-style6",max_length=10)

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    review = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    img= models.ImageField(upload_to='imgs')
    author = models.CharField(max_length=100)

class Booking(models.Model):
    place = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    number= models.CharField(max_length=10)
    package= models.CharField(max_length=50)
    package_prize = models.IntegerField()
    date = models.DateField()

