from django.contrib import admin
from apps.account.models import User, City, Position, Department

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password', 'username', 'last_login', 'date_joined')


admin.site.register(User, UserAdmin)
admin.site.register(City)
admin.site.register(Position)
admin.site.register(Department)

