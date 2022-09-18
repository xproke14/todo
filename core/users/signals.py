from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from .tasks import send_welcome_email


@receiver(post_save, sender=CustomUser)
def send_email(sender, instance, created, **kwargs):
    if created:
        #send_welcome_email.delay(instance.email)
        pass

