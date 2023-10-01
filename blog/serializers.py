from rest_framework.serializers import HyperlinkedModelSerializer,ModelSerializer
from .models import BlogPost

class BlogPostDetailsSerializers(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class BlogPostListSerializers(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"