#urls.py

from django.urls import path, include
from .views import CustomLoginView, SignUpView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),  # Добавить URL для регистрации
    path('accounts/', include('allauth.urls')), #URL-конфигурация allauth
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
