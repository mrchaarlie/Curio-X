from django.db import models

class Results(models.Model):
    image_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    game_type = models.CharField(max_length=200)
    output = models.CharField(max_length=200)

#class Choice(models.Model):
#    results = models.ForeignKey(Results)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
