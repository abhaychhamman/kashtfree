from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def GenerateLinkView(request):
    linksperuser=GenerateLink.objects.filter(user=request.user)
    if request.method=="POST":
        linksperuserlen=len(GenerateLink.objects.filter(user=request.user))
        
        msgerr=""

        flag=True
        flagexcept=False
        if linksperuserlen >5:
            flag=False
            msgerr+="<br>You can only generate 5 Links .Please wait to expired link otherwise you can delete the available links ....<br> "
        try:
            if int(request.POST['time_active_link']) >=16:
                msgerr+="<br>Your link only ,we can active for 15 days  ...."
                flag=False
        except ValueError:
            flagexcept=True
            msgerr+="<br>Please enter only number upto 15 for active links . string not allowed"
        
    
            
        try:
            if int(request.POST['nfields']) >=12:
                flag=False
                msgerr+="<br>You can only take 11 columns ...."
        except:
            flagexcept=True
            msgerr+="<br>Please enter only number upto 11 in column field . string not allowed"

        
        a=GenerateLink.objects.filter(linkName=request.POST['link_name'])
        if len(a) != 0:
            msgerr+="<br>link name  already taken ....<br> "
            print("waah")
            flag=False
        
        if flagexcept:
            messages.error(request,msgerr,extra_tags='safe')
            return render(request,"generate_link.html",context={"userAlllinks":linksperuser})

  


       

            

        if flag:
            GenerateLink.objects.create(user=request.user,title=request.POST['form_title'],desc=request.POST['form_desc'],linkName=request.POST['link_name'],activeDays=request.POST['time_active_link'],NumberOfcolumn=request.POST['nfields']).save()
            return HttpResponseRedirect(f"/formcolumn/{request.user.username}/{request.POST['link_name']}/{request.POST['nfields']}")
          
        else:            
            messages.error(request,msgerr,extra_tags='safe')
            return render(request,'generate_link.html',context={"userAlllinks":linksperuser})

         


    return render(request,'generate_link.html',context={"userAlllinks":linksperuser})

 

 
def FormColumn(request,user,linkName,column): 


    # print(request.POST,request.method)
    if request.method=="POST":
         
        lst=""  #colllector fields of form

        #collect all field name of form
        for i in range(column):
            lst+=(request.POST["Column"+str(i+1)])+","
        
        # dc=DataColumn.get(column)
        dc=GenerateLink.objects.get(linkName=linkName)
        dc.fieldName=lst
        dc.save() 
        messages.success(request,f"Your form has been created successfully .....<br>You Link name is : <a href='form/{linkName}' target='_blank'>kashtfree.in/form/{linkName}</a>",extra_tags='safe')
        return HttpResponseRedirect("/")

    else:
        if(user==request.user.username):
            return render(request,'form_column.html',context={"nfields":range(1,column+1)})
    return HttpResponse("Your Url doesn't Match .....")



# this is for genrate form for particular links 

def FormGenerator(request,linkName):
    link=GenerateLink.objects.get(linkName=linkName.strip()) 
    print(link)
    print(linkName)

    if request.method=="POST":
     
        # nf=DataColumn.get(int(link.NumberOfcolumn)).objects.create(linkName=link)
        lst=[]
        for i in range(1,int(link.NumberOfcolumn)+1):
            lst.append(request.POST['column'+str(i)])
     
        for i in range(11-int(link.NumberOfcolumn)):
            lst.append("")
     
        DataColumn(linkName=link,data1=lst[0],data2=lst[1],data3=lst[2],data4=lst[3],data5=lst[4],data6=lst[5],data7=lst[6],data8=lst[7],data9=lst[8],data10=lst[9],data11=lst[10]).save()
        messages.success(request,"You form has been submitted successfully.....")
        return HttpResponseRedirect("/")
        # print(GenerateLink.objects.all().values("user","title"))
        
        
            
            
        
   
    return render(request,'form_generator.html',context={"title":link.title,"desc":link.desc,"fieldname":link.fieldName.split(',')})