from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import os
import logging

logger = logging.getLogger(__name__)

@login_required
def index(request):
    logger.debug('Serve index')
    return render_to_response('index.html', locals())

@login_required
def game(request):
    logger.debug('Serve game mode 1 page')
    return render_to_response('game.html', locals()) 

@login_required
def game2(request):
    logger.debug('Serve game mode 2 page')
    return render_to_response('game2.html', locals()) 
