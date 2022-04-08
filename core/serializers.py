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
    workers = WorkerSerializer(many=True, read_only=True)
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


class ShiftUpdateSerializer(serializers.ModelSerializer):
    workers = WorkerSerializer(many=True, read_only=False)
    class Meta:
        model = Shift
        fields = [
            'id',
            'workers'
        ]

        depth = 1