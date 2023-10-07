from .models import Vacation
from django.db import models
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(models.signals.post_save, sender=Vacation)
def send_vacation_email(sender, instance, created, **kwargs):
    if created:
        # Define the email subject and message
        print(instance.user_id)
        subject = "New Vacation Request"
        message = f"A new vacation request has been created.\nStart Time: {instance.start_time}\nEnd Time: {instance.end_time}"
        from_email = "your@email.com"  # Replace with your email address
        recipient_list = ["recipient@email.com"]  # Replace with the recipient's email address

        # Send the email
        send_mail(subject, message, from_email, recipient_list)
