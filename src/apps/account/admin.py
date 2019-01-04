from django.contrib import admin
from apps.account.models import *


def get_salary(object):
    return object.get_salary
get_salary.short_description = 'Salary'

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password', 'username', 'last_login', 'date_joined')
    search_fields = ['phone']
    list_display = ('username', get_salary,)
    list_filter = ('position',)



admin.site.register(User, UserAdmin)
admin.site.register(City)
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(Country)

