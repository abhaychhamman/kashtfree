from django.shortcuts import render
from django.contrib import messages
from .models import Fdback
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def feedbackView(request):
    if request.method=="POST":
        Fdback.objects.create(yourname=request.POST['your_name'],user=request.user,email=request.POST['your_email'],comments=request.POST['comments']).save()
        messages.success(request,"Form has been submitted successfully .... ")
        return render(request,'contactus.html')

    return render(request,'feedback.html')