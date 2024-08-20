from django.urls import path
from TaskManager.views import home

urlpatterns = [
    path("", home)
]

app_name = "TaskManager"
