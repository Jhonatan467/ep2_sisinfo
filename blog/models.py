from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:
		return self.title

	def get_absolute_url(self) -> str:
		return reverse("post-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:
		return f"Comentario de {self.author} em {self.post}"
