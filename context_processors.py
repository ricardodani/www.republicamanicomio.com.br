# -*- encoding: utf-8 -*-

from django.conf import settings
from paginas.models import Banner
from photologue.models import Photo

def context(request):
    banners = Banner.objects.filter(publicado=True)
    
    try:
        ps = Photo.objects.filter(is_public=True).order_by("-date_added")[:9]
    except:
        ps = None
        
    c = {
       'SITE_NAME':settings.SITE_NAME,
       'ABSOLUTE_URL_PREFIX': settings.ABSOLUTE_URL_PREFIX,
       'banners':banners,
       'ultimas_fotos':ps,
    }
    return c
