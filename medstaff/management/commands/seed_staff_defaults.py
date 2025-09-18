import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from medstaff.models import StaffProfile
from decouple import config
from django.db import transaction

class Command(BaseCommand):
    help = "Seed default staff users for each department role using .env passwords"

    @transaction.atomic
    def handle(self, *args, **options):
        # Roles mapped to their password env vars
        roles = {
            'Admin': config('DEFAULT_ADMIN_PASSWORD'),
            'Frontdesk': config('DEFAULT_FRONTDESK_PASSWORD'),
            'Lab': config('DEFAULT_LAB_PASSWORD'),
            'Scan': config('DEFAULT_SCAN_PASSWORD'),
            'Inventory': config('DEFAULT_INVENTORY_PASSWORD'),
        }

        for role, password in roles.items():
            # Ensure the group exists
            group, _ = Group.objects.get_or_create(name=role)
            username = role.lower()

            if not User.objects.filter(username=username).exists():
                # Create the user
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    is_active=True
                )
                user.groups.add(group)
                StaffProfile.objects.create(
                    user=user,
                    must_change_password=True
                )
                self.stdout.write(self.style.SUCCESS(f"✅ Created {role} user ({username})"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ {role} user already exists"))
