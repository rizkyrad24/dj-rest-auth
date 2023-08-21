from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from accounts.views import GoogleLogin, redirectPasswordConfirm, redirectActivation
from dj_rest_auth.views import PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("reset/password/confirm/<str:uid>/<str:token>", redirectPasswordConfirm, name='password_reset_confirm'),
    path("dj-rest-auth/registration/account-confirm-email/<str:key>/", redirectActivation, name='account_email_verification_sent'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]