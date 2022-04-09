from .models import Worker, Shift
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from .serializers import WorkerSerializer, ShiftSerializer, ShiftUpdateSerializer
# Create your views here.

# Workers
class WorkersListAPIView(ListAPIView):
    """
    METHODS ALLOWED: GET
    API endpoint: api/workers-list/

    Lists all workers, displaying the most recently added worker.
    A typical worker object has the following fields:
        - first_name -> string
        - last_name -> string
        - email -> string
        - is_available -> boolean
    
    Returns a serialized jsonresponse
    """
    queryset = Worker.objects.order_by('-id')
    serializer_class = WorkerSerializer

class WorkerCreateAPIView(CreateAPIView):
    """
        METHODS ALLOWED: POST
        API endpoint: api/create-worker/

        Creates a new worker object. The following data is mandatory:
            - first_name -> string
            - last_name -> string
            - email -> string
        other field like is_available is set to True by default upon creation

        Returns the created object and a status code 201 if successful, else 400, 404, 500 depending on the error.
    """
    queryset = Worker.objects.order_by('-id')
    serializer_class = WorkerSerializer

    def perform_create(self, serializer):
        serializer.save(is_available=True)


# Shifts
class ShiftListAPIView(ListAPIView):
    """
    METHODS ALLOWED: GET
    API endpoint: api/shifts-list/

    Lists all shifts, displaying them in the earliest start time.
    A typical shift object has the following fields:
        - name -> string
        - start_time -> time field
        - end_time -> time field
        - workers -> many to many field to the Worker objects
    
    Returns a serialized jsonresponse
    """
    queryset = Shift.objects.order_by('start_time')
    serializer_class = ShiftSerializer

class ShiftCreateAPIView(CreateAPIView):
    """
        METHODS ALLOWED: POST
        API endpoint: api/shift/create/

        Creates a new shift object. The following data is mandatory:
            - name -> string
            - start_time -> time field
            - end_time -> time field
        Other field:
            - workers -> many to many field to the Worker objects. 

        Returns the created object and a status code 201 if successful, else 400, 404, 500 depending on the error.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class ShiftRetrieveAPIView(RetrieveAPIView):
    """
        METHODS ALLOWED: GET
        API endpoint: api/shift/<int:pk>/

        Gets the shift object that matches the shift_id. It returns the shift object if it finds it.

        Returns the created object and a status code 201 if successful, else 404 not found error.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class ShiftUpdateAPIView(UpdateAPIView):
    """The request body should be a "application/json" encoded object, containing the workers id list."""
    queryset = Shift.objects.order_by('start_time')
    serializer_class = ShiftUpdateSerializer

    def update(self, request, *args, **kwargs):
        shift_instance = self.get_object()
        workers = dict(request.data).get("workers")
        for i in workers:
            worker_id = int(i)
            worker = Worker.objects.get(id=worker_id)
            if worker.is_available:
                shift_instance.workers.add(worker.id)
            shift_instance.save()
            worker.is_available = False
            worker.save()
            
        serializer = ShiftSerializer(shift_instance)
        return Response(serializer.data)


from celery.schedules import crontab
from celery.task import periodic_task

@periodic_task(run_every=crontab(hour=18, minute=27, day_of_week="sat"))
def every_monday_morning():
    print("This is run every Monday morning at 7:30")
