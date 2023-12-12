from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator

# Create your models here.

class Event(models.Model):
    slug = models.SlugField(unique=True)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    speakers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='event_speakers')
    description = RichTextField()
    banner = models.ImageField(upload_to="events/banner/images")
    video = models.FileField(upload_to='events/videos',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Images(models.Model):
    image = models.ImageField(upload_to='events/images', height_field=None, width_field=None, max_length=None)
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='event_images')
    
class EventForm(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL,null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=11)
    reserved_count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

