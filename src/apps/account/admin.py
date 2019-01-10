from django.contrib import admin
from apps.account.models import *


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password', 'username', 'last_login', 'date_joined','get_salary')
    search_fields = ['phone', 'email']
    list_display = ('username', 'get_salary',)
    list_filter = ('position',)


admin.site.register(User, UserAdmin)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    pass


@admin.register(RequestDayOff)
class RequestDayOffAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'from_date', 'to_date')


