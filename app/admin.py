from django.contrib import admin

from app.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "deadline", "done")
    search_fields = ("content",)
    list_filter = ("content",)


admin.site.register(Tag)
