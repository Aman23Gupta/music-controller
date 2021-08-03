# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("<h1>Hello</h1>")

# Create your views here.
