from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email','first_name','last_name','code','id_number','phone_number','roles']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','code','id_number','phone_number', 'password']
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            id_number=validated_data['id_number'],
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            code=validated_data['code'],
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['role'] = user.roles.first().role
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['image'] = user.image
        
        # ...

        return token