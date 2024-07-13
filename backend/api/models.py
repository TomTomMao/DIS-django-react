from django.db import models

# Create your models here.


# This Python class defines a Vehicle model with attributes for make, model, colour, and licence.
class Vehicle(models.Model):

    make = models.CharField(max_length=20, null=True)
    model = models.CharField(max_length=20, null=True)
    color = models.CharField(max_length=20, null=True)
    plateNumber = models.CharField(max_length=7, null=True)


class People(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True)
    license = models.CharField(max_length=16, unique=True, null=True)
    dob = models.DateField(null=True)


class Ownership(models.Model):
    people = models.ForeignKey('People', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)

