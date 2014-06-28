from django.contrib import admin
from manager.models import Manager

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'manager',
        'manager_email',
        'manager_first_name',
        'manager_last_name',
    ]

    def manager_email(self, instance):
        return instance.manager.email

    def manager_first_name(self, instance):
        return instance.manager.first_name

    def manager_last_name(self, instance):
        return instance.manager.last_name

admin.site.register(Manager, UsersAdmin)
