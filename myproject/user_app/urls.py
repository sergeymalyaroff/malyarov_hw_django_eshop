# urls.py
from django.urls import path
from .views import CustomLoginView, SignUpView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),  # Добавить URL для регистрации
    path('accounts/', include('allauth.urls')), #URL-конфигурация allauth
]
