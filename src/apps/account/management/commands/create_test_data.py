from uuid import uuid4 # geneartor of random symbols
from django.core.management.base import BaseCommand
from apps.account.models import User
import random

class Command (BaseCommand):
    help = 'Create test data'

    def handle(self, *args, **options):
        result = [] # fill list
        for i in range(10_000):
            username = str(uuid4())
            user=User(
                username=username,
                email=username + '@example.com',
                age=random.randint(12,100),
                )
            result.append(user)
        User.objects.bulk_create(result) # create object from list
