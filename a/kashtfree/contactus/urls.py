 
from django.urls import path
from . import views

urlpatterns = [
   
    
    path('contactus/', views.contactView,name="contactus"),
  
]
