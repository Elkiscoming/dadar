from django.contrib.gis.db import models

# Create your models here.


class User(models.Model):
    data = models.CharField(max_length=20000)


class UserAction(models.Model):
    user = models.ForeignKey(User)
    action = models.CharField(max_length=10)


class Venue(models.Model):
    foursquare_id = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    lat = models.FloatField()
    lng = models.FloatField()
    image = models.ImageField()