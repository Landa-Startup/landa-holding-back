from django.db import models
from user_profile.models import Profile
# Create your models here.

class QRCodeData(models.Model):
    profile = models.OneToOneField(Profile, verbose_name="پروفایل", on_delete=models.PROTECT)
    