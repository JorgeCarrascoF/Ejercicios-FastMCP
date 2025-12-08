import httpx
import time
from fastmcp import FastMCP

client = httpx.AsyncClient(base_url="http://inventario:8080")

def wait_for_openapi(url, retries=20, delay=3):
    for i in range(retries):
        try:
            response = httpx.get(url)
            if response.status_code == 200:
                return response.json()
        except Exception:
            pass
        print(f"Esperando a que {url} esté disponible... (intento {i+1}/{retries})")
        time.sleep(delay)
    raise RuntimeError(f"No se pudo acceder a {url} después de {retries} intentos.")

openapi_spec = wait_for_openapi("http://inventario:8080/api-docs")

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="My API Server"
)

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8001)
