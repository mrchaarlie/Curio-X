from django.db import models

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

class Log(models.Model):
    LOGIN = 'LOGIN'
    LOGOUT = 'LOGOUT'
    START_GAME = 'START'
    COMPLETE_GAME = 'DONE'
    QUIT_GAME = 'QUIT'
    UNKNOWN = 'UNKNOWN'
    USER_ACTION_CHOICES = (
        (LOGIN, 'Login'),
        (LOGOUT, 'Logout'),
        (START_GAME, 'Start Game'),
        (COMPLETE_GAME, 'Complete Game'),
        (QUIT_GAME, 'Quit Game'),
        (UNKNOWN, 'Unknown Action'),
    )
    
    user_id = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=7,
                              choices=USER_ACTION_CHOICES,
                              default=UNKNOWN)
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

#class Choice(models.Model):
#    results = models.ForeignKey(Results)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

#	Pass a representation of the session
#	i.e. one user to a session; one to many association
