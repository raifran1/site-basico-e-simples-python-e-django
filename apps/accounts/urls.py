from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('novo-usuario/', views.add_user, name='add_user'),
    path('logout-usuario/', views.user_logout, name='user_logout'),
    path('login-usuario/', views.user_login, name='user_login'),
    path('alterar-senha/', views.change_password, name='change_password'),
    
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), 
        name='password_reset'),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), 
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), 
        name='password_reset_complete'),
]
