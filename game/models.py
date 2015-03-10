from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    img_idx = models.IntegerField(default=0)
    
    COUNTING = 'COUNT'
    CLASSIFICATION = 'CLAS'
    UNKNMODE = 'UNKNOWN'
    USER_GAME_MODE_CHOICES = (
        (COUNTING, 'Counting Mode'),
        (CLASSIFICATION, 'Classification Mode'),
        (UNKNMODE, 'Unknown Game Mode'),
    )
    
    game_mode = models.CharField(max_length=8,
                              choices=USER_GAME_MODE_CHOICES,
                              default=UNKNMODE)

class UserLog(models.Model):
    LOGIN = 'LOGIN'
    LOGOUT = 'LOGOUT'
    HOME = 'HOME'
    START_GAME = 'START'
    COMPLETE_GAME = 'DONE'
    SKIP_GAME = 'SKIP'
    QUIT_GAME = 'QUIT'
    UNKNOWN = 'UNKNOWN'
    USER_ACTION_CHOICES = (
        (LOGIN, 'Login'),
        (LOGOUT, 'Logout'),
        (HOME, 'Home Screen'),
        (START_GAME, 'Start Game'),
        (COMPLETE_GAME, 'Complete Game'),
        (SKIP_GAME, 'Skip Game'),
        (QUIT_GAME, 'Quit Game'),
        (UNKNOWN, 'Unknown Action'),
    )
    
    user = models.CharField(max_length=256)
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

class Image(models.Model):
    id = models.AutoField(primary_key=True) # auto-increment
    iid = models.CharField(max_length=256, default='')
    url = models.URLField()
    species = models.CharField(max_length=256, default='Unknown species')
    obj_type = models.CharField(max_length=32, default='')
    obj_count = models.IntegerField(default=0)
    
    FEW = 'FEW'
    MANY = 'MANY'
    UNKNCLASS = 'UNKNOWN'
    IMAGE_TEST_CLASS_CHOICES = (
        (FEW, 'Few Objects'),
        (MANY, 'Many Objects'),
        (UNKNCLASS, 'Unknown Test Class'),
    )
    test_class = models.CharField(max_length=8,
                                  choices=IMAGE_TEST_CLASS_CHOICES,
                                  default=UNKNCLASS)
    
    NEW = 'NEW'
    IN_PROGRESS = 'INPROG'
    DONE = 'DONE'
    IMAGE_STATUS_CHOICES = (
        (NEW, 'New Image'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Data Collection Complete'),
    )
    # TODO: How should we update this?
    status = models.CharField(max_length=8,
                              choices=IMAGE_STATUS_CHOICES,
                              default=NEW)
    
    def __str__(self):
        return str(self.__dict__)
    
    # Object metadata
    class Meta:
        ordering = ["iid"] # def order when selecting objs
        # there's a way to set an 'active' flag and
        # only lookup items with active=true

class ClassificationResult(models.Model):
    image = models.ForeignKey('Image')
    user = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    flower_bool = models.BooleanField(default=False)
    bud_bool = models.BooleanField(default=False)
    fruit_bool = models.BooleanField(default=False)
    
    # Object metadata
    class Meta:
        unique_together = [("image","user")]

class CountResult(models.Model):
    image = models.ForeignKey('Image')
    user = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

    flower_coords = models.TextField(blank=True, null=True)
    bud_coords = models.TextField(blank=True, null=True)
    fruit_coords = models.TextField(blank=True, null=True)
    
    flower_count = models.IntegerField(default=0)
    bud_count = models.IntegerField(default=0)
    fruit_count = models.IntegerField(default=0)

    # Object metadata
    class Meta:
        unique_together = [("image","user")]

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






















































# What is this?
#	Pass a representation of the session
#	i.e. one user to a session; one to many association
