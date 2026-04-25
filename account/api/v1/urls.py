from django.urls import path, include
from .views import (RegisterAPI,CustomObtainAuthToke)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),

    path('api-auth/', include('rest_framework.urls')),

    path('jwt_create/', CustomObtainAuthToke.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]