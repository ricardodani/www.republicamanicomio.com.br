from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^admin/', include(admin.site.urls)),
  (r'^photologue/', include('photologue.urls')),
  (r'^tinymce/', include('tinymce.urls')),

  url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':False}, name='site_media'),
  url(r'^admin_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes':False}, name='admin_media'),
         
  url(r'^noticias/(?P<link>[\w_-]+)', 'noticias.views.noticia', name="noticia"),
  url(r'^recados/$', 'muralderecados.views.recados', name="recados"),
  url(r'^mapa/$', 'contato.views.mapa', name='mapa'),
  url(r'^contato/$', 'contato.views.contato', name='contato'),
  url(r'^videos/$', 'videos.views.videos', name='videos'),
  url(r'^fotos/$', 'galerias.views.galerias', name='fotos'),
  url(r'^fotos/(?P<id>\d+)$', 'galerias.views.galerias', name='fotos'),
  url(r'^moradores/$', 'pessoas.views.moradores', name="moradores"),
  url(r'^moradores/(?P<categoria>\w+)', 'pessoas.views.moradores', name="moradores"),
  
  url(r'^(?P<pagina_slug>[\w_-]+)/$', 'paginas.views.pagina_info', name="pagina"),


  url(r'^$', 'portal.views.default', name="default"),

  
)
