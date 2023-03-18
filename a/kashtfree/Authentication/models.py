from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class Verification(models.Model):
    email=models.EmailField( max_length=254)
    code=models.IntegerField()
    
class MobileVerification(models.Model):
    mobile=models.EmailField( max_length=254)
    code=models.IntegerField()

# Create your models here.

 