# -*- encoding: utf-8 -*-

from django.db import models

from django.conf import settings
from datetime import datetime
from tinymce import models as tinymce_models


class NoticiaManager(models.Manager):

  def publicadas(self):
      
    n = self.filter(ativado=True,data_publicacao__lte=datetime.now()).order_by('-data_publicacao')
    return n

def caminho_foto(instance, filename):
  cod = instance.cod
  return "%s/noticias/%s/%s" % (settings.UPLOAD_PATH, cod, filename)

class Noticia(models.Model):
  objects = NoticiaManager()
  
  titulo = models.CharField(max_length=100, verbose_name="Título")
  cod = models.SlugField(unique=True, help_text="Insira um código do tipo 'slug': \
            sem caracteres especiais, espaços e em letras minúsculas. Ele servirá \
            como URL para este objeto.")

  descricao = models.CharField(blank=True, null=True, max_length=255, verbose_name="Descrição")
  ativado = models.BooleanField()
  html = tinymce_models.HTMLField()

  foto = models.ImageField(blank=True, upload_to=caminho_foto, verbose_name='Foto')
  
  data_criacao = models.DateTimeField(auto_now=True, auto_now_add=True, verbose_name='Data de criação', editable=False)
  data_publicacao = models.DateTimeField(default=datetime.now, verbose_name='Data de publicação')
  
  
  from photologue.models import Gallery
  from videos.models import Video
  from paginas.models import Pagina
  
  galerias_relacionados = models.ManyToManyField(Gallery, null=True, blank=True)
  videos_relacionados = models.ManyToManyField(Video, verbose_name=u"Vídeos Relacionados", null=True, blank=True)
  paginas_relacionadas = models.ManyToManyField(Pagina, verbose_name=u"Páginas Relacionadas", null=True, blank=True)

  def __unicode__(self):
    return self.cod
  
  def get_absolute_url(self):
    return '%snoticias/%s' % (settings.ABSOLUTE_URL_PREFIX, self.cod)
  
  class Meta:
    verbose_name = u"Notícia"