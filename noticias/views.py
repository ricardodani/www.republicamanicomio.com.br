# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import Http404
from models import Noticia
from django.template import RequestContext

def noticia(request, link=None):
  
    if link:
        try:
            noticia = Noticia.objects.publicadas().get(cod=link)
            conteudo_relacionado = {
                "galerias":[ {"titulo":x.title, "id":x.id, "sample":x.sample(5)} for x in noticia.galerias_relacionados.filter(is_public=True) if len(x.sample(5)) > 0 ],
                "videos"  :[ {"titulo":x.titulo, "cod":x.cod} for x in noticia.videos_relacionados.all() ],
                "paginas" :[ {"titulo":x.titulo, "slug":x.slug} for x in noticia.paginas_relacionadas.filter(publicado=True) ],
            }
        except:
            raise Http404
    else:
        raise Http404
    
    c = {"noticia":noticia, "conteudo_relacionado":conteudo_relacionado}
    
    
    return render_to_response('conteudo/noticia.html', c, context_instance=RequestContext(request))