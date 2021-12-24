from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('login/',views.loginView,name='login'),
    path('register/',views.registerView,name='register'),
    path('logout/',views.logoutView,name='logout'),
    path('otp/',views.otpVerifyView,name='otp_verify'),
    path('password_reset/', PasswordResetView.as_view(template_name='AccountsApp/password_reset.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='AccountsApp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="AccountsApp/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='AccountsApp/password_reset_complete.html'), name='password_reset_complete'),
]