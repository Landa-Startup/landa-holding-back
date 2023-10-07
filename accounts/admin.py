from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Roles
# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display=['email']
    ordering=('email',)

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Roles)
