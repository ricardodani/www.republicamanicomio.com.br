# -*- encoding: utf-8 -*-

from forms import ContatoForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from paginas.models import Pagina

def mapa(request):
  c = {
  }
  
  return render_to_response('conteudo/mapa.html', c, context_instance=RequestContext(request))

def contato(request):
  alert = ''
  if request.method == 'POST':
    form = ContatoForm(request.POST)

    if form.is_valid():
      
      from django.template import loader, Context
      from django.core.mail import EmailMessage
      from django.conf import settings
      
      dados = {
        "nome": form.cleaned_data['nome'],
        "email": form.cleaned_data['email'],
        "assunto": form.cleaned_data['assunto'],
        "mensagem": form.cleaned_data['mensagem']
      }
      
      t = loader.get_template('conteudo/contato_email.html')
      c = Context(dados)
      
      html = t.render(c) 
      lista_envio = settings.EMAILS_FALE_CONOSCO
      assunto = "www.republicamanicomio.com.br - Contato"
      from_mail = "contato@republicamanicomio.com.br"
      
      for i in lista_envio:
        email = EmailMessage(assunto, html, from_mail, [i], headers = {'Reply-To': i})
        email.content_subtype = "html"
        try:
          email.send()
          alert = u"Mensagem enviada com sucesso."
        except:
          alert = u"Erro do Servidor SMTP. Mensagem não pode ser enviada."
  else:
    form = ContatoForm()
  
  try:
    contato_page = Pagina.objects.filter(slug="contato", publicado=True)[0]
  except:
    contato_page = None
  
  c = {
    'contato' : contato_page,
    'form'    : form,
    'alert'   : alert,
  }
  
  return render_to_response('conteudo/contato.html', c, context_instance=RequestContext(request))
