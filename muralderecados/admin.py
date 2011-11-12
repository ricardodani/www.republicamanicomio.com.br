# -*- encoding: utf-8 -*-

from models import Recado
from django.contrib import admin

class RecadoAdmin(admin.ModelAdmin):
  list_display = ('__unicode__', 'de', 'para', 'texto', 'ativado', 'data_criacao')
  list_filter = ('de', 'para', 'ativado')
  

admin.site.register(Recado, RecadoAdmin)