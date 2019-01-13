#from django.forms import ModelForm
from django import forms
from apps.account.models import User, ContactUs


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
            'password',
        ]