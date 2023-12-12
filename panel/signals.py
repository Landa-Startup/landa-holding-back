import os
import jdatetime
import datetime
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models.signals import post_save, pre_save
from .models import Vacation  # Import the Vacation model from your app's models
from accounts.models import User


# IMPORTANT


def gregorian_to_jalali(gregorian_datetime_string: str):
    # gregorian_datetime_string = "2023-11-3T03:10:10+03:30"
    gregorian_datetime_string = str(
        gregorian_datetime_string).replace(' ', 'T')

    # Parse the Gregorian datetime string
    gregorian_datetime = datetime.datetime.fromisoformat(
        gregorian_datetime_string)

    # Convert the Gregorian datetime to Jalali
    jalali_datetime = jdatetime.datetime.fromgregorian(day=gregorian_datetime.day, month=gregorian_datetime.month,
                                                       year=gregorian_datetime.year,
                                                       hour=gregorian_datetime.hour, minute=gregorian_datetime.minute,
                                                       second=gregorian_datetime.second)

    return jalali_datetime


def convert_gmt_to_theran_timezone(time: str):
    dt = datetime.datetime.fromisoformat(time)

    duration = datetime.timedelta(hours=3, minutes=30)
    result = dt + duration
    return str(result)


@receiver(post_save, sender=Vacation)
def send_vacation_email(sender, instance, created, **kwargs):
    if created:
        # Define the email subject and message
        user = User.objects.get(id=instance.user_id)

        template_path = os.path.join(
            settings.BASE_DIR, 'templates', 'panel', 'email_template.html')

        # Sending context for email template
        context = {
            "recipient_name": (user.first_name.capitalize() + ' ' + user.last_name.capitalize()),
            "start_time": str(gregorian_to_jalali(instance.start_time)),
            "end_time": str(gregorian_to_jalali(instance.end_time)),
        }

        # Render the email template with the provided context
        email_content = render_to_string(template_path, context)

        # Create a plain text version of the email content (strip HTML tags)
        plain_message = strip_tags(email_content)

        subject = f"New Vacation Request From {user.first_name} {user.last_name}"
        from_email = "info@landaholding.com"  # Replace with your email address
        # Replace with the recipient's email address
        employer_list = [user.employer.email]

        send_mail(
            subject,
            plain_message,
            from_email,
            employer_list,
            html_message=email_content,  # Specify the HTML content here.
        )


# a reciver for update model signal
@receiver(pre_save, sender=Vacation)
def update_description(sender, instance, **kwargs):
    user = User.objects.get(id=instance.user_id)

    # check status
    status_message = ""
    if instance.status == 2:
        status_message = 'Approved'
    elif instance.status == 3:
        status_message = 'Declined'
    elif instance.status == 1:
        status_message = 'Pending'

    # Load the HTML template
    # email_template = ''
    template_path = os.path.join(
        settings.BASE_DIR, 'templates', 'panel', 'email_template_for_emails.html')
    # with open(template_path, 'r') as template_file:
    #     email_template = template_file.read()
    # Replace placeholders in the HTML template
    context = {
        "recipient_name": user.first_name.capitalize() + ' ' + user.last_name.capitalize(),
        "start_time": convert_gmt_to_theran_timezone(str(gregorian_to_jalali(instance.start_time))),
        "end_time": convert_gmt_to_theran_timezone(str(gregorian_to_jalali(instance.end_time))),
        "status": status_message
    }

    email_content = render_to_string(template_path, context)
    plain_message = strip_tags(email_content)
    # email_content = email_template.replace(
    #     '{{ recipient_name }}', (user.first_name.capitalize() + ' '+user.last_name.capitalize()), -2)
    # email_content = email_content.replace('{{start_time}}', convert_gmt_to_theran_timezone(
    #     str(gregorian_to_jalali(instance.start_time))))
    # email_content = email_content.replace('{{end_time}}', convert_gmt_to_theran_timezone(
    #     str(gregorian_to_jalali(instance.end_time))))
    # email_content = email_content.replace('{{status}}', status_message)

    email_me = user.email

    employer_list = [user.employer.email]
    from_email = "info@landaholding.com"  # Replace with your email address
    emails_users = user.emails.all()

    if instance.status != 1:
        if instance.status == 2:
            for email_user in emails_users:
                if email_user.email == employer_list[0]:
                    pass
                else:
                    subject = f"Vacation Request of {user.first_name} {user.last_name} Has Been Approved"
                    send_mail(
                        subject,
                        # Leave the message argument empty since we have HTML content.
                        plain_message,
                        from_email,
                        [email_user.email],
                        fail_silently=False,
                        # Specify the HTML content here.
                        html_message=email_content,
                    )

            send_mail(f"Your Vacation Request Has Been {status_message}",
                      f"Your Vacation Request is {status_message}", from_email, [email_me])
        elif instance.status == 3:
            send_mail(f"Your Vacation Request Has Been {status_message}",
                      f"Your Vacation Request is {status_message}", from_email, [email_me])
