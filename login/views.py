from django.shortcuts import render, redirect
from django.http import HttpResponse
from user_profile.models import User
from django.conf import settings
from django.urls import reverse
from django.contrib import auth

# Create your views here.



def login_user_in(request, ref_num):
    user=User.objects.get(ref_num=ref_num)
    user.backend='django.contrib.auth.backends.ModelBackend'
    auth.login(request, user)
    if "redirect" in request.POST:
        return redirect(request.POST["redirect"])
    else:
        return redirect(reverse('user-profile:user-profile', kwargs={'ref_num': ref_num}))
    
def login(request):
    if request.method == "POST":
        ref_num = request.POST.get('ref-num')
        user = User.objects.filter(ref_num=ref_num).first()

        if user is not None:
            if user.is_active:
                if "mfa" in settings.INSTALLED_APPS:
                    from mfa.helpers import has_mfa
                    res =  has_mfa(request,username=ref_num)
                    if res: return res
                    return login_user_in(request, ref_num)
            else:
                err="This student is NOT activated yet."
        else:
            err="No student with such matriculation number exists."
        return render(request, 'login.html', {"err":err})
    else:
        return render(request, 'login.html')
