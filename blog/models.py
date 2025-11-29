from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	categories = models.ManyToManyField("Category", related_name="posts", blank=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:
		return self.title

	def get_absolute_url(self) -> str:
		return reverse("post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=120, unique=True)
	description = models.TextField(blank=True)

	class Meta:
		ordering = ["name"]

	def __str__(self) -> str:
		return self.name

	def save(self, *args, **kwargs):
		if self.slug:
			self.slug = slugify(self.slug)
		else:
			base_slug = slugify(self.name) or "categoria"
			slug = base_slug
			index = 1
			while type(self).objects.filter(slug=slug).exclude(pk=self.pk).exists():
				index += 1
				slug = f"{base_slug}-{index}"
			self.slug = slug
		super().save(*args, **kwargs)

	def get_absolute_url(self) -> str:
		return reverse("category-detail", kwargs={"slug": self.slug})


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:
		return f"Comentario de {self.author} em {self.post}"
