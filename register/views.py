from django.shortcuts import render, redirect
from django.contrib import messages
from user_profile.models import User
from django.db import IntegrityError

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
        
        existing_ref_num = User.objects.get(user_ref_num = ref_num)
        if existing_ref_num:
            messages.error(request, "Reference number already exists")
            return render(request, "register.html")
        try:
                # Attempt to create the user
                user = User.objects.create(
                    user_ref_num=ref_num,
                    user_fname=first_name,
                    user_lname=last_name,
                    user_mname=middle_name,
                    user_suffix=suffix,
                    user_email=email,
                    user_contact_num=contact_number, 
                    user_birthdate=birthdate, 
                    user_sex=sex, 
                    user_address=address,
                    user_guardian=guardian, 
                    user_parent=parent,
                    user_work_status=work_status 
                )
                
                user.save()
                messages.success(request, "You have successfully registered!")
                return render(request, "register.html")
        except Exception:
                messages.warning(request, "Something went wrong")
        
    return render(request, "register.html")