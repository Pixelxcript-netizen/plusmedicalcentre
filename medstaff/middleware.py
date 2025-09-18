from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.conf import settings

from django.contrib.auth import get_user_model

User = get_user_model()

DEFAULT_PASSWORDS = [
    settings.DEFAULT_ADMIN_PASSWORD,
    settings.DEFAULT_FRONTDESK_PASSWORD,
    settings.DEFAULT_LAB_PASSWORD,
    settings.DEFAULT_SCAN_PASSWORD,
    settings.DEFAULT_INVENTORY_PASSWORD,
]


class MustChangePasswordMiddleware:
    """
    Forces users to change their password if they are still using the default one.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Only check for non-admin pages and non-password-change pages
            if (
                not request.path.startswith(reverse('password_change')) and
                not request.user.is_superuser
            ):
                for default in DEFAULT_PASSWORDS:
                    if check_password(default, request.user.password):
                        return redirect('password_change')  # send them to change it

        return self.get_response(request)
