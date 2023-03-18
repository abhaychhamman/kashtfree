from django.shortcuts import render
from .models import Dev
# Create your views here.

def dloper(request):
    return render(request,'developer.html',context={"developers":Dev.objects.all()})