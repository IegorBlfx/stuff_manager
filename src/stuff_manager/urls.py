from django.contrib import admin
from django.urls import path, include

from django.conf import settings  # correct way to import django settings
# from stuff_manager import settings # NEVER DO THIS


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls', namespace='account')),
    path('auth/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    # we don't want to use toolbar with debug=True
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns