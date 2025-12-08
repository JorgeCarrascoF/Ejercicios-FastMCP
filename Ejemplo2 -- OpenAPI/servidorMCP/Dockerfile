# Dockerfile para el servidor MCP (Python)
FROM python:3.11-slim

WORKDIR /app

COPY . /app

# Instala dependencias si existe requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
    
EXPOSE 8001

CMD ["python", "server.py", "--port", "8001"]
