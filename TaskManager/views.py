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
                               ProjectSearchForm,
                               PositionForm,
                               PositionSearchForm,
                               TeamForm,
                               TeamSearchForm,
                               TaskForm,
                               TaskSearchForm,
                               WorkerCreationForm,
                               WorkerSearchForm)
from django.contrib.auth import get_user_model

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


class WorkersListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    template_name = "TaskManager/workers_list.html"
    context_object_name = "workers_list"

    def get_context_data(self, **kwargs):
        context = super(WorkersListView, self).get_context_data(**kwargs)
        first_name = self.request.GET.get("first_name", "")
        context["search_form"] = WorkerSearchForm(initial={"first_name": first_name})
        return context
    
    def get_queryset(self):
        queryset = get_user_model().objects.select_related("position")
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(first_name__icontains=form.cleaned_data["first_name"])
        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    template_name = "TaskManager/worker_detail.html"


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    form_class = WorkerCreationForm
    success_url = reverse_lazy("TaskManager:workers-list")
    template_name = "TaskManager/worker_form.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = WorkerCreationForm
    success_url = reverse_lazy("TaskManager:workers-list")
    template_name = "TaskManager/worker_form.html"


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    template_name = "TaskManager/worker_confirm_delete.html"
    success_url = reverse_lazy("TaskManager:workers-list")


class ProjectsListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "TaskManager/projects_list.html"
    context_object_name = "projects_list"

    def get_context_data(self, **kwargs):
        context = super(ProjectsListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = ProjectSearchForm(initial={"name": name})
        return context
    
    def get_queryset(self):
        queryset = Project.objects.prefetch_related("teams")
        form = ProjectSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


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
    context_object_name = "positions_list"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PositionsListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = PositionSearchForm(initial={"name": name})
        return context
    
    def get_queryset(self):
        queryset = Position.objects.all()
        form = PositionSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


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
    context_object_name = "teams_list"

    def get_context_data(self, **kwargs):
        context = super(TeamsListView, self).get_context_data(**kwargs)
        team_code = self.request.GET.get("team_code", "")
        context["search_form"] = TeamSearchForm(initial={"team_code": team_code})
        return context
    
    def get_queryset(self):
        queryset = Team.objects.prefetch_related("workers")
        form = TeamSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(team_code__icontains=form.cleaned_data["team_code"])
        return queryset


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    template_name = "TaskManager/team_detail.html"


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("TaskManager:teams-list")
    template_name = "TaskManager/team_form.html"


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
    context_object_name = "tasks_list"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(TasksListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(initial={"name": name})
        return context
    
    def get_queryset(self):
        queryset = Task.objects.select_related("task_type",
                                                "project").prefetch_related("assignees").filter(assignees=self.request.user)
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "TaskManager/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("TaskManager:tasks-list")
    template_name = "TaskManager/task_form.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("TaskManager:tasks-list")
    template_name = "TaskManager/task_form.html"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url=reverse_lazy("TaskManager:tasks-list")
    template_name = "TaskManager/task_confirm_delete.html"


class TaskTypesListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "TaskManager/tasktypes_list.html"
    queryset = TaskType.objects.all()
    context_object_name = "tasktypes_list"


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "TaskManager/tasktype_detail.html"