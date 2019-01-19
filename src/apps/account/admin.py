from django.contrib import admin
from apps.account.models import *
from apps.account.forms import UserAdminForm
from apps import model_choices as mch


class UserAdmin(admin.ModelAdmin):
    readonly_fields = []
    search_fields = ['phone', 'email']
    list_display = ('username', 'get_salary',)
    list_filter = ('position',)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['password', 'username', 'last_login', 'date_joined','get_salary']
        return []

    def get_form(self, request, obj=None, **kwargs):
            if obj is None:
                return UserAdminForm
            else:
                return super().get_form(request, obj, **kwargs)
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
    readonly_fields = []
    list_display = ('user', 'status',)
    list_filter = ('type', 'status',)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            if obj.status != mch.STATUS_PENDING:
                return ['user', 'created', 'date_from', 'date_to','type', 'reason', 'status']
        return []




