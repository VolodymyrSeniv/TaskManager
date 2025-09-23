from django.test import TestCase
from TaskManager.models import (Project,
                                Position,
                                TaskType,
                                Task,
                                Tag,
                                Team)
from django.contrib.auth import get_user_model
from django.utils import timezone



class ModelsTests(TestCase):
    def test_position_str(self):
        position = Position.objects.create(name="Manager")
        self.assertEqual(str(position), "Manager")

    def test_worker_str(self):
        position = Position.objects.create(name="Developer")
        worker = get_user_model().objects.create_user(
            username="john",
            first_name="John",
            last_name="Doe",
            password="password",
            position=position
        )
        self.assertEqual(str(worker), "John Doe")

    def test_tasktype_str(self):
        task_type = TaskType.objects.create(name="Bug")
        self.assertEqual(str(task_type), "Bug")

    def test_team_str(self):
        team = Team.objects.create(team_code="T001")
        self.assertEqual(str(team), "T001")

    def test_project_str(self):
        project = Project.objects.create(name="Website", description="New website project")
        self.assertEqual(str(project), "Website")

    def test_tag_str(self):
        tag = Tag.objects.create(name="Landing Page")
        self.assertEqual(str(tag), "Landing Page")

    def test_task_str(self):
        task_type = TaskType.objects.create(name="Feature")
        project = Project.objects.create(name="App", description="Mobile App Project")
        tag = Tag.objects.create(name="Python")
        worker = get_user_model().objects.create_user(username="alice", first_name="Alice", last_name="Smith", password="pass")
        task = Task.objects.create(
            name="Build API",
            description="Create API endpoints",
            deadline=timezone.now() + timezone.timedelta(days=1),
            priority="High",
            task_type=task_type,
            project=project,
        )
        task.assignees.add(worker)
        task.tags.add(tag)

        expected_str_start = "Build API - High. False :"
        self.assertTrue(str(task).startswith(expected_str_start))
    
