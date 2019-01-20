
from celery import shared_task

@shared_task
def task_number_one():
    print('Hello from number One')
