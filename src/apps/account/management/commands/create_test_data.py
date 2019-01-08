from uuid import uuid4 # geneartor of random symbols
from django.core.management.base import BaseCommand
from apps.account.models import User, City
import random
import names

class Command (BaseCommand):
    help = 'Create test data'

    def handle(self, *args, **options):
        User.objects.exclude(username='admin').delete()
        result = [] # fill list

        cities = []
        for name in ('Kiev','Odessa','Lviv','Dnipro'):
            city,_ = City.objects.get_or_create(name=name)
            cities.append(city)
        for i in range(10_000):
            a = str(i)
            username = names.get_first_name() + a
            user=User(
                username=username,
                email=username + '@example.com',
                age=random.randint(18,65),
                first_name=names.get_first_name(),
                last_name=names.get_last_name(),
                city=random.choice(cities),
                )
            result.append(user)
        User.objects.bulk_create(result) # create object from list
