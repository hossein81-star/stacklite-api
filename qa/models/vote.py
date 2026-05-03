from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Vote(models.Model):
    class VoteType(models.IntegerChoices):
        upvote = 1
        downvote = -1

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    answer = models.ForeignKey("qa.answer", on_delete=models.CASCADE, related_name='votes')
    vote_type = models.IntegerField(
        choices=VoteType.choices,
        default=VoteType.upvote
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "answer"],
                name="unique_user_answer_vote"
            )
        ]


