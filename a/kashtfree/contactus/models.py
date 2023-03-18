from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class contactUSModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.TextField()
    yourname=models.TextField()
    message=models.TextField()
    phone=models.IntegerField()
    created_at =  models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return str(self.user)