# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def home_view(request ,*args, **kwargs):
    #return HttpResponse("<h1>Allan Site</h1>")
    print(args,kwargs)
    print(request.user)
    return render(request ,"home.html", {})
def products_view(request ,*args, **kwargs):
    return HttpResponse("<h1>Allan build this Site</h1>")