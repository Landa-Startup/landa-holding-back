# Generated by Django 4.2.4 on 2023-12-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=400, unique=True, verbose_name='لینک وبسایت')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='website/logo', verbose_name='لوگو وبسایت')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='websites',
        ),
        migrations.AddField(
            model_name='profile',
            name='websites',
            field=models.ManyToManyField(to='user_profile.website'),
        ),
    ]