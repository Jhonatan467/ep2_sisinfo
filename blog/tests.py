from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from blog.models import Post


class PostViewsTests(TestCase):
	def setUp(self):
		self.post = Post.objects.create(
			title="Post de teste",
			content="<p>Conteúdo inicial.</p>",
			created_at=timezone.now() - timezone.timedelta(days=1),
		)

	def test_list_view_displays_posts(self):
		response = self.client.get(reverse("post-list"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "blog/post_list.html")
		self.assertContains(response, self.post.title)

	def test_detail_view_displays_post(self):
		response = self.client.get(reverse("post-detail", args=[self.post.pk]))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "blog/post_detail.html")
		self.assertContains(response, "Conteúdo inicial.", html=True)

	def test_detail_view_returns_404_for_missing_post(self):
		response = self.client.get(reverse("post-detail", args=[self.post.pk + 1]))
		self.assertEqual(response.status_code, 404)

	def test_create_view_creates_post(self):
		payload = {
			"title": "Novo post",
			"content": "<p>Texto criado via teste.</p>",
			"created_at": timezone.localtime(timezone.now()).strftime("%Y-%m-%dT%H:%M"),
		}
		response = self.client.post(reverse("post-create"), payload, follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Post.objects.count(), 2)
		self.assertTrue(Post.objects.filter(title="Novo post").exists())

	def test_update_view_updates_post(self):
		payload = {
			"title": "Post atualizado",
			"content": "<p>Conteúdo atualizado.</p>",
			"created_at": timezone.localtime(timezone.now()).strftime("%Y-%m-%dT%H:%M"),
		}
		response = self.client.post(reverse("post-update", args=[self.post.pk]), payload, follow=True)
		self.assertEqual(response.status_code, 200)
		self.post.refresh_from_db()
		self.assertEqual(self.post.title, "Post atualizado")

	def test_delete_view_removes_post(self):
		response = self.client.post(reverse("post-delete", args=[self.post.pk]), follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
		self.assertTemplateUsed(response, "blog/post_list.html")
