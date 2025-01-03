from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.webauthn_register, name='webauthn_register'),
    path('register/complete/', views.webauthn_register_complete, name='webauthn_register_complete'),
    path('authenticate/', views.webauthn_authenticate, name='webauthn_authenticate'),
    path('authenticate/complete/', views.webauthn_authenticate_complete, name='webauthn_authenticate_complete'),
]