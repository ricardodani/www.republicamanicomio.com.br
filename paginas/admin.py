# -*- encoding: utf-8 -*-

from models import Pagina, Banner
from django.contrib import admin

class PaginaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}
    fieldsets = [
        ('Dados da Página',{'fields':['titulo', 'slug', 'foto', 'descricao', 'corpo', 'publicado', 'expiracao' ]}),
    ]
    list_display = ('titulo', 'slug', 'publicado',)

class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'link', 'publicado',)

admin.site.register(Pagina, PaginaAdmin)
admin.site.register(Banner, BannerAdmin)
