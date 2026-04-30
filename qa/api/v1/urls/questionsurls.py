from django.urls import path,include
from rest_framework.routers import DefaultRouter


from ..views.questionsviews import QuestionViewSet

router = DefaultRouter()
router.register(r'questions',QuestionViewSet,basename='questions')

urlpatterns = router.urls


