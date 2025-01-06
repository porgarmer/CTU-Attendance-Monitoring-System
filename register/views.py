from django.shortcuts import render, redirect
from django.contrib import messages
from user_profile.models import User
from django.db import IntegrityError
from django.contrib import auth


# Create your views here.
def regiser(request):
    
    if request.method == "POST":
        ref_num = request.POST.get("ref-num")
        first_name = request.POST.get("first-name")
        middle_name = request.POST.get("middle-name")
        last_name = request.POST.get("last-name")
        suffix = request.POST.get("suffix")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact-number")
        birthdate = request.POST.get("birthdate")
        sex = request.POST.get("sex")
        address = request.POST.get("address")
        guardian = request.POST.get("guardian")
        parent = request.POST.get("parent")
        work_status = request.POST.get("work-status")
        
        existing_ref_num = User.objects.filter(ref_num = ref_num)
        if existing_ref_num:
            messages.error(request, "Reference number already exists")
            return render(request, "register.html")
        try:
                # Attempt to create the user
                user = User.objects.create(
                    ref_num=ref_num,
                    fname=first_name,
                    lname=last_name,
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
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                auth.login(request, user)
                # user.save()
                # messages.success(request, "You have successfully registered!")
                return render(redirect('start_fido2'))
        except Exception:
            messages.warning(request, "Something went wrong")
    return render(request, "register.html")