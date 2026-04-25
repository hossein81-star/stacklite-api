from django.urls import path, include
from .views import RegisterAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),

]