from django.urls import path

from apps.account.views import index, profile, contact_us, request_day_off

app_name = 'account'

urlpatterns = [
    path('index/', index, name='index'),
    path('profile/<int:user_id>', profile, name='profile'),
    path('contact-us', contact_us, name='contact-us'),
    path('request-day-off/<int:user_id>', request_day_off, name='days_off')
]