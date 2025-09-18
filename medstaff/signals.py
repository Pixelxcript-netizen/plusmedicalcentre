from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name == 'medstaff':
        default_groups = ['Admin', 'Frontdesk', 'Lab', 'Scan', 'Inventory']
        for group_name in default_groups:
            Group.objects.get_or_create(name=group_name)
