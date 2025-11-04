from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PostForm
from .models import Post


def post_list(request):
	posts = Post.objects.all()
	return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, "blog/post_detail.html", {"post": post})


def post_create(request):
	form = PostForm(request.POST or None)

	if request.method == "POST" and form.is_valid():
		post = form.save()
		return redirect("post-detail", pk=post.pk)

	return render(
		request,
		"blog/post_form.html",
		{
			"form": form,
			"post": None,
			"form_action": reverse("post-create"),
			"submit_label": "Salvar",
		},
	)


def post_update(request, pk):
	post = get_object_or_404(Post, pk=pk)

	form = PostForm(request.POST or None, instance=post)

	if request.method == "POST" and form.is_valid():
		form.save()
		return redirect("post-detail", pk=post.pk)

	return render(
		request,
		"blog/post_form.html",
		{
			"form": form,
			"post": post,
			"form_action": reverse("post-update", kwargs={"pk": post.pk}),
			"submit_label": "Atualizar",
		},
	)


def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)

	if request.method == "POST":
		post.delete()
		return redirect("post-list")

	return render(request, "blog/post_confirm_delete.html", {"post": post})
