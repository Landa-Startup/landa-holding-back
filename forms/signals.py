from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save,pre_save
from .models import Vacation,User  # Import the Vacation model from your app's models

@receiver(post_save, sender=Vacation)
def send_vacation_email(sender, instance, created, **kwargs):
    if created:
        # Define the email subject and message
        user = User.objects.get(id=instance.user_id)

          
        subject = "New Vacation Request"
        message = f"A new vacation request has been created.\nStart Time: {instance.start_time}\nEnd Time: {instance.end_time} <html><a href='127.0.0.1:8000/approve/{instance.uuid}'>Approve</a><a href='127.0.0.1:8000/decline/{instance.uuid}'>Decline</a></html>"
        from_email = "merajbighamian@gmail.com"  # Replace with your email address
        employer_list = [user.employer.email]  # Replace with the recipient's email address

        # Send the email
        send_mail(subject, message, from_email, employer_list)


# a reciver for update model signal
@receiver(pre_save, sender=Vacation)
def update_description(sender, instance, **kwargs):
    # Here, you can define the logic to update the 'description' field.
    # For example, you can set it to a modified version of 'name'.
      user = User.objects.get(id=instance.user_id)
      email_me = user.email
      
      employer_list = [user.employer.email] 
      from_email = "merajbighamian@gmail.com"  # Replace with your email address
      emails_users = user.emails.all()
      
      status_message =""
      if instance.status == 2:
        status_message = 'Approve'
      elif instance.status == 3:
        status_message = 'Decline'
      
      if instance.status != 1:
        if instance.status == 2:
          for email_user in emails_users: 
            if email_user.email == employer_list[0]:   
              pass  
            else:
              subject_emails = "this is subject"
              email = email_user.email
              send_mail(subject_emails, f"{user.first_name} {user.last_name} vacation form is {status_message}", from_email, [email])
        elif instance.status ==2 or instance.status ==3:
          send_mail("this is subject", f"your vacation form is {status_message}", from_email, [user.email])
        