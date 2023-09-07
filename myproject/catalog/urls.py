
from django.urls import path
from .views import HomeView, ContactView, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .views import post_list_view


urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Домашняя страница
    path('contact/', ContactView.as_view(), name='contact'),  # Страница с контактной информацией
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'), # Страница продукта
    path('add_product/', ProductCreateView.as_view(), name='add_product'), # добавление продукта
    path('products/', ProductListView.as_view(), name='product_list'), # список продуктов
    # редактирование и удаление продуктов:
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'), # редактирование продукта
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'), # удаление продукта

    path('posts/', post_list_view, name='post_list'),
]
