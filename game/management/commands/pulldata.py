from django.core.management.base import BaseCommand, CommandError
from game.models import UserLog

from optparse import make_option
import os

class Command(BaseCommand):
    help= 'Loads image URLs and metadata into the database'
    option_list = BaseCommand.option_list + (
        make_option('--logs',
            metavar='FILE',
            help='Pull user log files from database and output them to specified CSV file'),
        )
    
    def handle(self, *args, **options):
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
