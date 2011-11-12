# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from models import Recado
from django.template import RequestContext

def recados(request):
  
  alert = ''
  
  from forms import RecadoForm
  
  if request.method == 'POST':
    form = RecadoForm(request.POST)
    if form.is_valid():
      form.save()
      alert = u'Recado Salvo! O seu recado será publicado assim que o administrador do site ativá-lo'
  else:
    form = RecadoForm()
  
  lim = 20
  recados = Recado.objects.filter(ativado=True).order_by("-data_criacao")[:lim]
  
  c = {
    "recados":recados,
    "form"   :form,
    "alert"  :alert,
  }
  
  return render_to_response('conteudo/recados.html', c, context_instance=RequestContext(request))