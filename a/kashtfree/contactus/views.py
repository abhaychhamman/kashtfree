from django.shortcuts import render
from .models import contactUSModel
from django.contrib import messages

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def contactView(request):

    if request.method=="POST":
        contactUSModel.objects.create(yourname=request.POST['your_name'],user=request.user,email=request.POST['your_email'],message=request.POST['your_msg'],phone=request.POST['your_mob']).save()
        messages.success(request,"Form has been submitted successfully .... ")
        return render(request,'contactus.html')

    return render(request,'contactus.html')