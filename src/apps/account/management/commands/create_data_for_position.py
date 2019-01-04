from uuid import uuid4 # geneartor of random symbols
from django.core.management.base import BaseCommand
from apps.account.models import Position
import random

class Command (BaseCommand):
    help = 'Create test data for positions'

    def handle(self, *args, **options):
        Position.objects.all().delete()
        result = [] # fill list
        for i in range(10):
            a = str(i)
            vacancy = ['manager', 'specialist', 'worker', 'ceo', 'HR', 'accounter', 'tester']
            vacancy_range = ['first ', 'second ', 'assistant of the ', 'head of ', 'general ']
            name =random.choice(vacancy_range) + random.choice(vacancy) # work hard ))))
            position=Position(
                name=name,
                salary=random.randint(4300,15000),
                vocation_on_position=24
                )
            result.append(position)
        Position.objects.bulk_create(result) # create object from list
