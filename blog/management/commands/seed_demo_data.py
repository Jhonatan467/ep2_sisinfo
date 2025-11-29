from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from blog.models import Category, Comment, Post


class Command(BaseCommand):
    help = "Populate the database with demo posts, categories, and comments for the lab assignment."

    def handle(self, *args, **options):
        User = get_user_model()

        categories_data = {
            "Django": "Tutoriais e novidades do framework Django.",
            "Tecnologia": "Cobertura ampla do universo de tecnologia.",
            "Carreira": "Dicas e histórias sobre desenvolvimento de carreira.",
        }

        categories = {}
        for name, description in categories_data.items():
            category, _created = Category.objects.get_or_create(
                name=name,
                defaults={"description": description},
            )
            if category.description != description:
                category.description = description
                category.save(update_fields=["description"])
            categories[name] = category

        posts_data = [
            {
                "title": "Guia rápido: CRUD com Django",
                "content": """<p>Neste guia mostramos como criar operações CRUD com as <strong>class-based views</strong>.</p>
<p>Inclui dicas de formulários, templates e rotas.</p>""",
                "created_at": timezone.now() - timezone.timedelta(days=5),
                "category_names": ["Django", "Tecnologia"],
                "has_comments": True,
            },
            {
                "title": "Produtividade para devs em 2025",
                "content": """<p>Ferramentas modernas, IA generativa e hábitos saudáveis.</p>
<ul><li>Automatize tarefas repetitivas.</li><li>Invista em testes e monitoramento.</li></ul>""",
                "created_at": timezone.now() - timezone.timedelta(days=3),
                "category_names": ["Tecnologia", "Carreira"],
                "has_comments": True,
            },
            {
                "title": "Checklist antes de publicar seu projeto",
                "content": """<p>Revise documentação, testes e monitoramento antes do deploy.</p>
<p>Não esqueça de conferir as variáveis de ambiente e fazer backup do banco.</p>""",
                "created_at": timezone.now() - timezone.timedelta(days=1),
                "category_names": ["Carreira"],
                "has_comments": False,
            },
        ]

        posts = {}
        for data in posts_data:
            post, _created = Post.objects.get_or_create(
                title=data["title"],
                defaults={
                    "content": data["content"],
                    "created_at": data["created_at"],
                },
            )
            if not _created:
                post.content = data["content"]
                post.created_at = data["created_at"]
                post.save(update_fields=["content", "created_at"])
            post.categories.set([categories[name] for name in data["category_names"]])
            posts[data["title"]] = post

        commenters = [
            {"username": "laura.dev", "email": "laura@example.com"},
            {"username": "mario.silva", "email": "mario@example.com"},
            {"username": "camila.writer", "email": "camila@example.com"},
        ]
        user_objects = []
        for commenter in commenters:
            user, _ = User.objects.get_or_create(
                username=commenter["username"],
                defaults={
                    "email": commenter["email"],
                    "is_active": True,
                },
            )
            if not user.password:
                user.set_password("labblog123")
                user.save(update_fields=["password"])
            user_objects.append(user)

        comments_content = {
            "Guia rápido: CRUD com Django": [
                "Excelente resumo! Já estou usando como referência.",
                "Adorei as dicas sobre formulários e validação.",
            ],
            "Produtividade para devs em 2025": [
                "A automação com IA tem salvado meu time.",
                "Inclua também a importância de pair programming!",
                "Gostei das sugestões de hábitos saudáveis.",
            ],
        }

        for title, texts in comments_content.items():
            post = posts[title]
            for idx, text in enumerate(texts):
                author = user_objects[idx % len(user_objects)]
                comment, created = Comment.objects.get_or_create(
                    post=post,
                    author=author,
                    text=text,
                )
                if created:
                    comment.created_at = timezone.now() - timezone.timedelta(hours=idx * 2)
                    comment.save(update_fields=["created_at"])

        self.stdout.write(self.style.SUCCESS("Demo data ready: 3 posts, 3 categories, comments populated."))
