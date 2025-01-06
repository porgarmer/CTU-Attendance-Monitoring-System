from django.urls import path
from . import views

app_name = 'user-profile'
urlpatterns = [
    path("<int:ref_num>", views.user_profile, name="user-profile")
]
