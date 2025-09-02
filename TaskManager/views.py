import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from TaskManager.models import Worker, Position, Task


def home(request: HttpRequest) -> HttpResponse:
    current_time = datetime.datetime.now()
    workers = Worker.objects.count()
    positions = Position.objects.count()
    tasks = Task.objects.count()
    context = {
        "current_time" : current_time,
        "workers" : workers,
        "positions" : positions,
        "task" : tasks,
    }
    return render(request, 'TaskManager/index.html', context=context)
