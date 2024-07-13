from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# This Python class defines a Vehicle model with attributes for make, model, colour, and licence.
class Vehicle(models.Model):
    make = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=20, null=False)
    plate_number = models.CharField(max_length=7, null=False)


class People(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=True)
    license = models.CharField(max_length=16, unique=True, null=True)
    dob = models.DateField(verbose_name='date of birth', null=True)


class Ownership(models.Model):
    people = models.ForeignKey('People', on_delete=models.PROTECT, null=True)
    vehicle = models.ForeignKey(
        'Vehicle', on_delete=models.PROTECT, null=False)


class Offense(models.Model):
    description = models.CharField(max_length=50, null=False)
    max_fine = models.IntegerField(null=False)
    max_points = models.IntegerField(null=False)


class Incident(models.Model):
    ownership = models.ForeignKey(
        'Ownership', on_delete=models.PROTECT, null=True)
    people = models.ForeignKey('People', on_delete=models.PROTECT, null=True)
    offense = models.ForeignKey('Offense', on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    date = models.DateField(null=False)
    report = models.CharField(max_length=500, null=False)


class Fines(models.Model):
    amount = models.IntegerField(null=False)
    points = models.IntegerField(null=False)
    incident = models.OneToOneField(
        'Incident', on_delete=models.CASCADE, null=False)
