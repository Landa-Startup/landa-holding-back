from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True,max_length=300)
    first_name = models.CharField(_("First Name"),blank=False,null=False,max_length=300)
    last_name = models.CharField(_("Last Name"),blank=False,null=False,max_length=300)
    phone_number = models.CharField(_("Phone Number"),blank=False,null=False,max_length=300,unique=True)
    id_number = models.CharField(_("ID Number"),blank=False,null=False,max_length=300,unique=True)
    code = models.CharField(_("Employe Code"),blank=False,null=False,max_length=300,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    employer = models.ForeignKey("CustomUser",verbose_name="employer",on_delete=models.CASCADE)
    emails = models.ManyToManyField("CustomUser",related_name="user_emails")
    roles = models.ManyToManyField("Roles",related_name="users_role")
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone_number','code','id_number','first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Roles(models.Model):
    role = models.CharField("role name",max_length=300)
    
    def __str__(self):
        return self.role
    