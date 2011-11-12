# -*- encoding: utf-8 -*-

from django.db import models
from django.conf import settings
from tinymce import models as tinymce_models
from django.db.models import Q
from datetime import datetime
from django.conf import settings 
# Create your models here.


class PaginaManager(models.Manager):
    
    def publicadas(self):
        
        n = self.filter(Q(publicado=True, expiracao__gte=datetime.now())|
                        Q(publicado=True, expiracao=None)).order_by('criacao')
        
        return n
        
        
class Pagina(models.Model):
    objects = PaginaManager()
    titulo = models.CharField(max_length=127, verbose_name='Título')
    slug = models.SlugField(unique=True, editable=True, verbose_name='Slug (link relativo)', default='')
    descricao = models.CharField(blank=True, max_length=255, verbose_name='Descrição')
    foto = models.ImageField(blank=True, upload_to=settings.UPLOAD_PATH, verbose_name='Foto')
    corpo = tinymce_models.HTMLField()
    publicado = models.BooleanField(verbose_name='Publicado')
    criacao = models.DateTimeField(auto_now=True, auto_now_add=True, verbose_name='Data de criação', editable=False)
    expiracao = models.DateTimeField(null=True, blank=True, verbose_name='Data de expiração')

    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return '%spaginas/%s' % (settings.ABSOLUTE_URL_PREFIX, self.slug)

class Banner(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título do Banner')
    arquivo = models.FileField(upload_to=settings.UPLOAD_PATH, verbose_name='Arquivo do Banner')
    link = models.URLField(blank=True, verify_exists=False, verbose_name='URL')
    publicado = models.BooleanField(verbose_name='Publicado')

    def __unicode__(self):
        return self.titulo
        
