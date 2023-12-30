import os
import jdatetime
from datetime import datetime
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save, pre_save
# Import the Vacation model from your app's models
from .models import StartUpsForm, ContactUs, PartnerMembership, InvestorRegistration, Entrepreuneur, ApplyJob, \
    Handicraft, LandaGene


@receiver(post_save, sender=StartUpsForm)
@receiver(post_save, sender=ContactUs)
@receiver(post_save, sender=Entrepreuneur)
@receiver(post_save, sender=PartnerMembership)
@receiver(post_save, sender=InvestorRegistration)
@receiver(post_save, sender=ApplyJob)
@receiver(post_save, sender=Handicraft)
@receiver(post_save, sender=LandaGene)
def send_create_form_email(sender, instance, created, **kwargs):
    if created:
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

# # a reciver for update model signal
# @receiver(pre_save, sender=Vacation)
# def update_description(sender, instance, **kwargs):
#     # Here, you can define the logic to update the 'description' field.
#     # For example, you can set it to a modified version of 'name'.
#       user = User.objects.get(id=instance.user_id)
#               # Define the email subject and message

#       #check status
#       status_message =""
#       if instance.status == 2:
#         status_message = 'Approved'
#       elif instance.status == 3:
#         status_message = 'Declined'
#       elif instance.status == 1:
#         status_message = 'Pending'

#       # Load the HTML template
#       email_template = ''
#       template_path = os.path.join(settings.BASE_DIR, 'templates', 'panel', 'email_template_for_emails.html')
#       with open(template_path, 'r') as template_file:
#           email_template = template_file.read()
#       # Replace placeholders in the HTML template
#       email_content = email_template.replace('{{ recipient_name }}', (user.first_name.capitalize() +' '+user.last_name.capitalize()),-2)
#       # email_content = email_template.replace('{{ user_name }}', (user.first_name.capitalize() +' '+user.last_name.capitalize()))
#       email_content = email_content.replace('{{start_time}}',str(gregorian_to_jalali(instance.start_time)))
#       email_content = email_content.replace('{{end_time}}',str(gregorian_to_jalali(instance.end_time)))
#       email_content = email_content.replace('{{status}}',status_message)

#       email_me = user.email

#       employer_list = [user.employer.email]
#       from_email = "info@landaholding.com"  # Replace with your email address
#       emails_users = user.emails.all()


#       if instance.status != 1:
#         if instance.status == 2:
#           for email_user in emails_users:
#             if email_user.email == employer_list[0]:
#               pass
#             else:
#               subject = f"New Vacation Request From {user.first_name} {user.last_name}"
#               send_mail(
#                 subject,
#                 '',  # Leave the message argument empty since we have HTML content.
#                 from_email,
#                 employer_list,
#                 fail_silently=False,
#                 html_message=email_content,  # Specify the HTML content here.
#               )
#           send_mail(f"Your Vacation Request Has Been {status_message}", f"Your Vacation Request is {status_message}", from_email, [email_me])
#         elif instance.status ==3:
#           send_mail(f"Your Vacation Request Has Been {status_message}", f"Your Vacation Request is {status_message}", from_email, [email_me])
