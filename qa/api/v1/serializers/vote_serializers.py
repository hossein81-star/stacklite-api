from rest_framework import serializers

from ....models.vote import Vote


class VoteSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    answer=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Vote
        fields=["user","answer","vote_type","created_at"]
        read_only_fields = ["user","answer"]
