import os
from django.conf import settings
import qrcode
from django.contrib import admin
from django.shortcuts import get_object_or_404
from user_profile.models import Profile
from config.settings import MEDIA_ROOT
from .models import QRCodeData

class QRCodeDataAdmin(admin.ModelAdmin):
    list_display = ('profile', 'display_qr_code')

    def display_qr_code(self, obj):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=1,
        )
        profile = get_object_or_404(Profile,pk=obj.profile.pk)
        qr.add_data(f'https://landaholding.com/en/profile/{profile.username}')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        os.makedirs(os.path.join(MEDIA_ROOT, 'qr_codes',f'{profile.username}'), exist_ok=True)
        img_root = os.path.join(MEDIA_ROOT, 'qr_codes',f"{profile.username}", f"{profile.first_name}_{profile.last_name}.png")
        img.save(img_root)  
        base_url = settings.MEDIA_URL
        base_dir = settings.MEDIA_ROOT
        img_root = img_root.replace(base_dir+'/', '')
        clean_url = base_url + img_root
        profile.qrcode_image = img_root
        profile.save()

        return clean_url

admin.site.register(QRCodeData, QRCodeDataAdmin)
