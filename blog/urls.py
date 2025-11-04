from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_list, name="post-list"),
    path("post/novo/", views.post_create, name="post-create"),
    path("post/<int:pk>/", views.post_detail, name="post-detail"),
    path("post/<int:pk>/editar/", views.post_update, name="post-update"),
    path("post/<int:pk>/remover/", views.post_delete, name="post-delete"),
]
