from rest_framework import serializers
from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email','first_name','last_name','code','id_number','phone_number','roles']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','first_name','last_name','code','id_number','phone_number', 'password']
    def create(self, validated_data):
        user = CustomUser(
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
    