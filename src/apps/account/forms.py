#from django.forms import ModelForm
from django import forms
from apps.account.models import User, ContactUs, RequestDayOff
from django.db.models import Q
import numpy as np


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

class ContactUsForm (forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = [
            'email_from',
            'title',
            'text'
        ]

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
            if cleaned_data['type'] is 3:
                if cleaned_data['date_from'] != cleaned_data['date_to']:
                    self.add_error('date_to', 'date_from must be equal to date_to')
            if np.busday_count(cleaned_data['date_from'],
                               cleaned_data['date_to']) > 20:
                self.add_error('date_to', 'You can request 20 days maximum')
            if np.busday_count(cleaned_data['date_from'], cleaned_data['date_to']) > self.user.vacations_days:\
                self.add_error('date_to', "You can't more days, than you have")

            # 1 dayoff is only for one day (more is vacation)
            # 2 date_to should be less than date_from
            # 3 date_from - date_to (in days) should not be greater than 20 (do not count weekends)
            # 4 dayoffs/vacation cannot be more than user has (user.vacation >= days)
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance