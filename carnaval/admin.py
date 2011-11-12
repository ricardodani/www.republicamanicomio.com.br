# -*- encoding: utf-8 -*-

from models import Turista, Grupo, Pacote, ItemPacote, Bloco, BlocosGrupo, Lote
from django.contrib import admin

class TuristaAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'grupo', 'sexo', 'email', 'telefones', 'responsavel', 'user')
    list_editable = ('email', 'telefones',)
    list_filter = ('grupo', 'sexo', 'responsavel')
    save_as = True
    search_fields = ('nome','email', 'telefone', 'responsavel')

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'nome',)
    list_editable = ('nome',)
    search_fields = ('nome', )
    #colocar turistas no grupo


class PacoteAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Dados do Pacote de Grupo", {
            'fields': ('grupo',)
        }),
    )
    list_display = ('__unicode__', 'grupo',)
    list_editable = ('grupo',)
    search_fields = ('grupo', )
    #colocar itens no pacote

class ItemPacoteAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'foto', 'quantidade', 'opcional', 'pacote', 'preco_opcional')
    list_editable = ('foto', 'quantidade', 'opcional', 'pacote', 'preco_opcional')
    list_filter = list_editable
    save_as = True
    search_fields = ('descricao',)

class BlocoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'nome', 'foto', 'dia', 'sexo', 'preco')
    list_editable = ('nome', 'foto','dia', 'sexo', 'preco')
    list_filter = ('dia', 'sexo', 'preco')
    ordering = ('nome', 'sexo')
    save_as = True
    search_fields = ('nome', )

class BlocosGrupoAdmin(admin.ModelAdmin):
    pass

class LoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Turista, TuristaAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Pacote, PacoteAdmin)
admin.site.register(ItemPacote, ItemPacoteAdmin)
admin.site.register(Bloco, BlocoAdmin)
admin.site.register(BlocosGrupo, BlocosGrupoAdmin)
admin.site.register(Lote, LoteAdmin)