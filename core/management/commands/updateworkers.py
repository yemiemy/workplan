from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = "Update workers's availability everyday"

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        print("This works now")