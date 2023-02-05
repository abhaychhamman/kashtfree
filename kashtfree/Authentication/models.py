from django.db import models

# Create your models here.
class Verification(models.Model):
    email=models.EmailField( max_length=254)
    code=models.IntegerField()