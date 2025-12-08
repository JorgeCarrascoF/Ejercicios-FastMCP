from fastmcp import Client
from fastmcp.client.transports import SSETransport
import asyncio

async def listar_tools():
    client = Client(SSETransport("http://localhost:8001/sse"))
    async with client:
        tools = await client.list_tools()
        print("Tools disponibles:")
        for t in tools:
            print("-", t.name)


if __name__ == "__main__":
    asyncio.run(listar_tools())