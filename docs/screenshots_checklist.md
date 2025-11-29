# Capturas de tela obrigatórias (para inserir no PDF)

Use o comando `python manage.py seed_demo_data` antes de tirar as capturas para garantir que existam posts, categorias e comentários.

1. **Página individual de post com categorias**
   - URL: `http://127.0.0.1:8000/post/<id>/` (ex.: `post/1/`).
   - Verifique se os badges de categoria aparecem logo abaixo do título. Certifique-se de que o post possua múltiplas categorias (ex.: "Guia rápido: CRUD com Django").
   - Mostre também a seção de comentários logo abaixo.

2. **Página individual de categoria**
   - URL: `http://127.0.0.1:8000/categorias/<slug>/` (ex.: `categorias/django/`).
   - Essa página reutiliza `post_list.html`, então o título deve estar como "Posts em <Categoria>".
   - Inclua na captura a lista de posts pertencentes à categoria.

3. **Outras capturas já exigidas anteriormente**
   - Listagem geral de posts (`/`).
   - Páginas de criação, edição e confirmação de remoção de post.
   - Página de criação de comentário (link "Adicionar comentário").

> Dica: mantenha o navegador em 100% de zoom e clique em "Salvar como" ou use a ferramenta de recorte do sistema operacional para gerar imagens limpas para o PDF.
