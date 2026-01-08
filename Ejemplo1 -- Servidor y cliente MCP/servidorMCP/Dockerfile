# Dockerfile para servidor MCP
FROM python:3.11-slim

WORKDIR /app

# Copia los archivos del proyecto
COPY . /app

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto por defecto
EXPOSE 8000

# Comando para lanzar el servidor
CMD ["python", "server.py"]
