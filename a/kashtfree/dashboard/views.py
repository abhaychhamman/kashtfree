from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from GenerateLink.models import GenerateLink,DataColumn
import json
from django.core.serializers.json import DjangoJSONEncoder
import numpy as np
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def Dashboard(request,id):
    gl=GenerateLink.objects.filter(user=request.user)
    return render(request,"dashboard.html",context={"links":gl})


@csrf_exempt
def linkData(request):
 
    gl=GenerateLink.objects.get(linkName=request.POST['links'])
    fields=[i for i in gl.fieldName.split(',') if i !=""]
     
    lst=[]
    for i in range(int(gl.NumberOfcolumn)):
        a=DataColumn.objects.filter(linkName=gl).values("data"+str(i+1),'id')
        
        # temp.append({'data'+str(i+1):})
        b=json.dumps(list(a),cls=DjangoJSONEncoder)
        ll=[]
        ids=[]
       
        for j in eval(b):
            ids.append(j.get("id"))
            ll.append(j["data"+str(i+1)])
        lst.append(ll)
  
    
    a=np.array(lst)
    print(ids)

  
    return JsonResponse({"data":a.tolist(),"fields":fields,"m":a.shape[0],"n":a.shape[1],"ids":ids})


 
@csrf_exempt
def deleteData(request):
 
    for i in request.POST.get('ids').split(','):
        if i != '':
            DataColumn.objects.filter(id=int(i)).delete()
 
  
     
 
    return JsonResponse({"msg":"Record deleted datasuccessfully ..."})


 



 
 
@csrf_exempt
def deleteLink(request):
    print(request.POST)
    a=GenerateLink.objects.get(linkName=request.POST['link']).delete()
  
     
 
    return JsonResponse({"msg":"Record deleted datasuccessfully ..."})


 



 