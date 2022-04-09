from django.core.management.base import BaseCommand
from core.models import Worker, Shift

class Command(BaseCommand):
    help = "Update workers's availability everyday"

    def handle(self, *args, **kwargs):
        worker_qs = Worker.objects.all()
        for worker in worker_qs:
            worker.is_available = True
            worker.save()
        
        shift_qs = Shift.objects.all()
        for shift in shift_qs:
            shift.workers.clear()
            shift.save()