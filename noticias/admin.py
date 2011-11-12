# -*- encoding: utf-8 -*-

from models import Noticia
from django.contrib import admin

class NoticiaAdmin(admin.ModelAdmin):
  prepopulated_fields = {"cod": ("titulo",)}
  list_display = ('cod', 'titulo', 'descricao', 'ativado', 'foto', 'data_criacao', 'data_publicacao')
  list_filter = ('data_criacao', 'data_publicacao', 'ativado')

admin.site.register(Noticia, NoticiaAdmin)