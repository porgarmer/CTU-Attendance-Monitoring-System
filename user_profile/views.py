from django.shortcuts import render
from .models import User
# Create your views here.
def user_profile(request, ref_num=None):
    ref_num = 1234
    user = User.objects.get(user_ref_num = ref_num)
    user_minitial = user.user_mname[0] + "."
    return render(request, "user_profile.html", {
        "user": user,
        "user_minitial": user_minitial
    })