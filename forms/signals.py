import os

from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models.signals import post_save
from ippanel import Client
# Import the Vacation model from your app's models
from .models import StartUpsForm, ContactUs, PartnerMembership, InvestorRegistration, Entrepreuneur, ApplyJob, \
    Handicraft, LandaGene, WorkWithUs


@receiver(post_save, sender=StartUpsForm)
@receiver(post_save, sender=ContactUs)
@receiver(post_save, sender=Entrepreuneur)
@receiver(post_save, sender=PartnerMembership)
@receiver(post_save, sender=InvestorRegistration)
@receiver(post_save, sender=Handicraft)
@receiver(post_save, sender=LandaGene)
@receiver(post_save, sender=WorkWithUs)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        template_path = os.path.join(
            settings.BASE_DIR, 'templates', 'panel', 'welcome_email_template.html')

        template = render_to_string(template_path)
        # send email
        # Define the email subject and message
        form_name = str(instance).split(' ')[0]
        user_email = instance.email
        user_phone = ''
        user_full_name = ''

        try:
            user_phone = instance.phoneNumber
        except AttributeError:
            try:
                user_phone = instance.phone
            except AttributeError:
                try:
                    user_phone = instance.phone_number
                except AttributeError:
                    pass

        try:
            user_full_name = f"{instance.firstName} {instance.lastName}"
        except AttributeError:
            try:
                user_full_name = f"{instance.first_name} {instance.last_name}"
            except AttributeError:
                try:
                    user_full_name = instance.full_name
                except AttributeError:
                    pass

        user_list_email = [user_email]
        from_email = "relation@landaholding.com"  # Replace with your email address
        # Replace with the recipient's email address
        company_emails_list = ["relation@landaholding.com" , "office@irimmigration.ca"]

        send_mail(
            f"New filled {form_name} from {user_email}",
            f'We have a new filled form with\nemail: {user_email}, phone: {user_phone}, name: {user_full_name}',
            from_email,
            company_emails_list,
            fail_silently=False,
            # html_message=email_content,  # Specify the HTML content here.
        )
        send_mail(
            "Greetings and welcome to the Landa family",
            template,
            from_email,
            user_list_email,
            fail_silently=False,
            html_message=template,   # Specify the HTML content here.
        )


@receiver(post_save, sender=ApplyJob)
def send_apply_job_email(sender, instance, created, **kwargs):
    if created:
        template_path = os.path.join(
            settings.BASE_DIR, 'templates', 'panel', 'email_workwithus_template.html')

        template = render_to_string(template_path)

        # send email
        # Define the email subject and message
        user_email = instance.email
        user_phone = instance.phoneNumber
        user_full_name = instance.firstName + instance.lastName
        user_list_email = [user_email]
        from_email = "relation@landaholding.com"  # Replace with your email address
        # Replace with the recipient's email address
        company_emails_list = ["relation@landaholding.com" , "office@irimmigration.ca"]

        send_mail(
            f"New filled Work With Us form from {user_email}",
            f'We have a new Work With Us form with \nemail: {user_email}, phone: {user_phone}, name: {user_full_name}',
            from_email,
            company_emails_list,
            fail_silently=False,
            # html_message=email_content,  # Specify the HTML content here.
        )
        send_mail(
            "Work With Us",
            template,
            from_email,
            user_list_email,
            fail_silently=False,
            html_message=template,  # Specify the HTML content here.
        )


key = "zYkFTImZ4E1uLfEh4jF1KvqNbsesulNgIemi_nOzRTI="
sms = Client(key)
# message = "به خانواده بزرگ هلدینگ لاندا خوش آمدید! ضمن قدردانی از حسن انتخاب شما در صورت تمایل با شماره 09120539563 با ما در ارتباط باشید"
fnumber = "983000505"


@receiver(post_save, sender=ContactUs)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        # send sms
        phone = instance.number.replace('0', '98', 1)

        message_id = sms.send_pattern(
            pattern_code="otu9jfznbjgnsej",  # pattern code
            sender=fnumber,  # originator
            recipient=phone,  # recipient
        )


@receiver(post_save, sender=Entrepreuneur)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        # send sms
        phone = instance.phone.replace('0', '98', 1)

        message_id = sms.send_pattern(
            pattern_code="otu9jfznbjgnsej",  # pattern code
            sender=fnumber,  # originator
            recipient=phone,  # recipient
        )


@receiver(post_save, sender=InvestorRegistration)
@receiver(post_save, sender=PartnerMembership)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        # send sms
        phone = instance.phoneNumber.replace('0', '98', 1)

        message_id = sms.send_pattern(
            pattern_code="otu9jfznbjgnsej",  # pattern code
            sender=fnumber,  # originator
            recipient=phone,  # recipient
        )


@receiver(post_save, sender=ApplyJob)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        # send sms
        phone = instance.phoneNumber.replace('0', '98', 1)

        message_id = sms.send_pattern(
            pattern_code="ojdm8oeg4w1recs",  # pattern code
            sender=fnumber,  # originator
            recipient=phone,  # recipient
        )


@receiver(post_save, sender=LandaGene)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        # send sms
        phone = instance.phone_number.replace('0', '+98', 1)

        message_id = sms.send_pattern(
            pattern_code="otu9jfznbjgnsej",  # pattern code
            sender=fnumber,  # originator
            recipient=phone,  # recipient
        )
