from rest_framework import viewsets, request
from rest_framework.permissions import IsAuthenticated
from ....permissions import IsActivatedUser,IsAuthorUser
from ..serializers.questions_serializers import QuestionSerializer
from ....models.question import Question
from rest_framework.filters import SearchFilter


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated,IsActivatedUser,IsAuthorUser]
    filter_backends = [SearchFilter]
    search_fields = ['question_text']
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
