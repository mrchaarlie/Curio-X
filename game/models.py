from django.db import models
from django.contrib.auth.models import User

class UserLog(models.Model):
    # Probably not going to be able to use these...
    LOGIN = 'LOGIN'
    LOGOUT = 'LOGOUT'
    HOME = 'HOME'
    START_GAME = 'START'
    COMPLETE_GAME = 'DONE'
    QUIT_GAME = 'QUIT'
    UNKNOWN = 'UNKNOWN'
    USER_ACTION_CHOICES = (
        (LOGIN, 'Login'),
        (LOGOUT, 'Logout'),
        (HOME, 'Home Screen'),
        (START_GAME, 'Start Game'),
        (COMPLETE_GAME, 'Complete Game'),
        (QUIT_GAME, 'Quit Game'),
        (UNKNOWN, 'Unknown Action'),
    )
    
    user = models.CharField(max_length=256)#ForeignKey(User.username)
    session = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    action = models.CharField(max_length=7,
                              choices=USER_ACTION_CHOICES,
                              default=UNKNOWN)
    path = models.TextField()
    query = models.TextField()
    variables = models.TextField()
    method = models.CharField(max_length=4)
    secure = models.BooleanField(default=False)
    #ajax = models.BooleanField(default=False)
    meta = models.TextField(null=True, blank=True)
    #address = models.IPAddressField()
    
    #view_func = models.CharField(max_length=256)
    #view_docstr = models.TextField(null=True, blank=True)
    #view_args = models.TextField()
    
    resp_code = models.CharField(max_length=3)

    def __str__(self):
        return str(self.__dict__)

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.CharField(max_length=32)
    
    def __str__(self):
        return 'ID: {id}, Animal: {an}'.format(id=self.id,an=self.animal)

class Adjective(models.Model):
    id = models.AutoField(primary_key=True)
    adjective = models.CharField(max_length=32)
    
    def __str__(self):
        return 'ID: {id}, Adjective: {adj}'.format(id=self.id,adj=self.adjective)

class Word(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=32)
    
    def __str__(self):
        return 'ID: {id}, Word: {word}'.format(id=self.id,word=self.word)

class taskSubmission(models.Model):
    raw = models.TextField(blank=True,null=True)

##
## TODO: Put into another file (ex. signals.py)
##
from django.contrib.auth.signals import user_logged_in, user_logged_out

import logging
import simplejson as json

logger = logging.getLogger(__name__)

def log_login(sender, user, request, **kwargs):
    new_log = UserLog(
        session = request.session.session_key,
        action = UserLog.LOGIN,
        user = request.user.username,
        path  = request.path,
        query = request.META["QUERY_STRING"],
        variables = json.dumps(request.REQUEST.__dict__),
        method = request.method,
        secure = request.is_secure(),
        meta = request.META.__str__(), #need meta for unique entry
        )
    
    logger.debug('User %s login', new_log.user)
    new_log.save()

def log_logout(sender, user, request, **kwargs):
    new_log = UserLog(
        session = request.session.session_key,
        action = UserLog.LOGOUT,
        user = request.user.username,
        path  = request.path,
        query = request.META["QUERY_STRING"],
        variables = json.dumps(request.REQUEST.__dict__),
        method = request.method,
        secure = request.is_secure(),
        meta = request.META.__str__(), #need meta for unique entry
        )
    
    logger.debug('User %s logout', new_log.user)
    new_log.save()

# Capture the logins and logouts
user_logged_in.connect(log_login)
user_logged_out.connect(log_logout)


'''
class Result(models.Model):
    CLASSIFICATION = 'CLAS'
    COUNT = 'COUNT'
    UNKNOWN = 'UNKNOWN'
    GAME_TYPE_CHOICES = (
        (CLASSIFICATION, 'Classification'),
        (COUNT, 'Counting'),
        (UNKNOWN, 'Unknown Game Type'),
    )
    
    img_id = models.PositiveIntegerField(default=0)
    user_id = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    game_type = models.CharField(max_length=7,
                                 choices=GAME_TYPE_CHOICES,
                                 default=UNKNOWN)
    output = models.CharField(max_length=200)
    # Object metadata
    class Meta:
        unique_together = [("img_id","user_id")] # user only uses image once
'''

'''
class Image(models.Model):
    id = models.AutoField(primary_key=True) # auto-increment
    url = models.URLField()
    
    def __str__(self):
        return '{}, {}'.format(self.id,self.url)
    
    # Object metadata
    class Meta:
        ordering = ["id"] # def order when selecting objs
        # there's a way to set an 'active' flag and
        # only lookup items with active=true
    ''
    NEW = 'NEW'
    IN_PROGRESS = 'INPROG'
    DONE = 'DONE'
    IMAGE_STATUS_CHOICES = (
        (NEW, 'New Image'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Data Collection Complete'),
    )
    
    status = models.CharField(max_length=6,
                              choices=IMAGE_STATUS_CHOICES,
                              default=NEW)
    ''
'''

# What is this?
#	Pass a representation of the session
#	i.e. one user to a session; one to many association
