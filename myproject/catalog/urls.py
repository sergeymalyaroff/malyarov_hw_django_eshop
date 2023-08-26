from django.urls import path

# Здесь будут представления
from . import views  # импортируем все представления из приложения

urlpatterns = [
    path('', views.home, name='home'),  # Домашняя страница
    path('contact/', views.contact, name='contact'),  # Страница с контактной информацией
]

