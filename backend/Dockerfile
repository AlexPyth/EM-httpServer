FROM python:3.14.5-slim

WORKDIR /app

EXPOSE 8080/tcp

RUN useradd -r em-backend-user

USER em-backend-user

CMD ["python3", "app.py"]