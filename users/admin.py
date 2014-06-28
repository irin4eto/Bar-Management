from django.contrib import admin
from users.models import UserProfile

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'role',
        'user'
    ]

admin.site.register(UserProfile, UsersAdmin)
