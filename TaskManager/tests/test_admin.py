from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from TaskManager.models import Position
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin"
        )
        self.client.force_login(self.admin_user)
        self.worker = get_user_model().objects.create_user(
            username="worker1",
            password="worker1",
            position = Position.objects.create(name="testname",
                                               description="testDescription")
        )
    
    def test_worker_position_listed(self):
        url = reverse("admin:TaskManager_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)
    
    def test_worker_detailed_position_listed(self):
        url = reverse("admin:TaskManager_worker_change", args=[self.worker.id])
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)