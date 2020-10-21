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
    banner1=models.ImageField(upload_to='imgs')
    banner2=models.ImageField(upload_to='imgs')
    banner3=models.ImageField(upload_to='imgs')
    banner4=models.ImageField(upload_to='imgs')
    banner5=models.ImageField(upload_to='imgs')
    style = models.CharField("style1-style6",max_length=10)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    review = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    img= models.ImageField(upload_to='imgs')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Booking(models.Model):
    place = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    number= models.CharField(max_length=10)
    package= models.CharField(max_length=50)
    package_prize = models.IntegerField()
    date = models.DateField()


class Enquirie(models.Model):
    package = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    # urgent = models.BooleanField()
    message =models.TextField()

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    rating = models.IntegerField()

