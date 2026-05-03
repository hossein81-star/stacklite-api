from rest_framework import serializers
from ....models.answer import Answer


class AnswerSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    question=serializers.StringRelatedField(read_only=True)
    score = serializers.IntegerField(read_only=True)
    class Meta:
        model = Answer
        fields = ("id","content", "question", "user", "created_at", "updated_at", "score")

    def validate_content(self, value):
        qs = Answer.objects.filter(content=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError("Answer already exists")

        return value
