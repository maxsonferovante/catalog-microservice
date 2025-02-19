# Use a imagem base do Python
FROM python:3.12

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de definição de dependências (pyproject.toml) e o arquivo de bloqueio de dependências (poetry.lock) para o diretório de trabalho
COPY pyproject.toml poetry.lock /app/

# Instala o Poetry
RUN pip install poetry

# Instala as dependências do projeto usando o Poetry
RUN poetry install --no-root --no-cache
# Copia o restante do código fonte para o diretório de trabalho

# ENV DB_ENGINE='mysql+pymysql'
# ENV DB_NAME='catalog'
# ENV DB_USER='root'
# ENV DB_PASSWORD='root'
# ENV DB_HOST='localhost'
# ENV DB_PORT='3306'
# ENV DB_SCHEMA='catalog'

# ENV BIND_HOST_PORT='0.0.0.0:8000'
# ENV NUM_WORKERS=2


# ENV MESSAGE_BROKER_HOST = 'localhost'
# ENV MESSAGE_BROKER_PORT = '9092'
# ENV MESSAGE_BROKER_TOPIC = 'catalog'

COPY . .

EXPOSE 8000
# Define o comando padrão para executar a aplicação
# CMD ["poetry", "run", "python", "main.py"]
