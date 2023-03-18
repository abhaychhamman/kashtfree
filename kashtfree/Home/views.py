from django.shortcuts import render
from GenerateLink.models import GenerateLink
from datetime import datetime 
# Create your views here.
def Home(request):
    if request.user.is_authenticated:

        gl=GenerateLink.objects.filter(user=request.user)
        for i in gl:
              if (datetime.now().date().day)-(i.created_at.date().day)>15  or (datetime.now().date().month)-(i.created_at.date().month)>0:
                print((datetime.now().date()),(i.created_at.date()),i )
                i.delete()  #delete link when time is over
        
        return render(request,'home.html',context={"links":gl})
                
        

    return render(request,'home.html')