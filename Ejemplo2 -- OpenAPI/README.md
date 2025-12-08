# Proyecto Inventario + FastMCP

Este proyecto integra un servicio de inventario desarrollado en Spring Boot (Java) y un servidor FastMCP (Python), ambos ejecutándose en un solo contenedor Docker. El servidor FastMCP se inicia utilizando la especificación OpenAPI generada por el servicio de inventario.

## Estructura del Proyecto

- `inventario/`: Servicio Spring Boot (Java, Maven)
- `server.py`: Servidor FastMCP (Python)
- `client.py`: Cliente FastMCP (opcional)
- `Dockerfile`: Imagen para construir y ejecutar ambos servicios

## Requisitos

- Docker instalado

## Construcción y Ejecución

1. **Construir la imagen Docker:**

   Abre una terminal en la raíz del proyecto y ejecuta:

   ```powershell
   docker build -t inventario-mcp .
   ```

2. **Ejecutar el contenedor:**

   ```powershell
   docker run -p 8001:8001 -p 8083:8083 inventario-mcp
   ```

   - El servicio Spring Boot estará disponible en `http://localhost:8083`
   - El servidor FastMCP estará disponible en `http://localhost:8001`
   