# -*- encoding: utf-8 -*-

from django.forms import ModelForm
from models import Recado


class RecadoForm(ModelForm):
  
  class Meta:
    model = Recado
    exclude = ["ativado",]