from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.SlugField("نام کاربری", max_length=150, unique=True, null=False, blank=False)
    first_name = models.CharField("نام",  max_length=150)
    last_name = models.CharField("نام خانوادگی",  max_length=150)
    phone_number = models.CharField("شماره تماس", max_length=11)
    email = models.EmailField("ایمیل", max_length=250)
    linkedin = models.URLField("لینکدین", unique=True, blank=True, null=True)
    whatsapp = models.URLField("واتساپ", unique=True, blank=True, null=True)
    instagram = models.URLField("اینستاگرام", unique=True, blank=True, null=True)
    telegram = models.URLField("تلگرام", unique=True, blank=True, null=True)
    websites = models.ManyToManyField('Website',blank=True)
    thumbnail = models.ImageField("عکس پروفایل",upload_to="profile/images",null=True,blank=True)
    qrcode_image = models.ImageField(upload_to='qrcodes/',default='',blank=True)
    job_title = models.CharField('عنوان شغلی', max_length=250, default='')
    
    def __str__(self) -> str:
        return self.username

class Website(models.Model):
    url = models.URLField("لینک وبسایت", max_length=400, unique=True, null=False)
    logo = models.ImageField("لوگو وبسایت", upload_to="website/logo", null=True, blank=True)

    def __str__(self) -> str:
        return self.url
