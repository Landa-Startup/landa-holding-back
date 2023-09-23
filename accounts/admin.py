from django.contrib import admin
from .models import CustomUser,Roles
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Roles)
