from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
	model = Post
	template_name = "blog/post_list.html"
	context_object_name = "posts"


class PostDetailView(DetailView):
	model = Post
	template_name = "blog/post_detail.html"
	context_object_name = "post"


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
