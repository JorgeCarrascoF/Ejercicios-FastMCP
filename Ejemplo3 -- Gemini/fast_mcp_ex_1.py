from fastmcp import FastMCP

server = FastMCP("ChatAOS")

@server.tool()
def greet_user(username: str) -> str:
    return f"Hola, {username}! Bienvenido al servidor FastMCP."

if __name__ == "__main__":
    server.run(transport="sse", host="0.0.0.0", port=8000)