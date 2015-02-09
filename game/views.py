from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import os
import datetime

from game.models import Image

current_dir = os.path.dirname(__file__)  # get current directory

@login_required
def index(request):
    '''
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)'''
    return render_to_response('index.html', locals())
    '''    else:
            print('Disabled account')
    else:
        print('Invalid login')'''

def game(request):
    return render_to_response('game.html', locals()) 

#def game(request):
#    image = Image.objects.get(id=1)
#    return render_to_response('game.html',locals()) 
