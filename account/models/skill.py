from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Skill(models.Model):
    class Level(models.TextChoices):
        BEGINNER = "BEGINNER", "BEGINNER"
        INTERMEDIATE = "INTERMEDIATE", "INTERMEDIATE"
        ADVANCED = "ADVANCED", "ADVANCED"


    title = models.TextField(max_length=256)
    level = models.CharField(
        max_length=20,
        choices=Level.choices,
        default=Level.BEGINNER
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='skills')
    def __str__(self):
        return self.title
