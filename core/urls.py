from os import name
from django.urls import path
from .views import (
    workers_list_api_view, 
    create_worker_api_view, 
    shifts_list_api_view, 
    create_shift_api_view, 
    shift_detail_api_view,
    add_worker_to_shift_api_view
)

urlpatterns = [
    path('workers-list/', workers_list_api_view, name="workers_list"),
    path('create-worker/', create_worker_api_view, name="create_worker"),
    path('shifts-list/', shifts_list_api_view, name="shifts_list"),
    path('create-shift/', create_shift_api_view, name="create_shift"),
    path('shift/<int:shift_id>/', shift_detail_api_view, name="shift_detail"),
    path('add-worker-to-shift/', add_worker_to_shift_api_view, name="add_worker_to_shift"),
]
