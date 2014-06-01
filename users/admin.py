from django.contrib import admin
from users.models import UserProfile

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'role',
        'first_name',
        'last_name',
    ]

    search_fields = ('role',)
    ordering = ('role',)
    filter_horizontal = ()

admin.site.register(UserProfile, UsersAdmin)
