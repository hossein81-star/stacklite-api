from django.contrib import admin
from .models.question import Question
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "question_text","user"]
    search_fields = ["title", "question_text"]
    fieldsets = (
        ("Title", {
            "fields": ("title",)
        }),

        ("Content", {
            "fields": ("question_text",)
        }),
        ("Author", {
            "fields": ("user",)
        }),

    )
    add_fieldsets = (
        ("Title", {
            "fields": ("title",)
        }),

        ("Content", {
            "fields": ("question_text",)
        }),
        ("Author", {
            "fields": ("user",)
        }),
        ("Important Dates", {
            "fields": ("created_at", "updated_at")
        }),

    )
