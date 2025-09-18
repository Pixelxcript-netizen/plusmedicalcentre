from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class RoleBasedLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name='Admin').exists():
            return '/admin-dashboard/'
        elif user.groups.filter(name='Frontdesk').exists():
            return '/frontdesk-dashboard/'
        elif user.groups.filter(name='Lab').exists():
            return '/lab-dashboard/'
        elif user.groups.filter(name='Scan').exists():
            return '/scan-dashboard/'
        elif user.groups.filter(name='Inventory').exists():
            return '/inventory-dashboard/'
        else:
            return '/'  # fallback

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def admin_dashboard(request):
    return render(request, 'medstaff/admin_dashboard.html')

@login_required
def frontdesk_dashboard(request):
    return render(request, 'medstaff/frontdesk_dashboard.html')

@login_required
def lab_dashboard(request):
    return render(request, 'medstaff/lab_dashboard.html')

@login_required
def scan_dashboard(request):
    return render(request, 'medstaff/scan_dashboard.html')

@login_required
def inventory_dashboard(request):
    return render(request, 'medstaff/inventory_dashboard.html')


from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages

def role_based_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Send them to their dashboard based on group
            if user.groups.filter(name='Admin').exists():
                return redirect('admin_dashboard')
            elif user.groups.filter(name='Frontdesk').exists():
                return redirect('frontdesk_dashboard')
            elif user.groups.filter(name='Lab').exists():
                return redirect('lab_dashboard')
            elif user.groups.filter(name='Scan').exists():
                return redirect('scan_dashboard')
            elif user.groups.filter(name='Inventory').exists():
                return redirect('inventory_dashboard')
            else:
                messages.error(request, "User has no assigned group.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")
