from django.urls import path

from .views import *

urlpatterns = [
    path('<pk>/edit/', EditTaskView.as_view(), name='task_edit'),
    path('<pk>/delete/', DeleteTaskView.as_view(), name='task_delete'),
]
