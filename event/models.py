from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator

# Create your models here.

class Event(models.Model):
    slug = models.SlugField(unique=True)
    start_date = models.DateTimeField('تاریخ شروع', null=False)
    end_date = models.DateTimeField('تاریخ پایان', null=False)
    speakers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='event_speakers', verbose_name='سخنگو ها')
    description = RichTextField(verbose_name='توضیحات')
    banner = models.ImageField(upload_to="events/banner/images", verbose_name='بنر')
    video = models.FileField(upload_to='events/videos',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], verbose_name='ویدئو')
    created_at = models.DateTimeField('ساخته شده در', auto_now_add=True)
    updated_at = models.DateTimeField('به روز شده در', auto_now=True)


class Images(models.Model):
    image = models.ImageField(upload_to='events/images', height_field=None, width_field=None, max_length=None, verbose_name='تصویر')
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='event_images', verbose_name='رویداد')

class EventForm(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL,null=True, verbose_name='رویداد')
    email = models.EmailField(max_length=254, verbose_name='ایمیل')
    phone = models.CharField('شماره موبایل', max_length=11)
    reserved_count = models.IntegerField('تعداد رزرو', default=1)
    created_at = models.DateTimeField('ساخته شده در', auto_now_add=True)
    updated_at = models.DateTimeField('به روز شده در', auto_now=True)
