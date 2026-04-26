from django.urls import path, include
from .views import (RegisterAPI,CustomObtainAuthToke,UserLogOutAPI,ChangePasswordAPI)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),



    path('jwt_create/', CustomObtainAuthToke.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #logout
    path("user_logout",UserLogOutAPI.as_view(), name='user_logout'),
    path("change_password/",ChangePasswordAPI.as_view(),name='change_password'),

]