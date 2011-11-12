#!/usr/bin/python
# -*- coding: utf-8 -*

from models import Morador
from django.contrib import admin


class MoradorAdmin(admin.ModelAdmin):
  list_display  = ["nome", "email"]

admin.site.register(Morador, MoradorAdmin)