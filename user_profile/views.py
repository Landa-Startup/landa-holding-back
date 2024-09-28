from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .serializers import ProfileSerializer
from .models import Profile
# Create your views here.

class ProfileDetailsView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    extra_kwargs = {
        'url': {'lookup_field': 'username'},
    }