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

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            return not obj.is_superuser
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.exclude(is_superuser=True)

        return qs
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
    readonly_fields = ('user', 'type')
    list_display = ('user', 'status',)
    list_filter = ('type', 'status',)
    #TODO ADD form

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(self, request)
        if obj is not None:
            if obj.status != mch.STATUS_PENDING:
                readonly_fields += ('created', 'date_from', 'date_to', 'reason', 'status')
                return readonly_fields




