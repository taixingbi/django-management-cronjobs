from django.core.management.base import BaseCommand, CommandError
import schedule
import time

#https://schedule.readthedocs.io/en/stable/
class Jobs:
    def min(self, min):
        def job():
            print("I'm working...")

        schedule.every(min).minutes.do(job)

        while True:
            schedule.run_pending()
            time.sleep(1)


class Command(BaseCommand):
    help = 'rename django project'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        while True:
            #print("test rename ....")
            Jobs().min(1/30)

            time.sleep(10)
