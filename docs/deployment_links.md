# Links de publicação

Registre estes links no relatório (ou nos comentários do Moodle) assim que concluir as etapas.

1. **Repositório GitHub**
   1. Abra https://github.com/new e crie um repositório público (ex.: `labblog`).
   2. No seu terminal PowerShell, execute:
      ```powershell
      cd C:\Users\Jhonatan\Desktop\ep2_sisinfo
      git init
      git add .
      git commit -m "Entrega completa do LabBlog"
      git branch -M master
      git remote add origin https://github.com/<usuario>/<repo>.git
      git push -u origin master
      ```
      > Ajuste `<usuario>` e `<repo>` para o nome escolhido. Se já existe `.git`, apenas configure o remoto e dê push.
   3. Faça push também das branches auxiliares (se ainda existirem):
      ```powershell
      git push origin comments
      git push origin categories
      ```
   4. Copie o link final: `https://github.com/<usuario>/<repo>` e inclua no PDF/comentário do Moodle.

2. **Deploy no Render**
   - Crie um novo Web Service a partir do repositório GitHub.
   - Build command sugerido: `pip install -r requirements.txt`.
   - Start command: `python manage.py runserver 0.0.0.0:$PORT`.
   - Configure a variável `PYTHON_VERSION` se necessário (3.11).
   - **Link a informar:** `https://<nome-do-servico>.onrender.com`.

3. **Seção do relatório**
   - Inclua um parágrafo com os dois links.
   - Alternativamente, insira os mesmos links nos comentários da entrega no Moodle.

> Você pode reutilizar este arquivo como referência ao preencher o PDF.
