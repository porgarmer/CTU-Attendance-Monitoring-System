from django.shortcuts import render
from .models import User
# Create your views here.
def user_profile(request, ref_num=None):
    user = User.objects.filter(ref_num = ref_num).first()
    
    return render(request, "user_profile.html", {
        "user": user,
    })