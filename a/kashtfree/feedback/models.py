from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Fdback(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="abhay")
    email=models.TextField()
    yourname=models.TextField()
    comments=models.TextField()
    created_at =  models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return str(self.user)