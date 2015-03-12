from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from game.models import Image, UserProfile, ClassificationResult

import os
import logging

logger = logging.getLogger(__name__)

def csrf_render(request, htmlpage, context):
    '''Wrapper for rendering to response with CSRF token in context'''
    context.update(csrf(request))
    return render_to_response(htmlpage, context)

@login_required
def index(request):
    '''Home page'''
    logger.debug('Serve index')
    return render_to_response('index.html', locals())

@login_required
def game(request):
    '''Classification game'''
    logger.debug('Serve game mode 1 page')
    
    c = {}
    user = request.user
    image_url = Image.objects.order_by('?')[0].url # TODO: Redundant
    if user.is_authenticated():
        image_url = Image.objects.filter(status=Image.NEW)[user.userprofile.img_idx].url
    
    c.update({'image_url' : image_url})
    return csrf_render(request, 'game.html', c) 

@login_required
def game2(request):
    '''Counting game'''
    logger.debug('Serve game mode 2 page')
    
    c = {}
    user = request.user
    image_url = Image.objects.order_by('?')[0].url # TODO: Redundant
    if user.is_authenticated():
        image_url = Image.objects.filter(status=Image.NEW)[user.userprofile.img_idx].url

    c.update({'image_url' : image_url})
    return csrf_render(request, 'game2.html', c) 

#@login_required
def gameSplash(request):
    logger.debug('Serve game mode 1 splash')
    return render_to_response('game-splash.html', locals()) 

#@login_required
def game2Splash(request):
    logger.debug('Serve game mode 2 splash')
    return render_to_response('game2-splash.html', locals()) 

def game_submit_task(request):
    logger.debug(request)
    
    if request.method == "POST":
        logger.debug("Get the post from the game")
        c = {}
        post = request.POST.copy()
        
        flowerbool = True if int(post.get('flowerbool')) else False
        budbool = True if int(post.get('budbool')) else False
        fruitbool = True if int(post.get('fruitbool')) else False
       
        logger.debug("POST request data: %s, %s, %s" % \
                        (flowerbool,
                        budbool,
                        fruitbool))
        
        user = request.user
        image_url = Image.objects.order_by('?')[0].url # TODO: Redundant
        if user.is_authenticated():
            userprofile = UserProfile.objects.get(user=user)
            result = ClassificationResult(user=userprofile.user.username, \
                         image=Image.objects.all()[userprofile.img_idx], \
                         flower_bool=flowerbool, \
                         bud_bool=budbool, \
                         fruit_bool=fruitbool)
            result.save()
            
            if len(Image.objects.all()) > userprofile.img_idx + 1:
                userprofile.img_idx += 1
                userprofile.save()
            image_url = Image.objects.filter(status=Image.NEW)[userprofile.img_idx].url
        
        c.update({'image_url' : image_url})
        return csrf_render(request, 'game.html', c)
    else:
        return HttpResponseServerError("post error: not a post")

def game2_submit_task(request):
    logger.debug(request)
    
    if request.method == "POST":
        logger.debug("Get the post from game 2")
        c = {}
        post = request.POST.copy()

        '''flowerbool = True if int(post.get('flowerbool')) else False
        budbool = True if int(post.get('budbool')) else False
        fruitbool = True if int(post.get('fruitbool')) else False

        logger.debug("POST request data: %s, %s, %s" % \
                        (flowerbool,
                        budbool,
                        fruitbool))'''

        user = request.user
        image_url = Image.objects.order_by('?')[0].url # TODO: Redundant
        if user.is_authenticated():
            userprofile = UserProfile.objects.get(user=user)
            '''result = ClassificationResult(user=userprofile.user.username, \
                         image=Image.objects.all()[userprofile.img_idx], \
                         flower_bool=flowerbool, \
                         bud_bool=budbool, \
                         fruit_bool=fruitbool)
            result.save()'''

            if len(Image.objects.all()) > userprofile.img_idx + 1:
                userprofile.img_idx += 1
                userprofile.save()
            image_url = Image.objects.filter(status=Image.NEW)[userprofile.img_idx].url

        c.update({'image_url' : image_url})
        return csrf_render(request, 'game2.html', c)
    else:
        return HttpResponseServerError("post error: not a post")

def game_skip(request):
    logger.debug("Get the skip from game")
    if request.method == "POST":
        post = request.POST.copy()
        c = {}
        
        user = request.user
        image_url = Image.objects.order_by('?')[0].url # TODO: Redundant
        if user.is_authenticated():
            userprofile = UserProfile.objects.get(user=user)
            if len(Image.objects.all()) > userprofile.img_idx + 1:
                userprofile.img_idx += 1
                userprofile.save()
            image_url = Image.objects.filter(status=Image.NEW)[userprofile.img_idx].url
        
        c.update({'image_url' : image_url})
        
        return csrf_render(request, 'game.html', c)
    else:
        return HttpResponseServerError("post error: not a post")
