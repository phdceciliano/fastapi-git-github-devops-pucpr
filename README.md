📚 Guia Rápido de Git, GitHub e GitHub Desktop projeto

Este repositório foi criado para estudos e prática de versionamento de código utilizando Git, GitHub e GitHub Desktop.
O objetivo é servir como um manual de referência para lembrar os comandos e processos mais comuns no dia a dia de desenvolvimento.

📂 1. Criando um Repositório
Via GitHub (site)

Acesse sua conta no GitHub.

Clique em New Repository.

Defina nome, descrição e visibilidade (público/privado).

(Opcional) Adicione um README inicial e um .gitignore.

Clique em Create Repository.

Via GitHub Desktop

Abra o GitHub Desktop.

Vá em File → New Repository.

Escolha a pasta local, nome e descrição.

Clique em Create Repository.

🌱 2. Clonando um Repositório

Via Git (terminal):

git clone https://github.com/usuario/repositorio.git


Via GitHub Desktop:

File → Clone Repository

Cole a URL ou selecione da lista de repositórios.

Escolha a pasta local e clique em Clone.

🛠 3. Criando e Trocando de Branch

Criar branch:

git checkout -b nome-da-branch


Trocar para branch existente:

git checkout nome-da-branch


Via GitHub Desktop:

No canto superior, clique no seletor de branch.

Escolha New Branch ou selecione a desejada.

✏ 4. Alterando Código e Salvando Mudanças

Faça as alterações nos arquivos.

Verificar status:

git status


Adicionar arquivos:

git add .


Commitar mudanças:

git commit -m "Mensagem descritiva da alteração"


Via GitHub Desktop:

Modifique os arquivos no editor.

Veja as mudanças no painel lateral.

Escreva uma mensagem de commit e clique em Commit to branch.

📤 5. Enviando Alterações (Push)

Via Git:

git push origin nome-da-branch


Via GitHub Desktop:
Clique em Push origin no topo.

🔄 6. Recebendo Alterações (Pull)

Via Git:

git pull origin nome-da-branch


Via GitHub Desktop:
Clique em Fetch origin → Pull origin.

🔀 7. Criando um Pull Request (PR)

Vá ao repositório no GitHub.

Clique em Compare & Pull Request.

Descreva a mudança e envie para revisão.

🩹 8. Corrigindo Após um Pull Request

Volte para a branch do PR:

git checkout nome-da-branch


Faça as correções e commit normalmente.

Envie novamente:

git push origin nome-da-branch


O PR será atualizado automaticamente.

🗑 9. Excluindo Branch

Localmente:

git branch -d nome-da-branch


No GitHub (site):
Após o merge do PR, clique no botão Delete branch.

📌 10. Comandos Git Mais Usados
Comando	Função
git status	Mostra mudanças no repositório
git add .	Adiciona todos os arquivos modificados
git commit -m "mensagem"	Salva alterações localmente
git push origin branch	Envia alterações para o GitHub
git pull origin branch	Baixa alterações do GitHub
git checkout branch	Troca de branch
git merge branch	Mescla branch com a atual

Visual
📚 Guia Rápido – GitHub Desktop & GitHub

Este repositório foi criado para estudos e prática de versionamento utilizando GitHub Desktop (interface gráfica) e GitHub (web).
O objetivo é servir como um manual de referência para lembrar os principais processos no trabalho com branches, commits, pull requests e correções.

📂 1. Criando um Repositório
Pelo GitHub (site)

Acesse sua conta no GitHub.

Clique em New (ou New Repository).

Preencha:

Repository name → nome do repositório.

Description (opcional).

Visibility → Público ou Privado.

(Opcional) Marque:

✅ Add a README file

✅ .gitignore se quiser ignorar arquivos específicos.

Clique em Create Repository.

📥 2. Clonando no GitHub Desktop

Abra o GitHub Desktop.

Vá em File → Clone Repository.

Escolha:

URL → cole o link do repositório.

Ou Your repositories → selecione da sua conta.

Escolha a pasta local onde ficará o código.

Clique em Clone.

🌱 3. Criando e Mudando de Branch

No canto superior do GitHub Desktop, clique no seletor de branch.

Selecione New Branch.

Dê um nome descritivo (ex.: feature-login ou bugfix-layout).

Clique em Create branch.

Para trocar de branch, basta selecionar outra na lista.

✏ 4. Fazendo Alterações

Abra o projeto na sua IDE/editor e modifique os arquivos.

Volte para o GitHub Desktop.

Você verá as mudanças listadas no painel esquerdo.

💾 5. Salvando Alterações (Commit)

No campo Summary, escreva uma mensagem curta e clara sobre a mudança.

(Opcional) No campo Description, detalhe melhor a alteração.

Clique em Commit to [nome-da-branch].

📤 6. Enviando Alterações (Push)

Depois de fazer o commit, clique no botão Push origin (topo direito).

Isso enviará suas mudanças para o GitHub.

🔄 7. Recebendo Alterações (Pull)

Clique em Fetch origin para verificar se há mudanças.

Se houver, clique em Pull origin para atualizar seu repositório local.

🔀 8. Criando um Pull Request (PR)

Após fazer Push, abra o repositório no GitHub (site).

Se aparecer o botão Compare & Pull Request, clique nele.

Revise as alterações.

Escreva um título e descrição do PR.

Clique em Create Pull Request.

🩹 9. Corrigindo Após um PR

Volte no GitHub Desktop para a mesma branch do PR.

Faça as alterações necessárias.

Commit → Push origin.

O PR será atualizado automaticamente no GitHub.

🗑 10. Deletando Branch

No GitHub (site): após o merge, clique em Delete branch.

No GitHub Desktop: selecione a branch, vá em Branch → Delete.

📌 Dicas Importantes

Commits pequenos e frequentes ajudam no histórico e na revisão.

Antes de começar a trabalhar, sempre faça um Fetch/Pull para evitar conflitos.

Use nomes de branch claros e padronizados:

feature/ para novas funcionalidades.

bugfix/ para correções.

hotfix/ para correções urgentes.

💡 Resumo visual do fluxo no GitHub Desktop:

Fetch/Pull → Pega alterações.

Criar branch → Começar tarefa.

Editar código → Fazer mudanças.

Commit → Salvar localmente.

Push → Enviar para GitHub.

PR → Pedir revisão e merge.
