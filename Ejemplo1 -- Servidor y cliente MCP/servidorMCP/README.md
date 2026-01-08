# README.md

# Servidor MCP

Este proyecto contiene un servidor MCP implementado en Python.

## Requisitos

- Python 3.8 o superior
- Docker (opcional, si deseas ejecutar el servidor en un contenedor)

## Instalación de dependencias

Si tu servidor requiere dependencias adicionales, instálalas usando:

```powershell
pip install -r requirements.txt
```

## Ejecución del servidor

### 1. Ejecutar directamente con Python

Abre una terminal en la carpeta del proyecto y ejecuta:

```powershell
python server.py
```

### 2. Ejecutar usando Docker

Si prefieres usar Docker, primero construye la imagen:

```powershell
docker build -t servidor-mcp .
```

Luego ejecuta el contenedor:

```powershell
docker run -p 8000:8000 servidor-mcp
```

Asegúrate de que el puerto que expone el servidor en `server.py` coincida con el mapeo de puertos en Docker.

## Archivos principales

- `server.py`: Código fuente del servidor MCP
- `Dockerfile`: Configuración para crear la imagen Docker
- `client.py`: Cliente de ejemplo para conectarse al servidor

## Notas

- Modifica los comandos según la configuración específica de tu servidor (puerto, dependencias, etc).
- Si tienes dudas, revisa los comentarios en el código fuente.
