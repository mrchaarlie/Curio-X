from django.contrib.auth.models import User
from game.models import UserProfile
from game.models import Adjective, Animal, Word

def add_user(username, pwd, email='curio.x.dev@gmail.com'):
    user = User.objects.create_user(username=username, password=pwd, email=email)
    user_profile = UserProfile(user=user)
    user_profile.save()
    print('Successfully created user %s' % user_profile.user)
    return user_profile

def generate_username():
    while True: #TODO: Avoid collisions
        adj = Adjective.objects.order_by('?')[0]
        an = Animal.objects.order_by('?')[0]
        username = ''.join([adj.adjective.strip(), an.animal.strip()])
        if is_username_available(username):
            print('Generated username %s' % username)
            return username

def is_username_available(username):
    return True if not User.objects.filter(username=username).exists() else False

def generate_pass():
    pwd = ''
    for word in Word.objects.order_by('?')[:3]:
        pwd = ''.join([pwd.strip(), word.word.strip()])
    print('Generated password %s' % pwd)
    return pwd
