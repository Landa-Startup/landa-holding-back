from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    description = RichTextField()
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='blog/images')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=150,default='admin')
    categories = models.ManyToManyField("Category", verbose_name="Categories",related_name="category_course",blank=True,null=True)
    tags = models.ManyToManyField("Tag", verbose_name="Tags",blank=True,null=True)

class Tag(models.Model):
    title = models.CharField('tag name',max_length=250)

class Category(models.Model):
    title = models.CharField('category name',max_length=250)
    