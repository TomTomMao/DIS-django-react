from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
# Create your models here.


# This Python class defines a Vehicle model with attributes for make, model, colour, and licence.
class Vehicle(models.Model):
    make = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=20, null=False)
    plate_number = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self): return self.plate_number


class People(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, blank=True, null=True)
    license = models.CharField(
        max_length=16, unique=False, blank=True, null=True, validators=[])
    dob = models.DateField(verbose_name='date of birth', blank=True, null=True)

    def __str__(self): return self.first_name + ' ' + self.last_name


class Ownership(models.Model):
    people = models.ForeignKey(
        'People', on_delete=models.PROTECT, blank=True, null=True)
    vehicle = models.ForeignKey(
        'Vehicle', on_delete=models.PROTECT, null=False)

    def __str__(self): return self.people.__str__() + \
        ' - ' + self.vehicle.__str__()


class Offense(models.Model):
    description = models.CharField(max_length=50, null=False)
    max_fine = models.IntegerField(null=False)
    max_points = models.IntegerField(null=False)

    def __str__(self):
        if len(self.description) <= 20:
            return self.description
        else:
            return self.description[:20] + '...'


class Incident(models.Model):
    ownership = models.ForeignKey(
        'Ownership', on_delete=models.PROTECT, blank=True, null=True)
    people = models.ForeignKey(
        'People', on_delete=models.PROTECT, blank=True, null=True)
    offense = models.ForeignKey('Offense', on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    date = models.DateField(null=False)
    report = models.CharField(max_length=500, null=False)

    def __str__(self):
        return 'id:' + str(self.id)

    def clean(self):
        super().clean()
        if self.ownership is None and self.people is None:
            raise ValidationError('Ownership and People are both None')


class Fine(models.Model):
    amount = models.IntegerField(null=False)
    points = models.IntegerField(null=False)
    incident = models.OneToOneField(
        'Incident', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.amount}$ point: {self.points}"

    def clean(self):
        super().clean()
        if self.amount > self.incident.offense.max_fine:
            raise ValidationError('fine amount greater than max fine')
        if self.points > self.incident.offense.max_points:
            raise ValidationError('point amount greater than max point')
