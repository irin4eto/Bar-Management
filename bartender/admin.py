from django.contrib import admin
from bartender.models import Bartender

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'bartender',
        'bartender_email',
        'bartender_first_name',
        'bartender_last_name',
    ]

    def bartender_email(self, instance):
        return instance.bartender.email

    def bartender_first_name(self, instance):
        return instance.bartender.first_name

    def bartender_last_name(self, instance):
        return instance.bartender.last_name

admin.site.register(Bartender, UsersAdmin)
