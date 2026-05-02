from django.urls import path, include
from ..views.voteviews import VoteListCreateAPIView, VoteDetailAPIView

urlpatterns = [
    path('answers/<int:answer_id>/votes/', VoteListCreateAPIView.as_view()),
    path('votes/<int:pk>/', VoteDetailAPIView.as_view()),
]
