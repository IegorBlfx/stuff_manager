from django.contrib import admin
from apps.account.models import *
from apps.account.forms import UserAdminForm


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
admin.site.register(City)
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(Country)
admin.site.register(ContactUs)

