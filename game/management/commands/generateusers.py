from django.core.management.base import BaseCommand, CommandError
from game.management import userutils
from game.models import UserProfile

from optparse import make_option

class Command(BaseCommand):
    help= 'Generate users by bulk into the database'
    option_list = BaseCommand.option_list + (
        make_option('--random',
            action='store_true',
            help='Generate random users'),
        make_option('--number',
            type=int,
            default=1,
            help='Number of users to generate'),
        )
    
    def handle(self, *args, **options):
        if options['random']:
            for i in range(options['number']):
                pwd = userutils.generate_pass()
                username = userutils.generate_username()
                user_profile = userutils.add_user(username=username, pwd=pwd)
                if i % 2 == 0:
                    user_profile.game_mode = UserProfile.COUNTING
                else:
                    user_profile.game_mode = UserProfile.CLASSIFICATION
                user_profile.save()
                print("User %s is assigned to game mode %s" % (user_profile.user.username, user_profile.game_mode))
        else:
            pass
