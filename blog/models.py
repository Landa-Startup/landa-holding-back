from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='blog/images')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=150,default='admin')