from os import name
from django.urls import path
from .views import (
    WorkersListAPIView,
    WorkerCreateAPIView,
    ShiftListAPIView,
    ShiftCreateAPIView,
    ShiftRetrieveAPIView,
    ShiftUpdateAPIView
)

urlpatterns = [
    path('worker/list/', WorkersListAPIView.as_view(), name="worker-list"),
    path('worker/create/', WorkerCreateAPIView.as_view(), name="create-worker"),
    path('shift/list/', ShiftListAPIView.as_view(), name="shift-list"),
    path('shift/create/', ShiftCreateAPIView.as_view(), name="create-shift"),
    path('shift/<int:pk>/', ShiftRetrieveAPIView.as_view(), name="shift-detail"),
    path('add-worker-to-shift/<int:pk>/', ShiftUpdateAPIView.as_view(), name="add_worker_to_shift"),
]
