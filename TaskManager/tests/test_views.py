from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from TaskManager.models import Task, TaskType, Project, Tag, Team
from django.utils import timezone
from datetime import timedelta


WORKER_URL = reverse("TaskManager:workers-list")
TASK_URL = reverse("TaskManager:tasks-list")


class PublicWorkerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(WORKER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTasksTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="testpassword"
        )
        self.manchik = get_user_model().objects.create_user(
            username="abobus",
            password="abobuspassword"
        )
        self.tasktype_1 = TaskType.objects.create(name="TestType_1")
        self.tasktype_2 = TaskType.objects.create(name="TestType_2")
        self.team_1 = Team.objects.create(team_code="team_name_1")
        self.team_1.workers.set([self.user])
        self.team_2 = Team.objects.create(team_code="team_name_2")
        self.team_2.workers.set([self.manchik])
        self.project_1 = Project.objects.create(name="testprojectname_1",
                                           description="tstdescription_1")
        self.project_1.teams.set([self.team_1, self.team_2])
        self.tag_1 = Tag.objects.create(name="TEsttag_1")
        self.tag_2 = Tag.objects.create(name="TEsttag_2")
        self.client.force_login(self.user)
    
    def test_retrieve_tasks(self):
        task_1 = Task.objects.create(
            name="testname",
            description="testdescription",
            deadline=timezone.now() + timedelta(days=7),
            is_completed=False,
            priority="Urgent",
            task_type=self.tasktype_1,
            project=self.project_1,
        )
        task_1.assignees.set([self.user, self.manchik])
        task_1.tags.set([self.tag_1, self.tag_2])
        task_2 = Task.objects.create(
            name="another_test_task",
            description="another_test_description",
            deadline=timezone.now() + timedelta(days=10),
            is_completed=False,
            priority="Medium",
            task_type=self.tasktype_2,
            project=self.project_1,
        )
        task_2.assignees.set([self.user, self.manchik])
        task_2.tags.set([self.tag_2])
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(list(response.context["tasks_list"]), list(tasks))
        self.assertTemplateUsed(response, "TaskManager/tasks_list.html")
