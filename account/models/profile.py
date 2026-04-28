from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()
# Create your models here.

class Profile(models.Model):
    class ExpertiseChoices(models.TextChoices):
        BACKEND = "backend", "Backend Developer"
        FRONTEND = "frontend", "Frontend Developer"
        FULLSTACK = "fullstack", "Fullstack Developer"
        MOBILE = "mobile", "Mobile Developer"
        DEVOPS = "devops", "DevOps Engineer"
        DATA = "data", "Data Engineer / Data Scientist"
        AI = "ai", "AI / Machine Learning Engineer"
        OTHER = "other", "Other"

    username = models.TextField(max_length=256,blank=True,null=True)
    bio = models.TextField(max_length=256,blank=True,null=True)
    prof_image = models.ImageField(upload_to="user_profile/", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    skills = models.ManyToManyField(
        "account.Skill",
        through="account.ProfileSkill",
        related_name="profiles",
        blank=True
    )
    expertise = models.CharField(
        max_length=50,
        choices=ExpertiseChoices.choices,
        default=ExpertiseChoices.OTHER
    )
    def __str__(self):
        if self.username:
            return self.username
        return "profile_name"