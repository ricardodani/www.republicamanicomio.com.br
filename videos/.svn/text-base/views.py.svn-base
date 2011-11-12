# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from models import Video
from django.template import RequestContext

def videos(request):
  
  videos = Video.objects.all()
  
  c = {"videos":videos}

  return render_to_response('conteudo/videos.html', c, context_instance=RequestContext(request))