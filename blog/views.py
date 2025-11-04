from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .models import Post


def post_list(request):
	posts = Post.objects.all()
	return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, "blog/post_detail.html", {"post": post})


def post_create(request):
	if request.method == "POST":
		title = request.POST.get("title", "").strip()
		content = request.POST.get("content", "").strip()
		created_at_raw = request.POST.get("created_at")

		if created_at_raw:
			try:
				created_at = timezone.datetime.fromisoformat(created_at_raw)
				if timezone.is_naive(created_at):
					created_at = timezone.make_aware(created_at, timezone.get_current_timezone())
			except ValueError:
				created_at = timezone.now()
		else:
			created_at = timezone.now()

		post = Post.objects.create(title=title, content=content, created_at=created_at)
		return redirect("post-detail", pk=post.pk)

	default_created_at = timezone.localtime(timezone.now()).strftime("%Y-%m-%dT%H:%M")
	return render(
		request,
		"blog/post_form.html",
		{
			"form_action": reverse("post-create"),
			"submit_label": "Salvar",
			"post": None,
			"default_created_at": default_created_at,
		},
	)


def post_update(request, pk):
	post = get_object_or_404(Post, pk=pk)

	if request.method == "POST":
		post.title = request.POST.get("title", "").strip()
		post.content = request.POST.get("content", "").strip()
		created_at_raw = request.POST.get("created_at")

		if created_at_raw:
			try:
				created_at = timezone.datetime.fromisoformat(created_at_raw)
				if timezone.is_naive(created_at):
					created_at = timezone.make_aware(created_at, timezone.get_current_timezone())
				post.created_at = created_at
			except ValueError:
				pass

		post.save()
		return redirect("post-detail", pk=post.pk)

	default_created_at = timezone.localtime(post.created_at).strftime("%Y-%m-%dT%H:%M")
	return render(
		request,
		"blog/post_form.html",
		{
			"form_action": reverse("post-update", kwargs={"pk": post.pk}),
			"submit_label": "Atualizar",
			"post": post,
			"default_created_at": default_created_at,
		},
	)


def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)

	if request.method == "POST":
		post.delete()
		return redirect("post-list")

	return render(request, "blog/post_confirm_delete.html", {"post": post})
