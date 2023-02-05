from django.shortcuts import render,HttpResponseRedirect,redirect
from email.message import EmailMessage
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from django.contrib.auth.models import User
from .models import Verification
from django.http import JsonResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def signup(request):

    if(request.method=="POST"):
        vf=Verification.objects.get(email=request.POST['user_email'])   # get the verification code by the user email
        if(str(vf.code)==request.POST['code']):
            user=User.objects.create_user(username=request.POST['user_email'],password=request.POST['user_password'],email=request.POST['user_email'])
            user.first_name=request.POST['user_fname']
            user.last_name=request.POST['user_lname']
            user.save()
            user=authenticate(username=request.POST['user_email'],password=request.POST['user_password']) 
            # print(user,request.POST['email'],request.POST['password'])
            login(request,user) 
            messages.success(request, "Your Email Verification SuccessFully  !!...!")
           
            return HttpResponseRedirect('/')
             
    
    return render(request,"signup.html")





@csrf_exempt
def verification(request):
  
    if(len(User.objects.filter(username=request.POST['email']))>0):
           return JsonResponse({"data":"userExists"})
       
    else:

        verification_code=random.randint(1000,2000)
        semail="www.abhaysingh722@gmail.com"
        psd="unmxddbfahesfhql"
        remail=request.POST['email']
        subject="verification on Kashtfree Website"
        try:
            vf=Verification.objects.get(email=request.POST['email'])
            vf.code=verification_code
            vf.save()
        except:
            # print("email doesn't exist")
            Verification.objects.create(email=request.POST['email'],code=verification_code).save()
            
        
        
        
        body=f"""
    <div class="cont">
    <p>thanks to register on our website ,Now continue the verification
    <h3>Your Verification Code is: <a style="color:blue; text-decoration:underline;">{verification_code}</a></h3>
    </div>
    """
        # em=EmailMessage()
        em = MIMEMultipart('alternative')
        em['From']=semail
        em['To']=remail
        em['Subject']=subject
        # em.set_content(body)
        part1 = MIMEText(body, 'html')
        # part2 = MIMEText(text, 'plain')
        context=ssl.create_default_context()
        em.attach(part1)

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp :
            smtp.login(semail,psd)
            smtp.sendmail(semail,remail,em.as_string())

            # print("sent verification code!")
        

        return JsonResponse({"data":"","sent verification":""})











def Login(request):
  
  
    if request.method == 'POST' and request.POST['submit']=="Log in":  
            print(request.POST)
            user=authenticate(username=request.POST['user_email'],password=request.POST['user_password']) 
            # print(user,request.POST['email'],request.POST['password'])
            if user is not None:
                login(request,user)
                print(request.user.is_authenticated)
               
                return HttpResponseRedirect('/')
            else:
             
                messages.success(request, "Your password or username Wrong... !!...!")
                return HttpResponseRedirect('/login/')

    return render(request,"login.html")