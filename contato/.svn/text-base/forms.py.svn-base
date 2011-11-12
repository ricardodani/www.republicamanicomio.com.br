# -*- encoding: utf-8 -*-

from django import forms

class ContatoForm(forms.Form):
  nome = forms.CharField(max_length=50, min_length=2, widget=forms.TextInput, required=True, label=u'Nome')
  email = forms.EmailField(required=True, label=u'E-mail')
  assunto = forms.CharField(widget=forms.TextInput, max_length=50, required=True, label=u'Assunto')
  mensagem = forms.CharField(widget=forms.Textarea)

