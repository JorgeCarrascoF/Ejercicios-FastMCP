# Acceso desde Copilot a Servidor MCP

Este proyecto permite conectarse a un servidor MCP local usando transporte SSE y realizar consultas de prueba para herramientas, recursos y prompts.

## Requisitos previos
- Tener el servidor MCP corriendo localmente en `http://localhost:8000/sse`.

## Configuración de conexión
El archivo `.vscode/mcp.json` ya está configurado para conectarse al servidor local:

```json
{
  "servers": {
    "local-mcp": {
      "type": "sse",
      "url": "http://localhost:8000/sse"
    }
  }
}
```

El siguiente paso es seleccionar la opción START que aparece encima de "local-mcp".
El estado debería cambiar a Running y mostrar la cantidad de tools y prompts disponibles.

Abrir un agente con Control + Alt + I. Preguntar algo usando las herramientas, recursos o prompts disponibles.

## Consultas de prueba

Las consultas de prueba se encuentran en el archivo consultas_mcp.md.