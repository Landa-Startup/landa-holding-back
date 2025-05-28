from .models import StartUpsForm,ContactUs,PartnerMembership,InvestorRegistration
from rest_framework import serializers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

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

    def create(self, validated_data):
        instance = super().create(validated_data)

        # Prepare email content
        subject = 'Thank you for registering as an investor'
        from_email = 'amir.esfahanizadeh@landaholding.com'
        to_email = instance.email
        context = {'first_name': instance.firstName}
        text_content = f"Hi {instance.firstName},\n\nThank you for registering as an investor. We appreciate your interest and will get back to you shortly.\n\nBest regards,\nThe Investment Platform Team"
        html_content = render_to_string('investor_registration_email.html', context)

        # Create and send email
        email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        email.attach_alternative(html_content, "text/html")
        email.send()

        return instance
    