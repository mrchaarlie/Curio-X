from django.core.management.base import BaseCommand, CommandError
from game.models import Image 

from optparse import make_option
import os

class Command(BaseCommand):
    help= 'Loads image URLs and metadata into the database'
    option_list = BaseCommand.option_list + (
        make_option('--images',
            metavar='FILE',
            help='CSV file with (image id, species, object type, object count, test class)'),
        )
    
    def handle(self, *args, **options):
        images = options['images']
        if images:
            try:
                with open(images, 'r') as f:
                    for line in f:
                        row = [attr.strip() for attr in line.split(',')]
                        if row[0] == 'ImageID':
                            continue
                        url = 'https://s3-us-west-2.amazonaws.com/curiox/medres/' + \
                               row[4] + '/' + \
                               row[0] + '.jpg' #TODO: Un-hardcode
                        species = row[1].lower()
                        obj_type = row[2].lower()
                        obj_count = row[3]
                        if row[4].lower() == 'fewobj':
                            test_class = Image.FEW
                        elif row[4].lower() == 'manyobj':
                            test_class = Image.MANY
                        else:
                            test_class = Image.UNKNCLASS
                        
                        img = Image(url=url, species=species, 
                                    obj_type=obj_type, obj_count=obj_count, 
                                    test_class=test_class)
                        img.save()
                        self.stdout.write('Successfully added image %s of class %s' % (url, test_class))
            except IOError:
                raise CommandError('File "%s" does not exist' % images)
