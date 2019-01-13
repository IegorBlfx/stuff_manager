#from django.forms import ModelForm
from django import forms
from apps.account.models import User, ContactUs
from django.db.models import Q


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


    #def save(self, commit=True):
        #instance = super().save(commit=False)
        #instance.username = instance.email
        #if commit:
            #instance.save()
        #return instance
