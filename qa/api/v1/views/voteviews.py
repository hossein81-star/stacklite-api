from rest_framework import viewsets, request, serializers
from rest_framework.permissions import IsAuthenticated

from ....models.answer import Answer
from ....models.vote import Vote
from ....permissions import IsActivatedUser,IsAuthorUser
from ..serializers.vote_serializers import VoteSerializer
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import mixins, generics

# class VoteViewSet(viewsets.ModelViewSet):
#     queryset = Vote.objects.all()
#     serializer_class = VoteSerializer
#     permission_classes = [IsAuthenticated,IsActivatedUser]
#     def get_queryset(self,**kwargs):
#         queryset = self.queryset
#         answer_id=self.kwargs.get("answer_id")
#         return queryset.filter(answer_id=answer_id)
#     def perform_create(self, serializer, **kwargs):
#         answer_id=self.kwargs.get("answer_id")
#         serializer.save(user=self.request.user,answer=answer_id)

class VoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated,IsActivatedUser]
    def get_queryset(self,**kwargs):
        answer_id=self.kwargs.get("answer_id")
        return Vote.objects.filter(answer=answer_id)
    def perform_create(self, serializer):
        answer_id=self.kwargs.get("answer_id")
        answer=get_object_or_404(Answer,id=answer_id)
        if Vote.objects.filter(answer=answer,user=self.request.user).exists():
            raise serializers.ValidationError("Vote already exists")
        serializer.save(user=self.request.user,answer=answer)

class VoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated,IsActivatedUser,IsAuthorUser]



