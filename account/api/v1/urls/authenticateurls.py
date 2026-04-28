from django.urls import path, include
from ..views.authenticateviews  import  (RegisterAPI, CustomObtainAuthToke, UserLogOutAPI, ChangePasswordAPI, ResetPasswordAPI,
                    PasswordResetConfirmView, ActivationsApi, ActivationResendApi,ProfileView)
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
    #reset password
    path("reset_password/",ResetPasswordAPI.as_view(),name='reset_password'),
    path(
        "password-reset-confirm/<uid>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),
    # activations
    # path("activation/confirm/<str:token>",ActivationsApi.as_view(),name="activation_confirm"),
    path("activation/confirm/<path:token>/", ActivationsApi.as_view(), name="activation_confirm"),
    path('activation/resend/', ActivationResendApi.as_view(), name="activation_resend"),

    #profile
    path("user_profile/",ProfileView.as_view(),name="user_profile"),

]