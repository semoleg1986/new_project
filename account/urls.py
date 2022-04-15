from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm, PasswordChangingForm, PasswordResetingForm, UserSetPasswordForm


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.welcome, name='welcome'),
    # Шаблоны для доступа к обработчикам смены пароля.
    path('password_change/', auth_views.PasswordChangeView.as_view(form_class=PasswordChangingForm), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # Обработчики восстановления пароля.
    path('password_reset/',auth_views.PasswordResetView.as_view(form_class=PasswordResetingForm),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class=UserSetPasswordForm),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),  name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),    
]
