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
