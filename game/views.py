from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

import os
import logging

logger = logging.getLogger(__name__)

#@login_required
def index(request):
    logger.debug('Serve index')
    return render_to_response('index.html', locals())

#@login_required
def game(request):
    c = {}
    c.update(csrf(request))
    logger.debug('Serve game mode 1 page')
    return render_to_response('game.html', c) 

#@login_required
def game2(request):
    c = {}
    c.update(csrf(request))
    logger.debug('Serve game mode 2 page')
    return render_to_response('game2.html', c) 

#@login_required
def gameSplash(request):
    logger.debug('Serve game mode 1 splash')
    return render_to_response('game-splash.html', locals()) 

#@login_required
def game2Splash(request):
    logger.debug('Serve game mode 2 splash')
    return render_to_response('game2-splash.html', locals()) 

def game_submit_task(request):
    if request.method == "POST":
        post = request.POST.copy()
        logger.debug(request)
        c = {}
        c.update(csrf(request))
        logger.debug("Get the post from the game")
        return render_to_response('game.html', c)
    else:
        return HttpResponseServerError("post error: not a post")

def game2_submit_task(request):
    if request.method == "POST":
        post = request.POST.copy()
        c = {}
        c.update(csrf(request))
        logger.debug("Get the post from game 2")
        return render_to_response('game2.html', c)
    else:
        return HttpResponseServerError("post error: not a post")
