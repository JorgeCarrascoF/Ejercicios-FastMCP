import random
import time
from datetime import datetime
from typing import List
from uuid import uuid4

from fastmcp import FastMCP

mcp = FastMCP("Servidor MCP")

@mcp.tool()
def greet(name: str) -> str:
    return f"Hola, {name}!"
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b
@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b
@mcp.tool()
def divide(a: int, b: int) -> float:
    if b == 0:
        return "No se puede dividir por cero"
    return a / b
@mcp.tool()
def system_info() -> dict:
    return {"estado": "activo", "usuarios": 42, "carga": 0.75}


@mcp.tool()
def word_stats(text: str) -> dict:
    words = [w for w in text.split() if w.strip()]
    normalized = {w.lower().strip('.,;:!?"') for w in words}
    return {
        "palabras": len(words),
        "palabras_unicas": len(normalized),
        "caracteres": len(text),
    }


@mcp.tool()
def fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]



@mcp.tool()
def temperature_convert(value: float, unit: str) -> dict:
    unit_normalized = unit.lower()
    if unit_normalized not in {"c", "f", "k"}:
        return {"error": "la unidad debe ser c, f o k"}
    if unit_normalized == "c":
        c = value
        f = value * 9 / 5 + 32
        k = value + 273.15
    elif unit_normalized == "f":
        c = (value - 32) * 5 / 9
        f = value
        k = c + 273.15
    else:
        k = value
        c = value - 273.15
        f = c * 9 / 5 + 32
    return {"celsius": round(c, 4), "fahrenheit": round(f, 4), "kelvin": round(k, 4)}


@mcp.tool()
def roll_dice(count: int = 1, sides: int = 6) -> List[int]:
    count_clamped = max(1, min(count, 20))
    sides_clamped = max(2, min(sides, 120))
    return [random.randint(1, sides_clamped) for _ in range(count_clamped)]


@mcp.tool()
def iso_timestamp() -> str:
    return datetime.utcnow().isoformat() + "Z"


@mcp.tool()
def sleepy_echo(message: str, delay_seconds: float = 0.1) -> str:
    time.sleep(max(0.0, min(delay_seconds, 5.0)))
    return message


@mcp.tool()
def random_quote() -> str:
    quotes = [
        "La simplicidad es el alma de la eficiencia.",
        "Los programas deben ser escritos para que los lean las personas.",
        "La optimizacion prematura es la raiz de todos los males.",
        "No hay bala de plata, pero hay muchos buenos patrones.",
        "Las pruebas son la red de seguridad para refactorizar rapido.",
    ]
    return random.choice(quotes)


@mcp.tool()
def generate_uuid() -> str:
    return str(uuid4())


@mcp.tool()
def shuffle_items(items: List[str]) -> List[str]:
    copy = list(items)
    random.shuffle(copy)
    return copy



# Basic dynamic resource returning a string
@mcp.resource("resource://greeting")
def get_greeting() -> str:
    """Devuelve un saludo simple."""
    return "Hola desde FastMCP Resources!"


# Resource returning JSON data (dict is auto-serialized)
@mcp.resource("data://config")
def get_config() -> dict:
    """Config de aplicacion en JSON."""
    return {
        "tema": "oscuro",
        "version": "1.2.0",
        "funciones": ["tools", "resources"],
    }
# Resource returning JSON data (dict is auto-serialized)
@mcp.resource("data://system_config")
def get_system_config() -> dict:
    """Config del sistema como JSON."""
    return {
        "estado": "activo",
        "usuarios": 42,
    }


@mcp.resource("resource://lorem")
def get_lorem() -> str:
    return (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    )


@mcp.resource("data://product_catalog")
def get_product_catalog() -> dict:
    return {
        "updated": "2025-12-07T00:00:00Z",
        "categorias": ["libros", "gadgets", "cursos", "servicios"],
        "items": [
            {
                "id": "bk-001",
                "nombre": "MCP Practico",
                "precio": 39.99,
                "tags": ["mcp", "python", "api"],
                "descripcion": "Patrones practicos para construir servidores y clientes MCP.",
            },
            {
                "id": "gd-010",
                "nombre": "Depurador IA",
                "precio": 129.0,
                "tags": ["hardware", "debug"],
                "descripcion": "Analizador logico USB optimizado para dispositivos edge con IA.",
            },
            {
                "id": "cs-050",
                "nombre": "Bootcamp de LLM Ops",
                "precio": 299.0,
                "tags": ["training", "llm", "ops"],
                "descripcion": "Tres semanas sobre observabilidad, evaluaciones y guardrails.",
            },
            {
                "id": "sv-200",
                "nombre": "Revision de Prompts",
                "precio": 499.0,
                "tags": ["servicios", "prompt", "auditoria"],
                "descripcion": "Revision experta de prompts, seguridad y rendimiento.",
            },
            {
                "id": "gd-099",
                "nombre": "Kit Edge Dev",
                "precio": 249.5,
                "tags": ["hardware", "edge", "dev"],
                "descripcion": "Computadora de placa unica con GPU y SDKs precargados.",
            },
        ],
    }


@mcp.resource("data://knowledge_base")
def get_knowledge_base() -> dict:
    return {
        "faqs": [
            {
                "q": "Que es MCP?",
                "a": "Un protocolo para exponer herramientas, recursos y prompts compatibles con modelos.",
            },
            {
                "q": "Como agrego una tool?",
                "a": "Decora una funcion con @mcp.tool() y devuelve datos serializables a JSON.",
            },
            {
                "q": "Los recursos pueden ser dinamicos?",
                "a": "Si, pueden calcular datos en cada llamada y devolver strings u objetos.",
            },
            {
                "q": "Que transportes se soportan?",
                "a": "SSE es comun; websockets pueden estar disponibles segun el stack.",
            },
        ],
        "examples": [
            "Usa tools para acciones como matematicas, formato o consultas de datos.",
            "Usa resources para datos cacheados o de referencia como docs o configs.",
            "Combina prompts con tools para guiar como el modelo debe pedir ayuda.",
        ]
    }


@mcp.resource("data://handbook")
def get_handbook() -> str:
    return (
        "# Manual del Servidor MCP\n"
        "## Inicio rapido\n"
        "1. Instala dependencias.\n"
        "2. Ejecuta el servidor con transporte SSE.\n"
        "3. Registra tools, resources y prompts.\n\n"
        "## Patrones\n"
        "- Mantener las tools rapidas y deterministas cuando sea posible.\n"
        "- Devolver datos serializables a JSON para facilitar el parsing.\n"
        "- Usar resources para datos mas grandes o mayormente de lectura.\n\n"
        "## Ejemplos\n"
        "- Utilidades de texto: conteos, normalizacion, resumenes.\n"
        "- Utilidades de datos: conversiones, estadisticas, timestamps.\n"
        "- Simulacion: tiradas de dados, retrasos, frases aleatorias.\n\n"
        "## Troubleshooting\n"
        "- Validar payloads antes de procesar.\n"
        "- Limitar entradas que puedan agotar CPU o memoria.\n"
        "- Loguear invocaciones para observabilidad.\n"
    )


@mcp.resource("data://benchmarks")
def get_benchmarks() -> dict:
    return {
        "updated": "2025-12-07T12:00:00Z",
        "runs": [
            {
                "nombre": "text-tools",
                "duracion_ms": 18,
                "p95_ms": 25,
                "tps": 120,
                "notas": "Estadisticas de palabras y normalizacion con baja carga.",
            },
            {
                "nombre": "math-suite",
                "duracion_ms": 9,
                "p95_ms": 15,
                "tps": 220,
                "notas": "Suma, resta, multiplicacion y division con enteros pequenos.",
            },
            {
                "nombre": "catalog-fetch",
                "duracion_ms": 6,
                "p95_ms": 10,
                "tps": 320,
                "notas": "Lectura del recurso de catalogo de productos.",
            },
            {
                "nombre": "sleepy-echo",
                "duracion_ms": 105,
                "p95_ms": 140,
                "tps": 40,
                "notas": "Latencia simulada con retrasos acotados para probar back-pressure.",
            },
        ],
    }


@mcp.resource("data://sample_logs")
def get_sample_logs() -> dict:
    return {
        "entries": [
            {
                "ts": "2025-12-07T10:00:00Z",
                "level": "INFO",
                "message": "Servidor iniciado",
                "meta": {"transporte": "sse", "pid": 12001},
            },
            {
                "ts": "2025-12-07T10:05:00Z",
                "level": "DEBUG",
                "message": "Tool invocada",
                "meta": {"tool": "add", "args": [2, 3]},
            },
            {
                "ts": "2025-12-07T10:06:30Z",
                "level": "WARN",
                "message": "Carga alta",
                "meta": {"carga": 0.91, "usuarios": 120},
            },
            {
                "ts": "2025-12-07T10:10:00Z",
                "level": "INFO",
                "message": "Resource servido",
                "meta": {"resource": "data://product_catalog"},
            },
        ]
    }


@mcp.resource("resource://changelog")
def get_changelog() -> str:
    return (
        "## v1.2.0\n"
        "- Se agregaron tools de ejemplo para matematicas, texto y tiempo.\n"
        "- Se incorporaron resources de catalogo de productos y base de conocimiento.\n"
        "- Se incluyeron logs de ejemplo para probar respuestas en streaming.\n"
        "- Se mejoraron las cadenas de documentacion en todo el proyecto.\n"
    )

@mcp.prompt
def ask_about_topic(topic: str, role: str) -> str:
    """Genera un mensaje pidiendo explicar un tema."""
    return f"Puedes explicar el concepto de '{topic}' de forma comprensible para un {role}?"


@mcp.prompt
def summarize_text(text: str, focus: str = "general") -> str:
    """Pide al modelo un resumen con foco opcional."""
    return (
        "Por favor resume el siguiente texto de manera concisa. "
        f"Enfocate en {focus}.\n\nTEXTO:\n{text}\n"
    )


@mcp.prompt
def translate_text(text: str, target_language: str) -> str:
    """Pide al modelo traducir un texto a otro idioma."""
    return (
        f"Traduce el siguiente texto al {target_language}. "
        "Preserva el sentido y el tono.\n\nTEXTO:\n"
        f"{text}\n"
    )


@mcp.prompt
def brainstorming(topic: str, count: int = 5) -> str:
    """Pide una lluvia de ideas sobre un tema."""
    return (
        f"Genera {count} ideas creativas y no obvias sobre: {topic}. "
        "Devuelvelas como lista numerada."
    )


@mcp.prompt
def code_review_snippet(code: str, language: str = "python") -> str:
    """Pide revisar un fragmento de codigo."""
    return (
        f"Revisa el siguiente codigo {language} buscando bugs, casos borde y claridad. "
        "Enumera hallazgos con severidad (alta/media/baja) y breve arreglo.\n\nCODIGO:\n"
        f"{code}\n"
    )


if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)