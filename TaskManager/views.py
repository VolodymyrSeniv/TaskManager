import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from TaskManager.models import Worker, Position, Task
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from TaskManager.models import (Project,
                                Position,
                                Worker,
                                TaskType,
                                Team,
                                Task)
from TaskManager.forms import ProjectForm


def home(request: HttpRequest) -> HttpResponse:
    current_time = datetime.datetime.now()
    workers = Worker.objects.count()
    positions = Position.objects.count()
    tasks = Task.objects.count()
    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits
    context = {
        "current_time" : current_time,
        "workers" : workers,
        "positions" : positions,
        "tasks" : tasks,
        "times_visited": num_visits
    }
    return render(request, 'TaskManager/home.html', context=context)


class ProjectsListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "TaskManager/projects_list.html"
    queryset = Project.objects.all()
    context_object_name = "projects_list"


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ProjectForm
    success_url = reverse_lazy("TaskManager:projects-list")
    template_name = "TaskManager/project_form.html"


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("TaskManager:projects-list")
    template_name = "TaskManager/project_form.html"


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    template_name = "TaskManager/project_confirm_delete.html"
    success_url = reverse_lazy("TaskManager:projects-list")


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = "TaskManager/project_detail.html"


class PositionsListView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "TaskManager/positions_list.html"
    queryset = Position.objects.all()
    context_object_name = "positions_list"
    paginate_by = 10


class PositionDetailView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    template_name = "TaskManager/position_detail.html"


class TeamsListView(LoginRequiredMixin, generic.ListView):
    model = Team
    template_name = "TaskManager/teams_list.html"
    queryset = Team.objects.all().select_related("project").prefetch_related("workers")
    context_object_name = "teams_list"


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    template_name = "TaskManager/team_detail.html"


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "TaskManager/tasks_list.html"
    queryset = Task.objects.all().select_related("task_type",
                                                 "project").prefetch_related("assignees")
    context_object_name = "tasks_list"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "TaskManager/task_detail.html"


class TaskTypesListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "TaskManager/tasktypes_list.html"
    queryset = TaskType.objects.all()
    context_object_name = "tasktypes_list"


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "TaskManager/tasktype_detail.html"