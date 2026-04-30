from rest_framework import serializers

from ....models.question import Question


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = ["title", "question_text", "user", "created_at", "updated_at"]

    def validate_question_text(self, value):
        qs = Question.objects.filter(question_text=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError("Question already exists")

        return value
