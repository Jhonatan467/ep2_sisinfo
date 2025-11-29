from django.urls import path

from .views import (
    CategoryDetailView,
    CategoryListView,
    CommentCreateView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("categorias/", CategoryListView.as_view(), name="category-list"),
    path("categorias/<slug:slug>/", CategoryDetailView.as_view(), name="category-detail"),
    path("post/novo/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/editar/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/remover/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/comentarios/novo/", CommentCreateView.as_view(), name="comment-create"),
]
