# Listagem do arquivo `blog/views.py`

Inclua esta listagem na seção de resultados do PDF. Caso prefira, exporte diretamente do editor e cole como anexo. Segue a versão atual completa:

```
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CommentForm, PostForm
from .models import Category, Comment, Post


class PostListView(ListView):
	model = Post
	template_name = "blog/post_list.html"
	context_object_name = "posts"

	def get_queryset(self):
		return super().get_queryset().prefetch_related("categories")


class PostDetailView(DetailView):
	model = Post
	template_name = "blog/post_detail.html"
	context_object_name = "post"

	def get_queryset(self):
		return super().get_queryset().prefetch_related("categories")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["comments"] = self.object.comments.select_related("author")
		context["comment_form"] = CommentForm()
		return context


class CategoryListView(ListView):
	model = Category
	template_name = "blog/category_list.html"
	context_object_name = "categories"

	def get_queryset(self):
		return Category.objects.annotate(post_count=Count("posts")).order_by("name")


class CategoryDetailView(DetailView):
	model = Category
	template_name = "blog/post_list.html"
	context_object_name = "category"
	slug_field = "slug"
	slug_url_kwarg = "slug"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["posts"] = self.object.posts.prefetch_related("categories").all()
		context["is_category_view"] = True
		return context


class PostCreateView(CreateView):
	model = Post
	form_class = PostForm
	template_name = "blog/post_form.html"


class PostUpdateView(UpdateView):
	model = Post
	form_class = PostForm
	template_name = "blog/post_form.html"


class PostDeleteView(DeleteView):
	model = Post
	template_name = "blog/post_confirm_delete.html"
	success_url = reverse_lazy("post-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	form_class = CommentForm
	template_name = "blog/comment_form.html"
	login_url = "admin:login"

	def get_post(self) -> Post:
		return get_object_or_404(Post, pk=self.kwargs["pk"])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["post"] = self.get_post()
		return context

	def form_valid(self, form):
		form.instance.post = self.get_post()
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.get_post().get_absolute_url()
```
