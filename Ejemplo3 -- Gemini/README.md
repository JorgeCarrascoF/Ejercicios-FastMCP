# Documentación sobre el uso de FastMCP

## Set-up inicial

Para poder iniciar el servidor, necesitamos utilizar la extensión Cline. Una vez en el menú de cline (barra a la izquierda), le damos a MCP servers (icono de una BD), hacemos click en "Remote Servers" -> "Edit Configuration" y copiamos este json.

``` json
{
  "mcpServers": {
    "ChatAOS": {
      "command": "C:\\Users\\ruben\\Desktop\\Universidad\\AOS\\FastMCP\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\ruben\\Desktop\\Universidad\\AOS\\FastMCP\\fast_mcp_ex_1.py"
      ]
    },
    "ChatAOS2": {
      "command": "C:\\Users\\ruben\\Desktop\\Universidad\\AOS\\FastMCP\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\ruben\\Desktop\\Universidad\\AOS\\FastMCP\\fast_mcp_ex_2.py"
      ]
    },
    "TextSintetizer": {
      "command": "C:\\Users\\ruben\\Desktop\\Universidad\\AOS\\FastMCP\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\ruben\\Desktop\\Universidad\\AOS\\FastMCP\\fast_mcp_ex_3.py"
      ]
    },
    "NASA_Analyzer": {
      "command": "C:\\Users\\ruben\\Desktop\\Universidad\\AOS\\FastMCP\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\ruben\\Desktop\\Universidad\\AOS\\FastMCP\\fast_mcp_ex_4.py"
      ]
    }
  }
}
```

## Uso

Para usarlo, simplemente confirma que los servidores MCP tienen el piloto en verde y ya puedes consultar al chatbot de Cursos Auto para que utilice tus servicios MCP.

## Tools

Existen varias tools entre todos los servidores.

### ChatAOS (fast_mcp_ex_1.py)

Este servidor contiene un único tool que se llama cuando se quiera saludar al usuario llamado greet_user()

### ChatAOS2 (fast_mcp_ex_2.py)

Este servidor tiene un tool que actúa de decodificador para un mensaje secreto, que consiste simplemente en invertir el orden de las letras de la frase tal que hola = aloh

### TextSintetizer (fast_mcp_ex_3.py)

Este servidor tiene dos tools. Uno permite leer un fichero, mientras que otro permite generar un pdf con el resumen realizado con la IA. De esta forma, ya no te cobrarán cada vez que quieras usarla para resumir los apuntes de AOS ni será limitadas por su incapacidad de generar artefactos de ese estilo.

### NASA-Quality-Auditor (fast_mcp_ex_4.py)

Este servidor tiene una sola tool, aunque es una mezcla de FastMCP y una IA de cosecha propia. La IA está entrenada usando [este dataset](https://github.com/kaur-anupreet/Software-Defect-Prediction/blob/master/cm1.csv), con el objetivo de discernir cómo de probable es que sucedan bugs en un código dado y medir la complejidad y mantenibilidad de dicho código. 

Dicha IA actúa como el "experto", mientras que la otra actúa como intermediario y analista de resultados entre la IA y el usuario, interpretando lo que esta dice y devolviéndole elr esultado al usuario, evitando así que sean los LLMs (IAs no especializadas) los que realicen tareas específicas e impropias, donde pueden suceder fallos.