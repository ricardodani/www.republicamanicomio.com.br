# -*- encoding: utf-8 -*-
from django.template import RequestContext
from models import Pagina
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings


def pagina_info(request, pagina_slug):
    try:  
        p = Pagina.objects.get(slug=pagina_slug, publicado=True)
    except Pagina.DoesNotExist:
        raise Http404
    else:
        c = {
            'pagina': p,
        }
        return render_to_response('conteudo/pagina.html',  
                                  c, 
                                  context_instance=RequestContext(request))

