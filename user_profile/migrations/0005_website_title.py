# Generated by Django 4.2.4 on 2023-12-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_profile_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='title',
            field=models.CharField(default='', max_length=500, verbose_name='عنوان وبسایت'),
        ),
    ]