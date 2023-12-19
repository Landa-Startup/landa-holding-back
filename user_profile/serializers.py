from rest_framework import serializers
from .models import Profile,Website

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = "__all__"
        read_only_fields = ['id']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ['id']
        
    websites = WebsiteSerializer(many=True,read_only=True)
