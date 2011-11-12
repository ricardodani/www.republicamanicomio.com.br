# -*- encoding: utf-8 -*-

from django.db import models
from django.conf import settings

class Video(models.Model):
  cod = models.CharField(unique=True, max_length=20, help_text=u"Insira o código do vídeo do YouTube.<br />\
                                      Exemplo: Se o link do vídeo for: http://www.youtube.com/watch?v=ILM8R8wVy8E<br />\
                                      Então, o cod será: ILM8R8wVy8E")
  titulo = models.CharField(max_length=100)

  def __unicode__(self):
    return self.titulo
  
  class Meta:
    #app_label = u"Páginas"
    verbose_name = u"Vídeo do Youtube"