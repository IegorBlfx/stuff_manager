#from django.forms import ModelForm
from django import forms
from apps.account.models import User, ContactUs, RequestDayOff
from django.db.models import Q
import numpy as np
from apps import model_choices as mch
from django.conf import settings
from django.core.mail import send_mail
from builtins import st

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'age', 'email',
            'first_name', 'last_name',
            'city'
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # TODO
#####################################################################
####################################################################
class ContactUsForm (forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = [
            'email_from',
            'title',
            'text'
        ]
#####################################################################
####################################################################
class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'age', 'email',
            'password'
        ]

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if User.objects.filter(Q(email=cleaned_data['email'])|
                                   Q(username=cleaned_data['email'])).exists():
                raise forms.ValidationError('User already exists')
        return cleaned_data
#####################################################################
####################################################################
class RequestDayOffAdminForm(forms.ModelForm):

    class Meta:
        model = RequestDayOff

        fields = [
        'user',
        'date_from', 'date_to',
        'type', 'reason',
        'status',
        ]
    def save(self, commit=True):
        instance = super().save(commit=False)
        cleaned_data = super().clean()
        self.user = instance.user
        #st()
        if cleaned_data['status'] == mch.STATUS_CONFIRMED:
            from apps.account.tasks import send_email_async
            send_email_async.delay(
            subject = 'Thank you for your information',
            message = ' Injoy your vacation ',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list=[f'{self.user.email}', ]
           )
        #elif cleaned_data['status'] == mch.STATUS_REJECT:
           # _email(request, email_for=cleaned_data['user'])
        if commit:
            instance.save(commit)
        return instance

#####################################################################
####################################################################
class RequestDayOffForm(forms.ModelForm):
    class Meta:
        model = RequestDayOff
        fields = ['type', 'date_from', 'date_to']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            # from pdb import set_trace
            # set_trace()
            if cleaned_data['date_from'] > cleaned_data['date_to']:
                self.add_error('date_to',
                               'date_from cannot be greater than date_to')
            if cleaned_data['type'] is mch.REQUEST_DAYOFF:
                if cleaned_data['date_from'] != cleaned_data['date_to']:
                    self.add_error('date_to', 'date_from must be equal to date_to')
            if np.busday_count(cleaned_data['date_from'],
                               cleaned_data['date_to']) > 20:
                self.add_error('date_to', 'You can request 20 days maximum')
            if np.busday_count(cleaned_data['date_from'], cleaned_data['date_to']) > self.user.vacations_days:
                self.add_error('date_to', "You can't more days, than you have")


        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save(commit)
        return instance
