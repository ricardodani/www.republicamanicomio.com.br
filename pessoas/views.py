# -*- encoding: utf-8 -*-
from models import Morador
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404

def moradores(request, categoria=None):
  if categoria:
    m = Morador.objects.filter(categoria=categoria)
  else:
    m = Morador.objects.all()
  
  from models import CATEGORIAS
  
  cat = u"Os Doidos"
  for i in CATEGORIAS:
    if i[0] == categoria:
      cat = i[1]
      
  c = { 'moradores': m, 'categoria':cat, 'categorias':CATEGORIAS }
  return render_to_response('conteudo/moradores.html', c, context_instance=RequestContext(request))
