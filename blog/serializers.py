from rest_framework.serializers import HyperlinkedModelSerializer,ModelSerializer
from .models import BlogPost,Category,Tag

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)

class TagSerializers(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)
        

class BlogPostDetailsSerializers(ModelSerializer):
    tags = TagSerializers(many=True,read_only=True)   
    categories = CategorySerializers(many=True,read_only=True)

    class Meta:
        model = BlogPost
        fields = "__all__"
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class BlogPostListSerializers(ModelSerializer):
    tags = TagSerializers(many=True,read_only=True) 
    categories = CategorySerializers(many=True,read_only=True)  
    class Meta:
        model = BlogPost
        fields = "__all__"