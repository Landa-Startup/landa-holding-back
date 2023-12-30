import os
import jdatetime
from datetime import datetime
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from ippanel import Client
# Import the Vacation model from your app's models
from .models import StartUpsForm, ContactUs, PartnerMembership, InvestorRegistration, Entrepreuneur, ApplyJob, LandaGene

@receiver(post_save, sender=StartUpsForm)
@receiver(post_save, sender=ContactUs)
@receiver(post_save, sender=Entrepreuneur)
@receiver(post_save, sender=PartnerMembership)
@receiver(post_save, sender=InvestorRegistration)
@receiver(post_save, sender=ApplyJob)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        # send email
        # Define the email subject and message
        user_email = instance.email
        user_list_email = [user_email]
        from_email = "relation@landaholding.com"  # Replace with your email address
        # Replace with the recipient's email address
        company_emails_list = ["relation@landaholding.com"]

        send_mail(
            f"New filled form from {user_email}",
            f'We have a new filled form from {user_email}',
            from_email,
            company_emails_list,
            fail_silently=False,
            # html_message=email_content,  # Specify the HTML content here.
        )
        send_mail(
            "Greetings and welcome to the Landa family",
            """Greetings and welcome to the Landa family
Gratitude for your astute selection Our primary objective at Landa International Holding is to deliver optimal services and ensure your satisfaction.
""", 
            from_email,
            user_list_email,
            fail_silently=False,
            # html_message=email_content,  # Specify the HTML content here.
        )


key = "zYkFTImZ4E1uLfEh4jF1KvqNbsesulNgIemi_nOzRTI="
sms = Client(key)
message = "Greetings and welcome to the Landa family Gratitude for your astute selection Our primary objective at Landa International Holding is to deliver optimal services and ensure your satisfaction."
fnumber = "+983000505"

@receiver(post_save,sender=ContactUs)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        #send sms
        phone = instance.number.replace('0','+98',1)
        pattern_values = {
            "name": f"{instance.name}",
        }

        message_id = sms.send_pattern(
            "4x101dyk22ovhs9",    # pattern code
            fnumber,      # originator
            phone,  # recipient
            pattern_values,  # pattern values
        )
    
@receiver(post_save,sender=Entrepreuneur)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        #send sms
        phone = instance.phone.replace('0','+98',1)
        pattern_values = {
            "name": f"{instance.companyName}",
        }

        message_id = sms.send_pattern(
            "4x101dyk22ovhs9",    # pattern code
            fnumber,      # originator
            phone,  # recipient
            pattern_values,  # pattern values
        )    
@receiver(post_save,sender=ApplyJob)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        #send sms
        phone = instance.phoneNumber.replace('0','+98',1)
        pattern_values = {
            "name": f"{instance.firstName} {instance.lastName}",
        }

        message_id = sms.send_pattern(
            "4x101dyk22ovhs9",    # pattern code
            fnumber,      # originator
            phone,  # recipient
            pattern_values,  # pattern values
        )
@receiver(post_save,sender=LandaGene)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        #send sms
        phone = instance.phone_number.replace('0','+98',1)
        pattern_values = {
            "name": f"{instance.full_name}",
        }

        message_id = sms.send_pattern(
            "4x101dyk22ovhs9",    # pattern code
            fnumber,      # originator
            phone,  # recipient
            pattern_values,  # pattern values
        )   