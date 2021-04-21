from django.db import models

# Create your models here.

class Time(models.Model):
    time = models.TimeField("max_length")

class Price(models.Model):
    price = models.CharField(max_length=200)