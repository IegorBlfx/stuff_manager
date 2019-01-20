from django.db import models, IntegrityError
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
from datetime import date
from apps import model_choices as mch





class User(AbstractUser):

    age = models.PositiveSmallIntegerField(null=True, blank=True)  # TODO validate age >= 18
    phone = PhoneField(blank=True, help_text='Contact phone number')
    city = models.ForeignKey('account.City', null=True, on_delete=models.SET_NULL, blank=True,related_name='users')
    address = models.CharField(null=True, blank=True,max_length=100)
    position = models.ForeignKey('account.Position', null=True, on_delete=models.SET_NULL)
    hired = models.DateField(default=date.today())
    vacations_days = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    sickness_days = models.PositiveSmallIntegerField(null=False,blank=False, default=0)

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

    def get_salary(self):
        if self.position is not None:
            return self.position.salary


    def get_salary_clear(self):
        tax = self.city.country.tax
        salary_clear = self.get_salary() * (1-tax/100)
        return salary_clear
    get_salary.short_description = 'Salary'

    def get_salary_clear_per_year(self):
        salary_clear_per_year = self.get_salary_clear()*12
        return salary_clear_per_year

    def get_salary_per_year(self):
        salary_per_year = self.get_salary() * 12
        return salary_per_year
    #prevent User delete


class RequestDayOff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dayoffs')
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add
    date_from = models.DateField(null=False, blank=False)
    date_to = models.DateField(null=False, blank=False)
    type = models.PositiveSmallIntegerField(
        null=False, blank=False,
        choices=mch.REQUEST_TYPES,
        default=mch.REQUEST_SICKNESS,
    )
    reason = models.CharField(max_length=256, blank=True, null=True, default=None)  # reason required when status = REJECTED
    status = models.PositiveSmallIntegerField(
        null=False, blank=False,
        choices=mch.STATUSES,
        default=mch.STATUS_PENDING,
    )

    def save(self, *args, **kwargs):
        if self.date_from > self.date_to:
            raise IntegrityError('date_from must be less, than date_to')
        super().save(*args, **kwargs)

    #def __str__(self):
        #return user thrue user_id


    # TODO
    # override save method, if date_from > date_to -> raise IntegrityError('error message') (from db)
    # override __str__ (DO NOT USE self.user)
    # def __str__(self):
#     return self.user.email  # extra DB call NEVER DO THIS!!!


class City(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
     )

    def __str__(self):
        return self.name
    country = models.ForeignKey('account.Country', null=True, blank=True, max_length=100, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Cities'

class Position(models.Model):
    name = models.TextField(null=True, blank=True, unique=True,)
    department = models.ForeignKey('account.Department', null=True, on_delete=models.SET_NULL)
    salary = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=3, default=3200)
    vocation_on_position = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.TextField(
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.name

class Country(models.Model):

    name = models.TextField(null=True, blank=True, max_length=100)
    tax = models.PositiveSmallIntegerField(null=False, blank=False, default=40)

    def __str__(self):
        return self.name


class ContactUs(models.Model):

    email_from = models.CharField(null=False, blank=False, max_length=100)
    title = models.CharField(null=False, blank=False, max_length=100)
    text = models.TextField(null=False, blank= False)

    def __str__(self):
        return self.title
# obj.get_{field}_display() -