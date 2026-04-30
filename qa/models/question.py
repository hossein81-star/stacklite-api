from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Question(models.Model):
    title = models.CharField(max_length=200)
    question_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title
