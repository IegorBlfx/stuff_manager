from django.contrib import admin
from apps.account.models import User

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password',)
admin.site.register(User, UserAdmin)

#TODO make readonly fields: username; date_joined, password, last_login