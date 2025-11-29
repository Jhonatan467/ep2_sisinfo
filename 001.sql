-- 1) Posts ordenados por data
SELECT id, title, created_at
FROM blog_post
ORDER BY created_at DESC;

-- 2) Comentários de um post
SELECT id, author_id, text, created_at
FROM blog_comment
WHERE post_id = 1
ORDER BY created_at DESC;

-- 3) Comentários com dados do post
SELECT c.id, c.author_id, c.text, c.created_at, p.title, p.created_at AS post_date
FROM blog_comment AS c
JOIN blog_post AS p ON p.id = c.post_id
WHERE p.id = 1
ORDER BY c.created_at DESC;

-- 4) Posts de uma categoria
SELECT cat.id AS category_id, cat.name AS category_name, cat.description,
       post.id AS post_id, post.title, post.created_at
FROM blog_category AS cat
JOIN blog_post_categories AS pc ON pc.category_id = cat.id
JOIN blog_post AS post ON post.id = pc.post_id
WHERE cat.id = 2
ORDER BY post.created_at DESC;

-- 5) Categorias com 2 ou mais posts
SELECT cat.id, cat.name, COUNT(pc.post_id) AS total_posts
FROM blog_category AS cat
JOIN blog_post_categories AS pc ON pc.category_id = cat.id
GROUP BY cat.id, cat.name
HAVING COUNT(pc.post_id) >= 2
ORDER BY total_posts DESC;