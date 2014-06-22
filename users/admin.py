from django.contrib import admin
from users.models import UserProfile

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'role',
        'first_name',
        'last_name'
    ]

admin.site.register(UserProfile, UsersAdmin)
