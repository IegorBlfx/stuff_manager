from django.forms import ModelForm

from apps.account.models import User, ContactUs


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
        # TODO

class ContactUsForm (ModelForm):

    class Meta:
        model = ContactUs
        fields = [
            'email_from',
            'title',
            'text'
        ]

