 
from django.urls import path
from . import views

urlpatterns = [
   
    path('signup/', views.signup),
    path('verification/', views.verification,name="verification"),
    path('login/', views.Login,name="Login"),
]
