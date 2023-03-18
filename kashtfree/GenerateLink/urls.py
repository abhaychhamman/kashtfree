 
from django.urls import path
from . import views

from django.contrib.sitemaps.views import sitemap
from GenerateLink.sitemap import GenerateLinkSitemap
from django.urls import path
  
  


urlpatterns = [
   
    
    path('generateLink/', views.GenerateLinkView,name="generateLink"),
    path('formcolumn/<str:user>/<str:linkName>/<int:column>', views.FormColumn,name="formcolumn"),
    path('form/<str:linkName>', views.FormGenerator,name="formcolumn"),
    path('sitemap.xml', sitemap, {'sitemaps': {'generateLink' : GenerateLinkSitemap}},
     name='django.contrib.sitemaps.views.sitemap')
]
