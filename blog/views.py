from .serializers import BlogPostDetailsSerializers,BlogPostListSerializers,CategorySerializers,TagSerializers
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import BlogPost,Tag,Category
# Create your views here.

class BlogList(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostListSerializers
    
class BlogDeatialsView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailsSerializers
    lookup_field = 'slug'

class TagsView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers

class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers