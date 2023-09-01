from django.urls import path

# Здесь будут представления
from . import views  # импортируем все представления из приложения

urlpatterns = [
    path('', views.home, name='home'),  # Домашняя страница
    path('contact/', views.contact, name='contact'),  # Страница с контактной информацией
    path('product/<int:product_id>/', views.product_detail, name='product_detail'), # Страница продукта
    path('add_product/', views.add_product, name='add_product'), # добавление продукта
    path('products/', views.product_list, name='product_list'), # список продуктов
]



