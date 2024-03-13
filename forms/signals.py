from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
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
@receiver(post_save, sender=ApplyJob)
@receiver(post_save, sender=Handicraft)
@receiver(post_save, sender=LandaGene)
@receiver(post_save, sender=WorkWithUs)
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


@receiver(post_save, sender=ApplyJob)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
        # send sms
        phone = instance.phoneNumber.replace('0', '98', 1)

        message_id = sms.send_pattern(
            pattern_code="otu9jfznbjgnsej",  # pattern code
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
