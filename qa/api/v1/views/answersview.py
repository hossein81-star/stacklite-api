from rest_framework import viewsets, request
from rest_framework.permissions import IsAuthenticated

from ..serializers.answer_serializers import AnswerSerializer
from ....models.answer import Answer
from rest_framework.filters import SearchFilter
from ....permissions import IsActivatedUser,IsAuthorUser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import mixins, generics

class AnswerListCreateAPIView(generics.ListCreateAPIView):
   permission_classes = [IsAuthenticated,IsActivatedUser]
   serializer_class = AnswerSerializer
   queryset = Answer.objects.all()
   def get_queryset(self):
       qs_id=self.kwargs.get('qs_id')
       answers=self.queryset.filter(question_id=qs_id)
       return answers
   def perform_create(self, serializer, **kwargs):
       qs_id = self.kwargs.get('qs_id')
       serializer.save(question_id=qs_id,user=self.request.user)

class AnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsActivatedUser,IsAuthorUser]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    lookup_field = 'pk'
    def get_object(self):
        questions_id=self.kwargs.get('qs_id')
        answer_id=self.kwargs.get('answer_id')
        answer=get_object_or_404(self.queryset,pk=answer_id,question_id=questions_id)
        return answer

