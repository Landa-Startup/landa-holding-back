# Generated by Django 4.2.4 on 2024-03-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0012_entrepreuneur_first_name_entrepreuneur_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnermembership',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=250, verbose_name='شماره موبایل'),
        ),
    ]