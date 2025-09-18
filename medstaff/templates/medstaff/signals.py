from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, created, **kwargs):
    if created:
        print(f"✨ A new user has been created: {instance.username}")
    else:
        print(f"⚡ User updated: {instance.username}")
