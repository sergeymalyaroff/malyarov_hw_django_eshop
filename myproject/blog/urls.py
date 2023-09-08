from django.urls import path
from . import views

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blog'


urlpatterns = [

    path('', PostListView.as_view(), name='post_list'),  # Список статей
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Детальное представление статьи
    path('create/', PostCreateView.as_view(), name='post_form'),  # Создание статьи
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  # Редактирование статьи
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Удаление статьи


]

