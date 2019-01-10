
from django.contrib import admin
from django.urls import path
from django.urls import include
from apps.account.views import tos, faq

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')),
    path('tos/', tos, name='tos'),
    path('faq/', faq, name='faq')
]
