from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
from datetime import date




class User(AbstractUser):

    age = models.PositiveSmallIntegerField(null=True, blank=True)  # TODO validate age >= 18
    phone = PhoneField(blank=True, help_text='Contact phone number')
    city = models.ForeignKey('account.City', null=True, on_delete=models.SET_NULL)
    address = models.TextField(null=True, blank=True)
    position = models.ForeignKey('account.Position', null=True, on_delete=models.SET_NULL)
    #salary = models.ForeignKey('account.Position',related_name='salary+', null=True, on_delete=models.SET_NULL)
    hired = models.DateField(default=date.today())
    #vacation_balance = models.ForeignKey(
    #    'account.Position',
    #    to_field='vocation_on_position',
    #    on_delete=models.SET_NULL
    #)


class City(models.Model):
    name = models.TextField(
        null=False,
        blank=False,
        unique=True,
        max_length=100
     )

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.TextField(null=True, blank=True, unique=True,)
    department = models.ForeignKey('account.Department',null=True ,on_delete=models.SET_NULL)
    salary = models.CharField(max_length=10)
    vocation_on_position = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.TextField(
        null=True,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.name
