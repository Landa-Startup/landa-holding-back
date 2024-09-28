from django import forms
from django.contrib import admin
from .models import BlogPost,Tag,Category
from ckeditor.widgets import CKEditorWidget

class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag)
admin.site.register(Category)