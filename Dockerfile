# Use a imagem base do Python
FROM python:3.12

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de definição de dependências (pyproject.toml) e o arquivo de bloqueio de dependências (poetry.lock) para o diretório de trabalho
COPY pyproject.toml poetry.lock /app/

# Instala o Poetry
RUN pip install poetry

# Instala as dependências do projeto usando o Poetry
RUN poetry install --no-root --no-dev
# Copia o restante do código fonte para o diretório de trabalho
COPY . .

EXPOSE 5000
# Define o comando padrão para executar a aplicação
CMD ["poetry", "run", "python", "main.py"]