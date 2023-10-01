# Generated by Django 4.2.4 on 2023-10-01 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='admin', max_length=150),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]