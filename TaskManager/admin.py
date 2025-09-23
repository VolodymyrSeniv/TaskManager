from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from TaskManager.models import (Position,
                                Worker,
                                TaskType,
                                Project,
                                Team,
                                Task,
                                Tag)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("position",)}),)
    list_filter = UserAdmin.list_filter + ("position", )
    search_fields = UserAdmin.search_fields + ("position", )
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("first_name",
                                                                                "last_name",
                                                                                "position",)}),)

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["team_code", ]
    search_fields = ["team_code",]


@admin.register(Tag)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name",]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "is_completed", "deadline", "priority", "project", "task_type"]
    search_fields = ["name",]
    list_filter = ["priority", "project", "is_completed", "task_type"]

