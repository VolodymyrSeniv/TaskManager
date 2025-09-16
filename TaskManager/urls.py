from django.urls import path
from TaskManager.views import home
from TaskManager.views import (ProjectsListView,
                               ProjectDetailView,
                               PositionsListView,
                               PositionDetailView,
                               TeamsListView,
                               TeamDetailView,
                               TasksListView,
                               TaskDetailView,
                               TaskTypesListView,
                               TaskTypeDetailView)

urlpatterns = [
    path("", home, name="home"),
    path("projects/", ProjectsListView.as_view(), name="projects-list"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("positions/", PositionsListView.as_view(), name="positions-list"),
    path("positions/<int:pk>", PositionDetailView.as_view(), name="position-detail"),
    path("teams/", TeamsListView.as_view(), name="teams-list"),
    path("team/<int:pk>", TeamDetailView.as_view(), name="team-detail"),
    path("tasks/", TasksListView.as_view(), name="tasks-list"),
    path("task/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("tasktypes/", TaskTypesListView.as_view(), name="task_types_list"),
    path("tasktype/<int:pk>", TaskTypeDetailView.as_view(), name="tasktype-detail")
]

app_name = "TaskManager"
