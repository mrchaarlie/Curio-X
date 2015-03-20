from django.core.management.base import BaseCommand, CommandError
from game.models import UserLog, ClassificationResult, CountResult

from optparse import make_option
from collections import Counter
import os

class Command(BaseCommand):
    help= 'Loads image URLs and metadata into the database'
    option_list = BaseCommand.option_list + (
        make_option('--logs',
            metavar='FILE',
            help='Pull user log files from database and output them to specified CSV file'),
        make_option('--clasresults',
            metavar='FILE',
            help='Pull classification results from database and output them to specified CSV file'),
        make_option('--countresults',
            metavar='FILE',
            help='Pull counting results from database and output them to specified CSV file'),
        )
    
    def handle(self, *args, **options):
        # Pull user logs
        logs = options['logs']
        if logs:
            try:
                with open(logs, 'w') as f:
                    userlogs = UserLog.objects.all()
                    cols = ','.join(['User','Action','Timestamp'])
                    f.write(cols + '\n')
                    for userlog in userlogs:
                        user = userlog.user
                        action = userlog.action
                        timestamp = userlog.timestamp.strftime("%s")
                        record = ','.join([user,action,timestamp])
                        f.write(record + '\n')
                        self.stdout.write(record)
                    self.stdout.write(cols)
                    self.stdout.write('Finished writing user log file "%s"' % logs)
            except IOError:
                raise CommandError('Error while writing to file "%s"' % logs)

        # Pull classification game results
        clas = options['clasresults']
        if clas:
            try:
                with open(clas, 'w') as f:
                    clasresults = ClassificationResult.objects.all()
                    cols = ','.join(['User','iID','Timestamp','Flower','Bud','Fruit'])
                    f.write(cols + '\n')
                    for result in clasresults:
                        user = result.user
                        iid = result.image.iid
                        timestamp = result.timestamp.strftime("%s")
                        flower = str(result.flower_bool)
                        bud = str(result.bud_bool)
                        fruit = str(result.fruit_bool)
                        
                        record = ','.join([user,iid,timestamp,flower,bud,fruit])
                        f.write(record + '\n')
                        self.stdout.write(record)
                    self.stdout.write(cols)
                    self.stdout.write('Finished writing file "%s"' % clas)
            except IOError:
                raise CommandError('Error while writing to file "%s"' % clas)
        
        # Pull counting game results
        count = options['countresults']
        if count:
            try:
                with open(count, 'w') as f:
                    countresults = CountResult.objects.all()
                    cols = ','.join(['User','iID','Timestamp','FlowerCount','BudCount','FruitCount'])
                    f.write(cols + '\n')
                    for result in countresults:
                        user = result.user
                        iid = result.image.iid
                        timestamp = result.timestamp.strftime("%s")
                        
                        # Get and count coordinates
                        coords = result.coords
                        if coords:
                            coordarray = [elem.split(':') \
                                             for elem in coords.strip('()').split('),(')]
                            counts = []
                            for i, pair in enumerate(coordarray):
                                if len(pair) == 2 and not 'Infinity' in pair[1]:
                                    counts.append(pair[0])
                            
                            counts = Counter(counts)
                            flower_count = str(counts['flower'])
                            bud_count = str(counts['bud'])
                            fruit_count = str(counts['fruit'])
                            
                            record = ','.join([user,iid,timestamp,flower_count,bud_count,fruit_count])
                            f.write(record + '\n')
                            self.stdout.write(record)
                        else:
                            continue
                    self.stdout.write(cols)
                    self.stdout.write('Finished writing file "%s"' % count)
            except IOError:
                raise CommandError('Error while writing to file "%s"' % count)
