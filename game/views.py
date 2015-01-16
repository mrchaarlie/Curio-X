from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

import os
import datetime

current_dir = os.path.dirname(__file__)  # get current directory

def index(request):
    return render_to_response('index.html',locals())

def game(request):
    return render_to_response('game.html',locals()) 

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now {NOW}.</body></html>".format(NOW=now)
    return HttpResponse(html)
