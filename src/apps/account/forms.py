from django.forms import ModelForm

from apps.account.models import User, ContactUs , RequestDayOff



class ProfileForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'age', 'email',
            'first_name', 'last_name',
            'city'
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ContactUsForm (ModelForm):

    class Meta:
        model = ContactUs
        fields = [
            'email_from',
            'title',
            'text'
        ]


class RequestDayOffForm(ModelForm):

    class Meta:
        model = RequestDayOff
        fields = [
            'name',
            'user',
            'from_date',
            'to_date'
        ]

    def clean(self):
        start_date = self.cleaned_data.get("from_date")
        end_date = self.cleaned_data.get("to_date")
        if end_date < start_date:
            raise ValueError('incorrect Value')
