# Usa imagem oficial do Python
FROM python:3.11

# Define pasta de trabalho
WORKDIR /app

# Copia todos os arquivos
COPY . .

# Comando que será executado
CMD ["python", "main.py"]

FROM python:3.11

WORKDIR /app

COPY . .

CMD ["sh", "-c", "python main.py && tail -f /dev/null"]