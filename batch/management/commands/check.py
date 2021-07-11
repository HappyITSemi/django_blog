# 使い方：
# $> python3 manage.py check -period 2021-03 2021-04 -dir media/output/media -file abc.csv
import logging

from django.core.management import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = '[Usage] command -period 2021-03 -dir media/outdata -file abc.csv'

    def add_arguments(self, parser):
        parser.add_argument('-period', nargs='+', type=str)  # nargs + -> must be at least 1
        parser.add_argument('-dir', type=str)  # Registered Argument 'dir'
        parser.add_argument('-file', type=str)
        parser.add_argument('-id', type=int)

    def handle(self, *args, **options):
        logger = logging.getLogger("django")
        logger.debug("debug--check")
        logger.error('error--check')

        now = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % now)
        print('time=', now)

        print('Period= ', options['period'])
        print('dir= ', options['dir'])
        print('file=', options['file'])
