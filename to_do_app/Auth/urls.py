from django.urls import path,include
from .views import *
from django.contrib.auth import forms, views as auth_views
urlpatterns = [
    path('',login,name ='user-login'),
    path('register/',register,name ='user-register'),
    path('logout/',logout,name ='user-logout'),
    path('home/',home,name ='home'),
    path('profile/',profile,name ='user-profile'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name ='auth/password_reset.html'),name ="password_reset"),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name ='auth/password_reset_done.html'),name ="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name ='auth/password_reset_confirm.html'),name ="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name ='auth/password_reset_complete.html'),name ="password_reset_complete"),
]
