from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.skillviews import SkillViewSet,SkillListViewSet


router = DefaultRouter()
router.register(r'profile_skills', SkillViewSet,basename='profile_skills')
router.register(r'skills', SkillListViewSet,basename='skills')

urlpatterns = router.urls