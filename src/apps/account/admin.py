from django.contrib import admin
from apps.account.models import *


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password', 'username', 'last_login', 'date_joined','get_salary')
    search_fields = ['phone', 'email']
    list_display = ('username', 'get_salary',)
    list_filter = ('position',)



admin.site.register(User, UserAdmin)
admin.site.register(City)
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(Country)
admin.site.register(ContactUs)

