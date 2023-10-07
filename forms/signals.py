from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.contrib.auth.models import User  # Import the User model if not already imported
from .models import Vacation  # Import the Vacation model from your app's models

@receiver(post_save, sender=Vacation)
def send_vacation_email(sender, instance, created, **kwargs):
    if created:
        # Define the email subject and message
        user = User.objects.get(id=instance.user_id)
        
        subject = "New Vacation Request"
        message = f"A new vacation request has been created.\nStart Time: {instance.start_time}\nEnd Time: {instance.end_time}"
        from_email = "merajbighamian@gmail.com"  # Replace with your email address
        employer_list = [user.employer.email]  # Replace with the recipient's email address

        # Send the email
        send_mail(subject, message, from_email, employer_list)
        
        emails_users = user.emails.all()
        for email_user in emails_users: 
          if email_user.email == employer_list[0]:   
            pass  
          else:
            subject_emails = "this is subject"
            email = email_user.email
            send_mail(subject_emails, "this is email", from_email, [email])
