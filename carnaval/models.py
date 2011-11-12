# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

genero_choices = [('F', 'Feminino'), ('M', 'Masculino')]

class Turista(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=2, choices=genero_choices)
    email = models.EmailField(null=True, blank=True, verbose_name=u"E-mail")
    telefones = models.CharField(null=True, blank=True, max_length=100)
    grupo = models.ForeignKey("Grupo", verbose_name=u"Grupo")
    responsavel = models.BooleanField(verbose_name=u"Responsável pelo Grupo?")
    
    user = models.OneToOneField(User, null=True, blank=True, verbose_name=u"Usuário")

    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Turista"

class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Grupo de Turistas"
        verbose_name_plural = "Grupos de Turistas"
    
class Pacote(models.Model):
    grupo = models.OneToOneField(Grupo)
    
    def __unicode__(self):
        return "Pacote do Grupo %s" % self.grupo.nome
    
    class Meta:
        verbose_name = "Pacote de Grupo"
        verbose_name_plural = "Pacotes de Grupos"

class ItemPacote(models.Model):
    descricao = models.CharField(max_length=200)
    foto = models.ImageField(verbose_name="Foto Ilustrativa", upload_to=settings.UPLOAD_PATH)
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade", default=1)
    opcional = models.BooleanField(verbose_name=u"Opcional", default=False)
    pacote = models.ForeignKey(Pacote)
    preco_opcional = models.FloatField(null=True, blank=True, default=None, verbose_name=u"Preço Opcional")
    
    def __unicode__(self):
        return self.descricao
    
    class Meta:
        verbose_name = "Item do Pacote"
        verbose_name_plural = "Itens do Pacote"
    

dias_semana = [('DO', "Domingo"),
               ('SE', "Segunda"),
               ('TE', "Terça"),
               ('QA', "Quarta"),
               ('QI', "Quinta"),
               ('SE', "Sexta"),
               ('SA', "Sábado"),
               ]

class Bloco(models.Model):
    
    nome = models.CharField(max_length=50)
    foto = models.ImageField(verbose_name="Foto Ilustrativa", upload_to=settings.UPLOAD_PATH)
    dia = models.CharField(max_length=2, choices=dias_semana)
    sexo = models.CharField(max_length=2, choices=genero_choices)
    preco = models.FloatField(null=True, blank=True, verbose_name=u"Preço Aproximado")
    
    def __unicode__(self):
        return "%s - %s" % (self.nome, [x for x in genero_choices if x[0] == self.sexo][0][1])

    
    def getPreco(self):
        return ("R$ %.2f" % self.preco).replace('.',',')
    
    getPreco.short_description = 'Valor'
    
    class Meta:
        verbose_name = "Bloco"
    

class BlocosGrupo(models.Model):
    
    bloco = models.ForeignKey(Bloco)
    grupo = models.ForeignKey(Grupo)
    homens = models.PositiveSmallIntegerField()
    mulheres = models.PositiveSmallIntegerField()
    
    def __unicode__(self):
        return "Turistas no %s do grupo %s" % (self.bloco, self.grupo)
    
    class Meta:
        verbose_name = "Grupo em Bloco"
        verbose_name_plural = "Grupos em Blocos"

class Lote(models.Model):
    
    nome = models.CharField(max_length=50, verbose_name="Nome do Lote")
    genero = models.CharField(max_length=2, choices=genero_choices, verbose_name="Gênero")
    preco = models.FloatField(verbose_name="Preço base")
    
    def __unicode__(self):
        return "%s %s" % (self.nome, self.genero)
    
    class Meta:
        verbose_name = "Lote"
    