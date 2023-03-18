from django.db import models

# Create your models here.
class Dev(models.Model):
    name=models.TextField()
    github=models.TextField()
    insta=models.TextField()
    linkedin=models.TextField()
    email=models.TextField(default="")
    desc=models.TextField()
    skills=models.TextField()
    address=models.TextField()
    img=models.ImageField(upload_to="media/dev/",default='')

    def __str__(self) -> str:
        return self.name