import datetime

from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.core.exceptions import ValidationError
from django.utils import timezone

from app.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    deadline = forms.SplitDateTimeField(required=False, widget=AdminSplitDateTime())

    def clean(self):
        if self.cleaned_data["deadline"]:
            now = timezone.now()
            if Task.objects.filter(content=self.cleaned_data["content"]).count():
                task = Task.objects.get(content=self.cleaned_data["content"])
                if task.created_at > self.cleaned_data["deadline"]:
                    raise ValidationError("Deadline must be later than time the task was created")
                if now > self.cleaned_data["deadline"]:
                    raise ValidationError("You can't create a task with overdue deadline")
            elif now > self.cleaned_data["deadline"]:
                raise ValidationError("You can't create a task with overdue deadline")

        return super(TaskForm, self).clean()

    class Meta:
        model = Task
        fields = "__all__"
