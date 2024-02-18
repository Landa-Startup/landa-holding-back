from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField('عنوان', max_length=300)
    description = RichTextField(verbose_name='توضیحات')
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='blog/images')
    updated_at = models.DateTimeField('به روز شده در', auto_now=True)
    created_at = models.DateTimeField('ساخته شده در', auto_now_add=True)
    author = models.CharField('نویسنده', max_length=150, default='admin')
    categories = models.ManyToManyField("Category", verbose_name="دسته بندی ها",related_name="category_course",blank=True,null=True)
    tags = models.ManyToManyField("Tag", verbose_name="Tags",blank=True,null=True)

class Tag(models.Model):
    title = models.CharField('tag name',max_length=250)

class Category(models.Model):
    title = models.CharField('category name',max_length=250)
    