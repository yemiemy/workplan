from .models import Worker, Shift

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WorkerSerializer, ShiftSerializer
# Create your views here.

@api_view(['GET'])
def workers_list_api_view(request, *args, **kwargs):
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
    qs = Worker.objects.all().order_by("-id")
    serializer = WorkerSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_worker_api_view(request, *args, **kwargs):
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
    serializer = WorkerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(is_available=True)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


# Shifts
@api_view(['GET'])
def shifts_list_api_view(request, *args, **kwargs):
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
    qs = Shift.objects.all().order_by("start_time")
    serializer = ShiftSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_shift_api_view(request, *args, **kwargs):
    """
        METHODS ALLOWED: POST
        API endpoint: api/create-shift/

        Creates a new shift object. The following data is mandatory:
            - name -> string
            - start_time -> time field
            - end_time -> time field
        Other field:
            - workers -> many to many field to the Worker objects. 

        Returns the created object and a status code 201 if successful, else 400, 404, 500 depending on the error.
    """
    serializer = ShiftSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(["GET"])
def shift_detail_api_view(request, shift_id, *args, **kwargs):
    """
        METHODS ALLOWED: GET
        API endpoint: api/shift/<int:shift_id>/

        Gets the shift object that matches the shift_id. It returns the shift object if it finds it.

        Returns the created object and a status code 201 if successful, else 404 not found error.
    """
    qs = Shift.objects.filter(id=shift_id)
    if not qs.exists():
        return Response({}, status=404)
    
    obj = qs.first()
    serializer = ShiftSerializer(obj)

    return Response(serializer.data, status=200)

@api_view(["POST", "PUT"])
def add_worker_to_shift_api_view(request, *args, **kwargs):
    """
        METHODS ALLOWED: POST, PUT
        API endpoint: api/add-worker-to-shift/

        Updates a shift object. The following data is required from the request body:
            A shift object containing:
                - name -> string
                - start_time -> time field
                - end_time -> time field
                - workers -> many to many field to the Worker objects. 
        Uses the data provided to update the shift and the workers.

        Returns the updated object and a status code 200 if successful, else 400, 404, 500 depending on the error.
    """
    serializer = ShiftSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = request.data
        if "id" not in data or "workers" not in data:
            return Response({
                "error":"invalid data provided. Requires the shift data: id, start_time, end_time, workers"
                }, status=400)

        shift_id = data['id']
        workers = data.get('workers')
        shift_qs = Shift.objects.filter(id=int(shift_id))
        # return an error if the shift with that id doesn't exists
        if not shift_qs.exists():
            return Response({'error':'shift not found.'}, status=404)

        # now update the shift
        shift = shift_qs.first()
        for i in workers:
            worker_id = int(i)
            worker = Worker.objects.get(id=worker_id)
            if worker.is_available:
                shift.workers.add(worker.id)
            shift.save()
            worker.is_available = False
            worker.save()
        serialize_obj = ShiftSerializer(shift)
        return Response(serialize_obj.data, status=200)
    return Response({}, status=400)