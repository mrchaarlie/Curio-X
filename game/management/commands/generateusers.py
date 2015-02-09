from django.core.management.base import BaseCommand, CommandError
from game.management import userutils

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
                userutils.add_user(username=username, pwd=pwd)
        else:
            pass
