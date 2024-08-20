from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="position_name"
        )

        # Adding unique related_name attributes to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="taskmanager_workers",  # Unique related_name to avoid clashes
        blank=True,
        help_text="The groups this user belongs to.",
        related_query_name="worker",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="taskmanager_worker_permissions",  # Unique related_name to avoid clashes
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="worker",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f"{self.name}"


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
                                  related_name="tasktype_name")
    assignees = models.ManyToManyField(Worker, related_name="assignees_name")

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f"{self.name} - {self.priority}. {self.is_completed} : {self.assignees}"
