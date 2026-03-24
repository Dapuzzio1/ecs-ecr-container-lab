FROM python:3.11-slim

RUN apt-get update && apt-get install -y nginx

WORKDIR /app

COPY app.py .
COPY app2.py .
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD service nginx start && python3 app.py & python3 app2.py
