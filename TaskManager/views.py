import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from TaskManager.models import (Project,
                                Position,
                                TaskType,
                                Team,
                                Task,
                                Tag)
from TaskManager.forms import (ProjectForm,
                               ProjectSearchForm,
                               PositionForm,
                               PositionSearchForm,
                               TeamForm,
                               TeamSearchForm,
                               TaskForm,
                               TaskSearchForm,
                               WorkerCreationForm,
                               WorkerSearchForm,
                               TaskTypeForm,
                               TaskTypeSearchForm,
                               TagForm,
                               TagSearchForm)
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required
def home(request: HttpRequest) -> HttpResponse:
    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits
    context = {
        "current_day" : datetime.datetime.now().date,
        "current_time" : datetime.datetime.now().time,
        "first_name" : request.user.first_name,
        "last_name" : request.user.last_name,
        "email" : request.user.email,
        "position" : request.user.position.name,
        "tasks" : Task.objects.filter(assignees=request.user,
                                      is_completed=False).count(),
        "times_visited": num_visits
    }
    return render(request, 'TaskManager/home.html', context=context)


class WorkersListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    template_name = "TaskManager/workers_list.html"
    context_object_name = "workers_list"
    paginate_by = 10

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
    paginate_by = 10

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
    paginate_by = 10

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
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("query", "")
        context["search_form"] = TaskSearchForm(initial={"query": query})
        return context

    def get_queryset(self):
        queryset = Task.objects.select_related(
            "task_type", "project"
        ).prefetch_related("assignees", "tags").filter(
            assignees=self.request.user
        )

        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            if query:
                queryset = queryset.filter(
                    Q(name__icontains=query) |
                    Q(project__name__icontains=query) |
                    Q(tags__name__icontains=query)
                ).distinct()
        return queryset


    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        if task_id:
            task = Task.objects.filter(pk=task_id).first()
            if task:
                task.is_completed = True
                task.save()
        return redirect(request.path)


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
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TaskTypesListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskTypeSearchForm(initial={"name": name})
        return context
    
    def get_queryset(self):
        form = TaskTypeSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data["name"])
        return self.queryset


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "TaskManager/tasktype_detail.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    success_url = reverse_lazy("TaskManager:tasktypes-list")
    template_name = "TaskManager/tasktype_form.html"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    success_url = reverse_lazy("TaskManager:tasktypes-list")
    template_name = "TaskManager/tasktype_form.html"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url=reverse_lazy("TaskManager:tasktypes-list")
    template_name = "TaskManager/tasktype_confirm_delete.html"


class TagsListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    template_name = "TaskManager/tags_list.html"
    queryset = Tag.objects.all()
    context_object_name = "tags_list"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TagsListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TagSearchForm(initial={"name": name})
        return context
    
    def get_queryset(self):
        form = TagSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data["name"])
        return self.queryset


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("TaskManager:tags-list")
    template_name = "TaskManager/tag_form.html"


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("TaskManager:tags-list")
    template_name = "TaskManager/tag_form.html"


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url=reverse_lazy("TaskManager:tags-list")
    template_name = "TaskManager/tag_confirm_delete.html"

