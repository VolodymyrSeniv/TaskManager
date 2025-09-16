from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from back_end.settings import AUTH_USER_MODEL
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, default="0")

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("TaskManager:position-detail", args=[str(self.id)])


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="position_name",
        null=True,
        blank=True,
        )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("TaskManager:tasktype-detail", args=[str(self.id)])

    

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("TaskManager:project-detail", args=[str(self.id)])



class Team(models.Model):
    team_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    workers = models.ManyToManyField(Worker,
                                     related_name="workers_name")
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name="project_team")

    def __str__(self):
        return f"{self.team_code} - {self.project.name}"

    def get_absolute_url(self):
        return reverse("TaskManager:team-detail", args=[str(self.id)])



class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Urgent', 'Urgent'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10,
                                choices=PRIORITY_CHOICES,
                                default="Medium")
    task_type = models.ForeignKey(TaskType,
                                  on_delete=models.CASCADE,
                                  related_name="tasktype_task")
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name="project_task",
                                blank=True,
                                null=True)
    assignees = models.ManyToManyField(AUTH_USER_MODEL, related_name="assignees_task")


    class Meta:
        ordering = ["priority"]


    def __str__(self):
        return f"{self.name} - {self.priority}. {self.is_completed} : {self.assignees}"
    
    def get_absolute_url(self):
        return reverse("TaskManager:task-detail", args=[str(self.id)])

