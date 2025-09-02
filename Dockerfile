# Usa a imagem oficial do Python
FROM python:3

# Define o diretório de trabalho no container
WORKDIR /usr/src/app

# Copia os arquivos de requisitos primeiro (para aproveitar o cache do Docker)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação
COPY . .

# Expõe a porta que a aplicação vai rodar
EXPOSE 80

# Comando para executar a aplicação
CMD ["uvicorn", "main:app", "fastapi", "run", "main.py", "--port", "80"]
