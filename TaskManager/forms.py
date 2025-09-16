from django.forms import ModelForm
from TaskManager.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"