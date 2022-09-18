# Create Default category for a new user
# https://docs.djangoproject.com/en/4.1/topics/signals/

from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser
from categories.models import Category

@receiver(post_save, sender=CustomUser)
def my_handler(sender, instance, created, **kwargs):
    if created:
        cat = Category(name = 'Default', user = instance)
        cat.save()
