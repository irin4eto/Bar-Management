from django.contrib import admin
from waiter.models import Waiter

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'waiter',
        'waiter_email',
        'waiter_first_name',
        'waiter_last_name',
    ]

    def waiter_email(self, instance):
        return instance.waiter.email

    def waiter_first_name(self, instance):
        return instance.waiter.first_name

    def waiter_last_name(self, instance):
        return instance.waiter.last_name

admin.site.register(Waiter, UsersAdmin)
