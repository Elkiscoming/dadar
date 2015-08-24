from django.contrib.gis.db import models

# Create your models here.


class User(models.Model):
    pass


class UserAction(models.Model):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=700)


class Venue(models.Model):
    user = models.ManyToManyField(User)
    foursquare_id = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    lat = models.FloatField()
    lng = models.FloatField()
    image = models.CharField(max_length=500)
    categories = models.ManyToManyField(Category)
