from django.urls import path
#from django.urls import include
from apps.account.views import index, profile

urlpatterns = [
    path('index/', index),
    path('profile/<int:user_id>', profile),
]