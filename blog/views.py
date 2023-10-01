from .serializers import BlogPostDetailsSerializers,BlogPostListSerializers
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import BlogPost
# Create your views here.

class BlogList(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostListSerializers
    
class BlogDeatialsView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailsSerializers
    lookup_field = 'slug'
