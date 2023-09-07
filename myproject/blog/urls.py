from django.urls import path
from . import views

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/<slug:slug>/edit/', views.blog_update, name='blog_update'),
    path('blog/<slug:slug>/delete/', views.blog_delete, name='blog_delete'),

    path('', PostListView.as_view(), name='post_list'),  # Список статей
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Детальное представление статьи
    path('create/', PostCreateView.as_view(), name='post_create'),  # Создание статьи
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  # Редактирование статьи
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Удаление статьи
]

