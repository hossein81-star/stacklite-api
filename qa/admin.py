from django.contrib import admin
from .models.question import Question
from .models.answer import Answer
from .models.vote import Vote

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "question_text", "user"]
    search_fields = ["title", "question_text"]
    readonly_fields = ["created_at", "updated_at"]

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
        ("Important Dates", {
            "fields": ("created_at", "updated_at")
        }),
    )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["content", "user"]
    search_fields = ["content"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Content", {
            "fields": ("content",)
        }),
        ("Question", {
            "fields": ("question",)
        }),
        ("Author", {
            "fields": ("user",)
        }),
        ("Important Dates", {
            "fields": ("created_at", "updated_at")
        }),
    )

@admin.register(Vote)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["answer", "user", "vote_type"]
    search_fields = ["answer", "user"]

    readonly_fields = ["created_at",]

    fieldsets = (
        ("User", {
            "fields": ("user",)
        }),
        ("Answer", {
            "fields": ("answer",)
        }),
        ("your Vote", {
            "fields": ("vote_type",)
        }),

        ("Important Dates", {
            "fields": ("created_at",)
        }),
    )
