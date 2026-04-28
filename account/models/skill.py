from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.title


class ProfileSkill(models.Model):

    class Level(models.TextChoices):
        BEGINNER = "BEGINNER", "Beginner"
        INTERMEDIATE = "INTERMEDIATE", "Intermediate"
        ADVANCED = "ADVANCED", "Advanced"

    profile = models.ForeignKey(
        "account.Profile",
        on_delete=models.CASCADE,
        related_name="profile_skills"
    )

    skill = models.ForeignKey(
        "account.Skill",
        on_delete=models.CASCADE,
        related_name="skill_profiles"
    )

    level = models.CharField(
        max_length=20,
        choices=Level.choices,
        default=Level.BEGINNER
    )

    class Meta:
        unique_together = ("profile", "skill")

    def __str__(self):
        return f"{self.profile} - {self.skill} ({self.level})"
