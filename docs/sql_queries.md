# Consultas SQL obrigatórias

As consultas abaixo utilizam os nomes reais das tabelas geradas pelo Django (`blog_post`, `blog_comment`, `blog_category` e a tabela intermediária `blog_post_categories`). Execute-as no `db.sqlite3` após popular o banco com o comando `python manage.py seed_demo_data`.

Para cada consulta:
1. Execute no DB Browser for SQLite ou na extensão SQLite do VS Code.
2. Capture um print do resultado e inclua a imagem na seção de Resultados do relatório.
3. Mencione a consulta correspondente no texto do relatório.

---

## 1. Todos os posts ordenados do mais recente para o mais antigo
```sql
SELECT id,
       title,
       created_at,
       content
FROM blog_post
ORDER BY created_at DESC;
```

## 2. Comentários de um post específico
Substitua `:post_title` pelo título escolhido ou adapte usando o `post_id`.
```sql
SELECT c.id,
       c.author_id,
       c.text,
       c.created_at
FROM blog_comment AS c
JOIN blog_post AS p ON p.id = c.post_id
WHERE p.title = 'Guia rápido: CRUD com Django'
ORDER BY c.created_at DESC;
```

## 3. Comentários + título e data do post (renomeada para `post_date`)
```sql
SELECT c.id,
       c.author_id,
       c.text,
       c.created_at,
       p.title,
       p.created_at AS post_date
FROM blog_comment AS c
JOIN blog_post AS p ON p.id = c.post_id
WHERE p.title = 'Produtividade para devs em 2025'
ORDER BY c.created_at DESC;
```

## 4. Posts de uma categoria (todas as colunas de categoria e de post)
```sql
SELECT c.id           AS category_id,
       c.name         AS category_name,
       c.slug,
       c.description,
       p.id           AS post_id,
       p.title,
       p.content,
       p.created_at
FROM blog_category AS c
JOIN blog_post_categories AS pc ON pc.category_id = c.id
JOIN blog_post AS p ON p.id = pc.post_id
WHERE c.name = 'Django'
ORDER BY p.created_at DESC;
```

## 5. Categorias com dois ou mais posts associados
```sql
SELECT c.id,
       c.name,
       COUNT(pc.post_id) AS post_count
FROM blog_category AS c
JOIN blog_post_categories AS pc ON pc.category_id = c.id
GROUP BY c.id, c.name
HAVING COUNT(pc.post_id) >= 2
ORDER BY c.name;
```

> 💡 Dica: use os mesmos inputs ao capturar os prints para que os resultados correspondam ao conteúdo do relatório.
