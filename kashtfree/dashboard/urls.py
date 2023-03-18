 
from django.urls import path
from . import views

urlpatterns = [
   
    
    path('dashboard/<int:id>', views.Dashboard,name="dashboard"),
    path('linkData/', views.linkData,name="linkData"),
    path('deleteData/', views.deleteData,name="deleteData"),
    path('deleteLink/', views.deleteLink,name="deleteLink"),
]
