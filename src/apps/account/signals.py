from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.account.models import User


@receiver(pre_save, sender=User)
def user_pre_save(sender, **kwargs):
    print('111111')