# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from photologue.models import Gallery

def galerias(request, id=None):

  galerias = Gallery.objects.all()
  
  try:
    galeria = Gallery.objects.get(id=id)
  except:
    galeria = None
  
  c = {
      'galerias':galerias,
      'galeria':galeria
  }
  
  return render_to_response('conteudo/galerias.html', c, context_instance=RequestContext(request))