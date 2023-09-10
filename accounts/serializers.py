from rest_framework import serializers
from .models import CustomUser,EmployeAndEmployer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email','first_name','last_name','code','id_number','phone_number']

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
    
class EmployeAndEmployer(serializers.ModelSerializer):
    employer = serializers.SerializerMethodField(read_only=True)
    employe = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = EmployeAndEmployer
        fields={
            'employe',
            'employer'
        }
    def get_employer(self,obj):
        return{
            "employe" : obj.employe.email
        }