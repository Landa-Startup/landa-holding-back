# Generated by Django 4.2.4 on 2024-01-04 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_alter_profile_websites'),
        ('qrcode_generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodedata',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='user_profile.profile', verbose_name='پروفایل'),
        ),
    ]
