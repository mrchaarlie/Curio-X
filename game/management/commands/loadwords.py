from django.core.management.base import BaseCommand, CommandError
from game.models import Adjective, Animal

from optparse import make_option
import os

class Command(BaseCommand):
    help= 'Loads words into the database'
    option_list = BaseCommand.option_list + (
        make_option('--adjectives',
            metavar='FILE',
            help='CSV file with adjectives'),
        make_option('--animals',
            metavar='FILE',
            help='CSV file with animals'),
        )
    
    def handle(self, *args, **options):
        print(options)
        adjectives = options['adjectives']
        try:
            with open(adjectives, 'r') as f:
                for line in f:
                    adj = Adjective(adjective=line)
                    adj.save()
                    self.stdout.write('Successfully added word %s' % adj)
        except IOError:
            raise CommandError('File "%s" does not exist' % adjectives)
        
        animals = options['animals']
        try:
            with open(animals, 'r') as f:
                for line in f:
                    an = Animal(animal=line)
                    an.save()
                    self.stdout.write('Successfully added word %s' % an)
        except IOError:
            raise CommandError('File "%s" does not exist' % animals)
                
