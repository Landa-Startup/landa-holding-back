
from rest_framework import serializers
from accounts.serializers import UserSerializer

from panel.models import Vacation

class VacationGetAllFormSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model= Vacation
        fields = '__all__'
        read_only_fields = ['id','status']

class VacationSerializers(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Vacation
        fields = '__all__'
    
class CreateVacationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = '__all__'