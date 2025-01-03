from django.urls import path
from . import views
urlpatterns = [
    path("", views.regiser, name="register")
]
