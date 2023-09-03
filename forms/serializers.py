from .models import StartUpsForm,ContactUs,PartnerMembership,InvestorRegistration
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
    