from django.core.management.base import BaseCommand, CommandError
from game.models import Adjective, Animal, Word

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
        make_option('--words',
            metavar='FILE',
            help='CSV file with single words'),
        )
    
    def handle(self, *args, **options):
        adjectives = options['adjectives']
        if adjectives:
            try:
                with open(adjectives, 'r') as f:
                    for line in f:
                        adj = Adjective(adjective=line)
                        adj.save()
                        self.stdout.write('Successfully added word %s' % adj)
            except IOError:
                raise CommandError('File "%s" does not exist' % adjectives)
        
        animals = options['animals']
        if animals:
            try:
                with open(animals, 'r') as f:
                    for line in f:
                        an = Animal(animal=line)
                        an.save()
                        self.stdout.write('Successfully added word %s' % an)
            except IOError:
                 raise CommandError('File "%s" does not exist' % animals)
            
        words = options['words']
        if words:
            try:
                with open(words, 'r') as f:
                    for line in f:
                        word = Word(word=line)
                        word.save()
                        self.stdout.write('Successfully added word %s' % word)
            except IOError:
                raise CommandError('File "%s" does not exist' % words)
