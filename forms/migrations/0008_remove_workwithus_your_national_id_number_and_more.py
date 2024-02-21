# Generated by Django 4.2.4 on 2024-02-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_rename_number_of_credits_passed_workwithus_your_national_id_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workwithus',
            name='your_national_id_number',
        ),
        migrations.AddField(
            model_name='workwithus',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='workWithUs/cv_file'),
        ),
        migrations.AddField(
            model_name='workwithus',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در'),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='firstName',
            field=models.CharField(max_length=500, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='lastName',
            field=models.CharField(max_length=500, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=250, verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, verbose_name='به روز شده در'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(blank=True, verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(blank=True, max_length=250, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='number',
            field=models.CharField(blank=True, max_length=250, verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(blank=True, max_length=500, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='entrepreuneur',
            name='companyName',
            field=models.CharField(max_length=300, verbose_name='نام شرکت'),
        ),
        migrations.AlterField(
            model_name='entrepreuneur',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در'),
        ),
        migrations.AlterField(
            model_name='entrepreuneur',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='entrepreuneur',
            name='fieldOfProfessional',
            field=models.CharField(max_length=500, verbose_name='زمینه حرفه ای'),
        ),
        migrations.AlterField(
            model_name='entrepreuneur',
            name='phone',
            field=models.CharField(max_length=300, verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='entrepreuneur',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, verbose_name='به روز شده در'),
        ),
        migrations.AlterField(
            model_name='entrepreuneur',
            name='website',
            field=models.CharField(max_length=500, verbose_name='سایت'),
        ),
        migrations.AlterField(
            model_name='handicraft',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در'),
        ),
        migrations.AlterField(
            model_name='handicraft',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='handicraft',
            name='first_name',
            field=models.CharField(max_length=500, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='handicraft',
            name='last_name',
            field=models.CharField(max_length=500, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='handicraft',
            name='organization',
            field=models.CharField(max_length=500, verbose_name='سازمان'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='birthDate',
            field=models.DateField(blank=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='companyName',
            field=models.CharField(blank=True, max_length=500, verbose_name='اسم شرکت'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='countryOfResidence',
            field=models.CharField(blank=True, max_length=500, verbose_name='کشور اقامت'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='firstName',
            field=models.CharField(blank=True, max_length=500, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='howDidYouKnowUs',
            field=models.CharField(blank=True, max_length=500, verbose_name='چگونه با ما آشنا شدید'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='interests',
            field=models.CharField(blank=True, max_length=500, verbose_name='علاقه ها'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='lastName',
            field=models.CharField(blank=True, max_length=500, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='preferredAreas',
            field=models.CharField(blank=True, max_length=500, verbose_name='زمینه موردعلاقه'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='provinceOfResidence',
            field=models.CharField(blank=True, max_length=500, verbose_name='استان اقامت'),
        ),
        migrations.AlterField(
            model_name='investorregistration',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, verbose_name='به روز شده در'),
        ),
        migrations.AlterField(
            model_name='landagene',
            name='company_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='نام شرکت'),
        ),
        migrations.AlterField(
            model_name='landagene',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در'),
        ),
        migrations.AlterField(
            model_name='landagene',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='landagene',
            name='full_name',
            field=models.CharField(max_length=500, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='landagene',
            name='phone_number',
            field=models.CharField(blank=True, max_length=250, verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='birthDate',
            field=models.DateField(blank=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='companyName',
            field=models.CharField(blank=True, max_length=500, verbose_name='اسم شرکت'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='countryOfResidence',
            field=models.CharField(blank=True, max_length=500, verbose_name='کشور اقامت'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='firstName',
            field=models.CharField(blank=True, max_length=500, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='howDidYouKnowUs',
            field=models.CharField(blank=True, max_length=500, verbose_name='چگونه با ما آشنا شدید'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='investmentCeiling',
            field=models.CharField(blank=True, max_length=500, verbose_name='سقف سرمایه گذاری'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='lastName',
            field=models.CharField(blank=True, max_length=500, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='provinceOfResidence',
            field=models.CharField(blank=True, max_length=500, verbose_name='استان اقامت'),
        ),
        migrations.AlterField(
            model_name='partnermembership',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, verbose_name='به روز شده در'),
        ),
    ]
