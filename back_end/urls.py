from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("task_manager/", include("TaskManager.urls", namespace="task_manager")),
    path("accounts/", include("django.contrib.auth.urls"))
]
