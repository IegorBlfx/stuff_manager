from django.urls import path
#from django.urls import include
from apps.account.views import index

urlpatterns = [
    path('index/', index),
]