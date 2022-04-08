from rest_framework import serializers
from .models import Worker, Shift

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'is_available'
        ]

        
class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = [
            'id',
            'name',
            'start_time',
            'end_time',
            'workers'
        ]

        depth = 1