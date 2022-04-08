from django.test import TestCase
from .models import Worker, Shift

# rest_framework tests
from rest_framework.test import APIClient

# Create your tests here.

class WorkerTestCase(TestCase):
    def setUp(self) -> None:
        Worker.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jdoe@email.com",
            is_available=True
            )
        Worker.objects.create(
            first_name="Pete",
            last_name="Raddison",
            email="praddison@email.com",
            is_available=True
            )
        Worker.objects.create(
            first_name="Yemi",
            last_name="Rasheed",
            email="yrasheed@email.com",
            is_available=True
            )
        Worker.objects.create(
            first_name="Emily",
            last_name="George",
            email="egeorge@email.com",
            is_available=True
            )

        Shift.objects.create(
            name="First Shift",
            start_time="00:00:00",
            end_time="08:00:00"
        )

        Shift.objects.create(
            name="Second Shift",
            start_time="08:00:00",
            end_time="16:00:00"
        )

        Shift.objects.create(
            name="Third Shift",
            start_time="16:00:00",
            end_time="23:59:59"
        )
    
    def get_client(self):
        client = APIClient()
        return client

    def test_workers_list_api(self):
        client = self.get_client()
        response = client.get('/api/workers-list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
    
    def test_create_worker_api(self):
        client = self.get_client()
        response = client.post(
            '/api/create-worker/',
            {
                'first_name':'Ben',
                'last_name':'Fray',
                'email':'bfray@email.com'
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('first_name'), 'Ben')
        self.assertEqual(response.json().get('is_available'), True)
    
    def test_shifts_list_api(self):
        client = self.get_client()
        response = client.get('/api/shifts-list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
    
    def test_create_shift_api(self):
        client = self.get_client()
        response = client.post(
            '/api/create-shift/',
            {
                'name':'Shift Four',
                'start_time':'16:00:00',
                'end_time':'23:59:59'
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('name'), 'Shift Four')
        self.assertEqual(len(response.json().get('workers')), 0)

    def test_shift_detail_successful_view(self):
        client = self.get_client()
        response = client.get('/api/shift/2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('name'), 'Second Shift')
        
    def test_shift_detail_unsuccessful_view(self):
        client = self.get_client()
        response = client.get('/api/shift/20/')
        self.assertEqual(response.status_code, 404)

    def test_add_worker_to_shift_post(self):
        client = self.get_client()
        response = client.post(
            '/api/add-worker-to-shift/',
            {
                'id':'1',
                'name':'First Shift',
                'start_time':'00:00:00',
                'end_time':'08:00:00',
                'workers': ['1', '3']
            },
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json().get("workers")), 2)
        worker_name = response.json().get("workers")[0].get('first_name')
        self.assertEqual(worker_name, "Jane")

    def test_add_worker_to_shift_put(self):
        client = self.get_client()
        response = client.put(
            '/api/add-worker-to-shift/',
            {
                'id':'1',
                'name':'First Shift',
                'start_time':'00:00:00',
                'end_time':'08:00:00',
                'workers': ['1', '3']
            },
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json().get("workers")), 2)
        worker_name = response.json().get("workers")[1].get('first_name')
        self.assertEqual(worker_name, "Yemi")
