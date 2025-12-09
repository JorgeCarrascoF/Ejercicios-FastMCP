from fastmcp import FastMCP
import random

# Inicializamos el servidor
mcp = FastMCP("NumberGuesser")

# Variable global para guardar el secreto
# En un entorno real usaríamos una base de datos o una clase, 
# pero para aprender, una variable global basta.
numero_secreto = None

@mcp.tool()
def iniciar_partida() -> str:
    """Arranca el juego generando un número aleatorio entre 1 y 100."""
    global numero_secreto
    numero_secreto = random.randint(1, 100)
    return "He pensado un número del 1 al 100. ¡Intenta adivinarlo!"

@mcp.tool()
def hacer_intento(numero: int) -> str:
    """Envía un número para ver si es el correcto."""
    global numero_secreto
    
    if numero_secreto is None:
        return "Error: Primero debes iniciar la partida."

    if numero < numero_secreto:
        return "El número secreto es MAYOR."
    elif numero > numero_secreto:
        return "El número secreto es MENOR."
    else:
        # Al ganar, reseteamos para limpiar
        numero_secreto = None 
        return "¡CORRECTO! Has adivinado el número. Fin del juego."

if __name__ == "__main__":
    mcp.run()