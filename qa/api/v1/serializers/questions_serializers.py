from rest_framework import serializers

from ....models.question import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["title","question_text","user","created_at","updated_at"]