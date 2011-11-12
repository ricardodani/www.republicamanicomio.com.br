# -*- encoding: utf-8 -*-

from django.db import models

class Recado(models.Model):
  
    de = models.CharField(max_length=100, verbose_name="De")
    para = models.CharField(max_length=100, verbose_name="Para")
    texto = models.CharField(max_length=255, verbose_name="Texto")
    
    ativado = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(auto_now=True, auto_now_add=True, verbose_name='Data de criação', editable=False)

    def __unicode__(self):
        return "Recado %s" % (self.id)
    
    class Meta:
        #app_label = u"Páginas"
        verbose_name = u"Recado"