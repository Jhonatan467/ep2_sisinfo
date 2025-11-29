# LabBlog (Segunda Entrega de Laboratório)

Aplicação Django que implementa um blog com operações CRUD, sistema de comentários e categorização de posts. Este repositório contempla as três etapas do enunciado e inclui um comando auxiliar para popular o banco com os dados mínimos exigidos na etapa de SQL.

## ✅ Funcionalidades principais
- CRUD completo de posts usando class-based views e templates Bootstrap simples.
- Sistema de comentários autenticados, exibidos do mais recente para o mais antigo.
- Categorias com listagem, página individual reutilizando o template de posts e badges clicáveis nos posts.
- Testes automatizados em `blog/tests.py` cobrindo operações essenciais de posts, comentários e categorias.

## 🚀 Como executar localmente
```powershell
# Ativar o ambiente virtual (já configurado)
& .\.venv\Scripts\Activate.ps1

# Aplicar migrações
python manage.py migrate

# Popular o banco com os dados exigidos no enunciado
python manage.py seed_demo_data

# Rodar os testes
python manage.py test

# Subir o servidor de desenvolvimento
python manage.py runserver
```

## 🗂️ Comando de seed
O comando `seed_demo_data` cria:
- 3 categorias (“Django”, “Tecnologia”, “Carreira”);
- 3 posts (dois com múltiplas categorias e comentários, um sem comentários);
- Usuários fictícios para assinar os comentários.

Isso garante a consistência dos dados antes de produzir as capturas de tela e executar as consultas SQL.

## 🧾 Consultas SQL
As cinco consultas exigidas na Parte 4 estão documentadas em `docs/sql_queries.md`, com instruções para execução e impressão dos resultados.

## 📸 Checklist de capturas para o relatório
1. **Parte 1** – Listagem de posts, página individual, criação, edição e confirmação de remoção.
2. **Parte 2** – Página de post com comentários e página de criação de comentário.
3. **Parte 3** – Página de post mostrando badges de categoria e página de categoria (usando `post_list.html`).
4. **Parte 4** – Screenshot de cada consulta SQL executada.

> Sugestão: use o comando de seed, abra o admin (`/admin`) para conferir os dados e, em seguida, capture todas as telas solicitadas.

## 🌐 Publicação
1. **GitHub** – Inicialize o repositório remoto e faça `git push origin master` (ou `main`). Inclua o histórico com os commits das três versões de views conforme solicitado.
2. **Render** – Crie um serviço web apontando para este repositório. Configure o build command `pip install -r requirements.txt` (ou `pip install django` se preferir) e o start command `python manage.py runserver 0.0.0.0:$PORT`. Após a publicação, copie o link público.
3. Informe os links de GitHub e Render no relatório ou nos comentários do Moodle.

## 📄 Relatório (PDF)
Estrutura sugerida:
- **Introdução / Objetivo / Metodologia** – Contextualize as etapas executadas.
- **Resultados** – Inclua:
  - Listagem do arquivo `blog/views.py` (ou prints das partes correspondentes) para cada etapa;
  - Capturas solicitadas acima;
  - Cópia das consultas SQL e os prints dos resultados.
- **Anexos** – Links de GitHub e Render.

Com isso, basta gerar o PDF, anexar o `db.sqlite3` preenchido e enviar no Moodle. Boa entrega! 🎉
