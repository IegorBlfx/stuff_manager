from django.core.mail import send_mail
from django.conf import settings


def _email(request, email_for):
    subject = 'Thank you for your information'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [f'{email_for}', ]
    send_mail(subject, message, email_from, recipient_list)

