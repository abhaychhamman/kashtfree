from django.contrib.sitemaps import Sitemap
from .models import GenerateLink
  
class GenerateLinkSitemap(Sitemap):
    def items(self):
        return GenerateLink.objects.all()
        
    def lastmod(self, obj):
        return obj.created_at