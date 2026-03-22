
FROM python:3.11

WORKDIR /app

COPY . .


CMD ["python", "main.py"]

FROM python:3.11

WORKDIR /app

COPY . .

CMD ["sh", "-c", "python main.py && tail -f /dev/null"]