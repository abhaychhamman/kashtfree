from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class GenerateLink(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.TextField()
    desc=models.TextField()
    linkName=models.TextField()
    activeDays=models.TextField()
    NumberOfcolumn=models.TextField()
    fieldName=models.TextField()
    created_at =  models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        return "/form/"+ self.linkName
 
    def __str__(self) -> str:
        return self.linkName
 
 
 
 

class DataColumn(models.Model):
    linkName=models.ForeignKey(GenerateLink, on_delete=models.CASCADE)
    data1=models.TextField()
    data2=models.TextField()
    data3=models.TextField()
    data4=models.TextField()
    data5=models.TextField()
    data6=models.TextField()
    data7=models.TextField()
    data8=models.TextField()
    data9=models.TextField()
    data10=models.TextField(default='')
    data11=models.TextField(default='')
    
    def __str__(self) -> str:
        return str(self.linkName)
    

 