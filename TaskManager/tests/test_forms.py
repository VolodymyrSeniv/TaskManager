from django.test import TestCase
from django.contrib.auth import get_user_model
from TaskManager.models import Position, Team, Project, TaskType, Tag, Task
from TaskManager.forms import (
    WorkerCreationForm,
    WorkerSearchForm,
    TagForm,
    TagSearchForm,
    ProjectForm,
    ProjectSearchForm,
    PositionForm,
    PositionSearchForm,
    TeamForm,
    TeamSearchForm,
    TaskForm,
    TaskSearchForm,
    TaskTypeForm,
    TaskTypeSearchForm,
)
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class FormsTestCase(TestCase):
    def setUp(self):
        # Create initial objects
        self.position = Position.objects.create(name="Manager", description="Manages tasks")
        self.user = User.objects.create_user(username="user1", password="pass", first_name="John", last_name="Doe", position=self.position)
        self.tag1 = Tag.objects.create(name="python")
        self.tag2 = Tag.objects.create(name="frontend")
        self.team = Team.objects.create(team_code="A1")
        self.team.workers.add(self.user)
        self.project = Project.objects.create(name="ProjectX", description="Test project")
        self.project.teams.add(self.team)
        self.task_type = TaskType.objects.create(name="Bug")
    
    def test_worker_creation_form_valid(self):
        form_data = {
            "username": "user2",
            "password1": "Complexpass123",
            "password2": "Complexpass123",
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice@example.com",
            "position": self.position.id,
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_worker_search_form(self):
        form = WorkerSearchForm(data={"first_name": "John"})
        self.assertTrue(form.is_valid())
    
    def test_tag_form_valid(self):
        form = TagForm(data={"name": "django"})
        self.assertTrue(form.is_valid())
    
    def test_tag_search_form(self):
        form = TagSearchForm(data={"name": "python"})
        self.assertTrue(form.is_valid())
    
    def test_project_form_valid(self):
        form_data = {"name": "NewProject", "description": "desc", "teams": [self.team.id]}
        form = ProjectForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_project_search_form(self):
        form = ProjectSearchForm(data={"name": "ProjectX"})
        self.assertTrue(form.is_valid())
    
    def test_position_form_valid(self):
        form_data = {"name": "Tester", "description": "Testing stuff"}
        form = PositionForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_position_search_form(self):
        form = PositionSearchForm(data={"name": "Manager"})
        self.assertTrue(form.is_valid())
    
    def test_team_form_valid(self):
        form_data = {"team_code": "B2", "workers": [self.user.id]}
        form = TeamForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_team_search_form(self):
        form = TeamSearchForm(data={"team_code": "A1"})
        self.assertTrue(form.is_valid())
    
    def test_task_form_valid(self):
        future_date = (timezone.now() + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M")
        form_data = {
            "name": "Fix bug",
            "description": "Fix critical bug",
            "deadline": future_date,
            "priority": "High",
            "task_type": self.task_type.id,
            "project": self.project.id,
            "assignees": [self.user.id],
            "tags": [self.tag1.id, self.tag2.id],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_task_search_form(self):
        form = TaskSearchForm(data={"query": "Fix bug"})
        self.assertTrue(form.is_valid())
    
    def test_tasktype_form_valid(self):
        form = TaskTypeForm(data={"name": "Feature"})
        self.assertTrue(form.is_valid())
    
    def test_tasktype_search_form(self):
        form = TaskTypeSearchForm(data={"name": "Bug"})
        self.assertTrue(form.is_valid())
