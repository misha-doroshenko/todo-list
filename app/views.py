from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app.forms import TaskForm
from app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").all()


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:task-list")


def complete_undo(request, pk):
    Task.objects.filter(id=pk).update(done=Q(done=False))
    return HttpResponseRedirect(reverse_lazy("app:task-list"))


class TagListView(generic.ListView):
    model = Tag
