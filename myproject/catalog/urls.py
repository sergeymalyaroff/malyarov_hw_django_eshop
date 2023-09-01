from django.urls import path

# Здесь будут представления
from . import views  # импортируем все представления из приложения

urlpatterns = [
    path('', views.home, name='home'),  # Домашняя страница
    path('contact/', views.contact, name='contact'),  # Страница с контактной информацией
    path('product/<int:product_id>/', views.product_detail, name='product_detail'), # Страница продукта
]
