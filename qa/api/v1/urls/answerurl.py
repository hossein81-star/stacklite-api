from  django.urls import path,include
from ..views.answersview import AnswerRetrieveUpdateDestroyAPIView,AnswerListCreateAPIView

urlpatterns = [
path(
        "questions/<int:qs_id>/answers/",
        AnswerListCreateAPIView.as_view(),
        name="answer-list-create"
    ),

    path(
        "questions/<int:qs_id>/answers/<int:answer_id>/",
        AnswerRetrieveUpdateDestroyAPIView.as_view(),
        name="answer-detail"
    ),
]