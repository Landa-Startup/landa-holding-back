from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Roles


# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'id_number', 'code')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'roles', 'employer', 'emails', 'groups', 'image')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Roles)
