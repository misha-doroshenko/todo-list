from django.urls import path
from django.views.i18n import JavaScriptCatalog

from app.views import TaskListView, TaskUpdateView, TaskCreateView, TaskDeleteView, complete_undo, TagListView, \
     TagUpdateView, TagCreateView, TagDeleteView

urlpatterns = [
     path("", TaskListView.as_view(), name="task-list"),
     path("jsi18n", JavaScriptCatalog.as_view(), name="js-catlog"),
     path("<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
     path("create/", TaskCreateView.as_view(), name="task-create"),
     path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
     path("<int:pk>/complete-undo", complete_undo, name="task-complete-undo"),
     path("tags/", TagListView.as_view(), name="tag-list"),
     path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
     path("tags/create/", TagCreateView.as_view(), name="tag-create"),
     path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "app"
