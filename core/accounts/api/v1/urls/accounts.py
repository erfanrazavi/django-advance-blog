from django.urls import path
from ..views import (
    RegistrationApiView,
    TestEmailApiView,
    ActivationApiView,
    ActivationResendApiView,
    ChangePasswordApiView,
    ResetPasswordApiView,
    ResetPasswordConfirmApiView,
    CustomAuthToken,
    CustomDiscardAuthToken,
    CustomTokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


urlpatterns = [
    # registration
    path("registration/", RegistrationApiView.as_view(), name="registration"),
    # activation
    path("test-email/", TestEmailApiView.as_view(), name="test-email"),
    path(
        "activation/confirm/<str:token>", ActivationApiView.as_view(), name="activation"
    ),
    # resend activation
    path(
        "activation/resend", ActivationResendApiView.as_view(), name="activation-resend"
    ),
    # change password
    path("change-password/", ChangePasswordApiView.as_view(), name="change-password"),
    # reset password
    path("reset-password/", ResetPasswordApiView.as_view(), name="reset-password"),
    path(
        "reset-password/confirm/<str:token>/",
        ResetPasswordConfirmApiView.as_view(),
        name="reset-password-confirm",
    ),
    # login token
    path("token/login/", CustomAuthToken.as_view(), name="token-login"),
    path("token/logout/", CustomDiscardAuthToken.as_view(), name="token-logout"),
    # login jwt
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
