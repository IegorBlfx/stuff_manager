from django.urls import path

from apps.account.views import index, profile, contact_us, create_request, cache_test

app_name = 'account'

urlpatterns = [
    path('index/', index, name='index'),
    path('profile/', profile, name='profile'),
    path('contact-us', contact_us, name='contact-us'),
    path('create-request/', create_request, name='create-request'),
    path('cache_test/', cache_test, name='cache_test'),
]