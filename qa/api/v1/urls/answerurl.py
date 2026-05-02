from  django.urls import path,include
from ..views.answersview import AnswerRetrieveUpdateDestroyAPIView,AnswerListCreateAPIView

urlpatterns = [
path(
        "questions/<int:qs_id>/answers/",
        AnswerListCreateAPIView.as_view(),
        name="answer-list-create"
    ),

    path(
        "answers/<int:pk>/",
        AnswerRetrieveUpdateDestroyAPIView.as_view(),
        name="answer-detail"
    ),
]