from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


@shared_task
def send_welcome_email(email_address):
    email_subject = "Welcome to ToDo app!"
    context = {'email':email_address}
    email_body = render_to_string('email_template.txt', context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [email_address,]
    )
    email.send()