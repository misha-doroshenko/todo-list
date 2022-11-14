from django.urls import path
from django.views.i18n import JavaScriptCatalog

from app.views import TaskListView, TaskUpdateView, TaskCreateView

urlpatterns = [
     path("", TaskListView.as_view(), name="task-list"),
     path("jsi18n", JavaScriptCatalog.as_view(), name="js-catlog"),
     path("<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
     path("create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "app"
