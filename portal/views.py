# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from noticias.models import Noticia
from videos.models import Video

def default(request):
    try:
        destaque = Noticia.objects.publicadas()[0]
    except:
        destaque = None
    noticias = Noticia.objects.publicadas()[1:][:3]
    
    
    try:
        v = Video.objects.order_by('-id')[0]
    except:
        v = None
    
    c = {"noticias":noticias, "destaque":destaque, "video":v}
    
    return render_to_response('conteudo/default.html', c, context_instance=RequestContext(request))
