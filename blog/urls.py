from django.urls import path

from .views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/novo/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/editar/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/remover/", PostDeleteView.as_view(), name="post-delete"),
]
