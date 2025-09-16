from django.forms import ModelForm
from TaskManager.models import (Project,
                                Position,
                                Team,
                                Task,)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = "__all__"


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields= "__all__"