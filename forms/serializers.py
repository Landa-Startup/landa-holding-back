from .models import StartUpsForm,ContactUs,PartnerMembership,InvestorRegistration,Entrepreuneur,ApplyJob ,\
    Handicraft, LandaGene, WorkWithUs
from rest_framework import serializers
class StartupFormSerializer(serializers.ModelSerializer):
    financialModelFile = serializers.FileField(required=False)
    financialFile = serializers.FileField(required=False)
    pitchDeckFile = serializers.FileField(required=False)
    businessPlanFile = serializers.FileField(required=False)
    class Meta:
        model = StartUpsForm
        fields = '__all__'
        read_only_fields = ['id','createdAt']
    
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
        read_only_fields = ['id','createdAt']

class PartnerMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerMembership
        fields = '__all__'
        read_only_fields = ['id','createdAt']
    
class InvestorRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorRegistration
        fields = '__all__'
        read_only_fields = ['id','createdAt']

class EntrepreuneurSerializer(serializers.ModelSerializer):
    class Meta:
        model= Entrepreuneur
        fields = '__all__'
        read_only_fields = ['id','createdAt']

class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model= ApplyJob
        fields = '__all__'
        read_only_fields = ['id','createdAt']

class HandicraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handicraft
        fields = '__all__'
        read_only_fields = ['id', 'created_at']


class LandaGeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandaGene
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

class WorkWithUsSerializers(serializers.ModelSerializer):
    cv_file = serializers.FileField(required=False)
    
    class Meta:
        model = WorkWithUs
        fields = '__all__'
        read_only_fields = ['id', 'created_at']