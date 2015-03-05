from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import os
import logging

logger = logging.getLogger(__name__)

#@login_required
def index(request):
    logger.debug('Serve index')
    return render_to_response('index.html', locals())

#@login_required
def game(request):
    logger.debug('Serve game mode 1 page')
    return render_to_response('game.html', locals()) 

#@login_required
def game2(request):
    logger.debug('Serve game mode 2 page')
    return render_to_response('game2.html', locals()) 

#@login_required
def gameSplash(request):
    logger.debug('Serve game mode 1 splash')
    return render_to_response('game-splash.html', locals()) 

#@login_required
def game2Splash(request):
    logger.debug('Serve game mode 2 splash')
    return render_to_response('game2-splash.html', locals()) 

def game2_submit_task(request):
    if request.method == "POST":
        post = request.POST.copy()
        # do with post what you will
        return render_to_response('game2.html', locals())
    else:
        return HttpResponseServerError("post error: not a post")
