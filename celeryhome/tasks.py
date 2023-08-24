from celery import shared_task

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Client

from django.core.mail import send_mail

  
# @shared_task(bind=True)
# def add(self,x,y):
#     return x + y


# @shared_task
# def send_email(recipient_list, subject, message):
#     send_mail(subject, message, 'danish@snakescript.com', recipient_list)


@shared_task
def send_email_to_users():
    # Fetch the users from your model
    users = Client.objects.all()

    # Send email to each user
    for user in users:
        subject = "Your Subject"
        message = "Your Message"
        from_email = 'danish@snakescript.com'
        to_email = [user.email]  # Use the email field from your User model
        send_mail(subject, message, from_email, to_email)