from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.utils import timezone
from django.conf import settings
from .models import User
from . import utils
from django.contrib.auth.decorators import login_required


def login_user_in(request, username):
    user=User.objects.get(username=username)
    user.backend='django.contrib.auth.backends.ModelBackend'
    auth.login(request, user)
    if "redirect" in request.POST:
        return redirect(request.POST["redirect"])
    else:
        return redirect(reverse('accounts:index'))

def login(request):
    if request.method == "POST":
        ref_num = request.POST.get('ref-num')
        user = User.objects.filter(ref_num=ref_num).first()
        if user is not None:
            username = user.username
            if user.is_active:
                if "mfa" in settings.INSTALLED_APPS:
                    from mfa.helpers import has_mfa
                    res =  has_mfa(request,username=username)
                    if res: return res
                    return login_user_in(request, username)
            else:
                err="This student is NOT activated yet."
        else:
            registered = 'false'
            return render(request, 'login.html', {"registered": registered})
  
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        ref_num = request.POST.get("ref-num")
        first_name = request.POST.get("first-name")
        middle_name = request.POST.get("middle-name")
        last_name = request.POST.get("last-name")
        suffix = request.POST.get("suffix")
        email = request.POST.get("username")
        contact_number = request.POST.get("contact-number")
        birthdate = request.POST.get("birthdate")
        sex = request.POST.get("sex")
        address = request.POST.get("address")
        guardian = request.POST.get("guardian")
        parent = request.POST.get("parent")
        work_status = request.POST.get("work-status")
        # if not utils.validate_username(username):
        #    error = 'Invalid matriculation number'
        #    return render(request, 'register.html', context = {'page_title': "Register", 'error': error})
        # if not utils.validate_display_name(display_name):
        #    error = 'Invalid display name'
        #    return render(request, 'register.html', context = {'page_title': "Register", 'error': error})
        # if User.objects.filter(username=username).exists():
        #     error = 'Student already exists.'
        #     return render(request, 'register.html', context = {'page_title': "Register", 'error': error})
        # else:
        #     u = User.objects.create(first_name = display_name, password='none', is_superuser=False, username=username,  last_name='', display_name=display_name, email='none', is_staff=False, is_active=True,date_joined=timezone.now())
        #     u.backend = 'django.contrib.auth.backends.ModelBackend'
        #     auth.login(request,u)
        #     return redirect(reverse('start_fido2'))
        
        u = User.objects.create(
                    username = email,
                    ref_num=ref_num,
                    first_name=first_name,
                    last_name=last_name,
                    mname=middle_name,
                    suffix=suffix,
                    email=email,
                    contact_num=contact_number, 
                    birthdate=birthdate, 
                    sex=sex, 
                    address=address,
                    guardian=guardian, 
                    parent=parent,
                    work_status=work_status
                )
        u.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request,u)
        return redirect(reverse('start_fido2'))
    
    return render(request, 'register.html')

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html', {"page_title": "Welcome home"})