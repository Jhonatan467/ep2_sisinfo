from django.contrib import admin

from .models import Category, Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "created_at")
	search_fields = ("title", "categories__name")
	ordering = ("-created_at",)
	filter_horizontal = ("categories",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ("post", "author", "created_at")
	search_fields = ("post__title", "author__username", "text")
	ordering = ("-created_at",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name", "slug")
	prepopulated_fields = {"slug": ("name",)}
	search_fields = ("name", "slug")
