from django.db import models

# Create your models here.
class User(models.Model):
    user_ref_num = models.CharField(max_length=255, primary_key=True)
    user_fname = models.CharField(max_length=50)
    user_lname = models.CharField(max_length=50)
    user_mname = models.CharField(max_length=50, null=True)
    user_suffix=models.CharField(max_length=25, null=True)
    user_email = models.EmailField(max_length=100, null=True)
    user_contact_num = models.CharField(max_length=20, null=True)
    user_birthdate = models.DateField(auto_now_add=False, auto_now=False)
    user_sex = models.CharField(max_length=25)
    user_address = models.CharField(max_length=255)
    user_guardian = models.CharField(max_length=100)
    user_parent = models.CharField(max_length=100)
    user_work_status = models.CharField(max_length=25)

