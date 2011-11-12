# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.localflavor.br.br_states import STATE_CHOICES as UFS
from django.conf import settings

CATEGORIAS = (
  ('EA', "Ex-Alunos"),
  ('HO', "Homenageados"),
  ('MO', "Moradores"),
)

def caminho_foto(instance, filename):
    return "%s/moradores/%s" % (settings.UPLOAD_PATH, filename)
  
class Morador(models.Model):
    """Perfil do morador com seus dados."""
    
    foto = models.ImageField(upload_to=caminho_foto)

    nome = models.CharField(max_length=100)
    email = models.EmailField(verbose_name=u"E-mail de contato")
    
    categoria = models.CharField(max_length=2, choices = CATEGORIAS)
    
    sobre = models.CharField(max_length=100)

    cidade = models.CharField(null=True, blank=True, max_length=100)
    uf = models.CharField(null=True, blank=True, max_length=2, choices=UFS)
    
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name = u"Doido"
        verbose_name_plural = u"Doidos"