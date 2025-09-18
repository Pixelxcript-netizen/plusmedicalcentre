from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from core.views import home
from medstaff.views import (
    admin_dashboard,
    frontdesk_dashboard,
    lab_dashboard,
    scan_dashboard,
    inventory_dashboard,
)

urlpatterns = [
    # Root page
    path('', home, name='home'),

    # Django admin
    path('admin/', admin.site.urls),

    # Auth-related
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path(
        'accounts/password_change/',
        auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
        name='password_change'
    ),
    path(
        'accounts/password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
        name='password_change_done'
    ),

    # Department dashboards
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('frontdesk-dashboard/', frontdesk_dashboard, name='frontdesk_dashboard'),
    path('lab-dashboard/', lab_dashboard, name='lab_dashboard'),
    path('scan-dashboard/', scan_dashboard, name='scan_dashboard'),
    path('inventory-dashboard/', inventory_dashboard, name='inventory_dashboard'),
]
