from rest_framework import serializers

from ....models.question import Question

class QuestionSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:

        model = Question
        fields = ["title","question_text","user","created_at","updated_at"]