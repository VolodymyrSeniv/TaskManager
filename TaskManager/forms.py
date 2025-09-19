from django.forms import (ModelForm,
                          ModelMultipleChoiceField,
                          CheckboxSelectMultiple, 
                          Select,
                          ModelChoiceField,
                          DateTimeInput,
                          CharField,
                          Form,
                          TextInput)
from TaskManager.models import (Project,
                                Position,
                                Team,
                                Task,
                                TaskType)
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("first_name",
                                                 "last_name",
                                                 "position",
                                                 "email")


class WorkerSearchForm(Form):
    first_name = CharField(max_length=255,
                            required=False,
                            label="",
                            widget=TextInput(
                                attrs={
                                    "placeholder": "search by first name"
                                }
                            )
                        )


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("name", "description", "teams")
    
    teams = ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        widget=CheckboxSelectMultiple,  
        required=False
    )


class ProjectSearchForm(Form):
    name = CharField(max_length=255,
                            required=False,
                            label="",
                            widget=TextInput(
                                attrs={
                                    "placeholder": "search by name"
                                }
                            )
                        )


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ("name", "description")


class PositionSearchForm(Form):
    name = CharField(max_length=255,
                            required=False,
                            label="",
                            widget=TextInput(
                                attrs={
                                    "placeholder": "search by name"
                                }
                            )
                        )


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ("team_code", "workers")
    
    workers = ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple, 
        required=False
    )


class TeamSearchForm(Form):
    team_code = CharField(max_length=255,
                            required=False,
                            label="",
                            widget=TextInput(
                                attrs={
                                    "placeholder": "search by team code"
                                }
                            )
                        )


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields= ("name",
                 "description",
                 "deadline",
                 "priority",
                 "task_type",
                 "project",
                 "assignees")
        widgets = {
            "deadline": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control"
                },
                format="%Y-%m-%dT%H:%M"
            ),
            "priority": Select(attrs={"class": "form-select"})
        }
    
    assignees = ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple,   # Or forms.SelectMultiple
        required=True
    )

    task_type = ModelChoiceField(
        queryset=TaskType.objects.all(),
        widget=Select(attrs={"class": "form-select"}),
        required=True
    )

    project = ModelChoiceField(
        queryset=Project.objects.all(),
        widget=Select(attrs={"class": "form-select"}),
        required=True
    )


class TaskSearchForm(Form):
    name = CharField(max_length=255,
                            required=False,
                            label="",
                            widget=TextInput(
                                attrs={
                                    "placeholder": "search by name"
                                }
                            )
                        )


class TaskTypeForm(ModelForm):
    class Meta:
        model = TaskType
        fields = "__all__"


class TaskTypeSearchForm(Form):
    name = CharField(max_length=255,
                            required=False,
                            label="",
                            widget=TextInput(
                                attrs={
                                    "placeholder": "search by name"
                                }
                            )
                        )
