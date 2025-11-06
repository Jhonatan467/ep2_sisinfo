from django import forms
from django.utils import timezone

from .models import Comment, Post


class PostForm(forms.ModelForm):
    created_at = forms.DateTimeField(
        label="Data de publicação",
        widget=forms.DateTimeInput(
            attrs={"class": "form-control", "type": "datetime-local"},
            format="%Y-%m-%dT%H:%M",
        ),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    class Meta:
        model = Post
        fields = ["title", "content", "created_at"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 8}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_tz = timezone.get_current_timezone()
        if self.instance and self.instance.pk and "created_at" not in self.initial:
            self.initial["created_at"] = timezone.localtime(self.instance.created_at, current_tz).strftime("%Y-%m-%dT%H:%M")
        elif "created_at" not in self.initial:
            self.initial["created_at"] = timezone.localtime(timezone.now(), current_tz).strftime("%Y-%m-%dT%H:%M")

    def clean_created_at(self):
        created_at = self.cleaned_data["created_at"]
        if timezone.is_naive(created_at):
            return timezone.make_aware(created_at, timezone.get_current_timezone())
        return created_at


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        labels = {"text": "Comentário"}
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Escreva seu comentário"
                }
            )
        }
