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
from TaskManager.forms import (ProjectForm,
                               PositionForm,
                               TeamForm,
                               TaskForm)


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
    model = Project
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


class PositionsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("TaskManager:positions-list")
    template_name = "TaskManager/position_form.html"


class PositionsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("TaskManager:positions-list")
    template_name = "TaskManager/position_form.html"


class PositionsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    template_name = "TaskManager/position_confirm_delete.html"
    success_url = reverse_lazy("TaskManager:positions-list")


class TeamsListView(LoginRequiredMixin, generic.ListView):
    model = Team
    template_name = "TaskManager/teams_list.html"
    queryset = Team.objects.all().select_related("project").prefetch_related("workers")
    context_object_name = "teams_list"


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    template_name = "TaskManager/team_detail.html"


class TeamCreateView(LoginRequiredMixin, generic.DetailView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("TaskManager:teams-list")
    template_name = "TaskManager/team_from.html"


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("TaskManager:teams-list")
    template_name = "TaskManager/team_form.html"


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url=reverse_lazy("TaskManager:teams-list")
    template_name = "TaskManager/team_confirm_delete.html"


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "TaskManager/tasks_list.html"
    queryset = Task.objects.all().select_related("task_type",
                                                 "project").prefetch_related("assignees")
    context_object_name = "tasks_list"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "TaskManager/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.DetailView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("TaskManager:teams-list")
    template_name = "TaskManager/task_form.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("TaskManager:teams-list")
    template_name = "TaskManager/task_form.html"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url=reverse_lazy("TaskManager:teams-list")
    template_name = "TaskManager/task_confirm_delete.html"

class TaskTypesListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "TaskManager/tasktypes_list.html"
    queryset = TaskType.objects.all()
    context_object_name = "tasktypes_list"


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "TaskManager/tasktype_detail.html"