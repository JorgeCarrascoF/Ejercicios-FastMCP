from fastmcp import Client
from fastmcp.client.transports import SSETransport
import asyncio

client = Client(SSETransport("http://localhost:8000/sse"))

async def call_tool(name: str):
    async with client:

        tools = await client.list_tools()
        print("herramientas disponibles:")
        for tool in tools:
            print(f"- {tool.name}")

        resources = await client.list_resources()
        print("recursos disponibles:")
        for resource in resources:
            print(f"- {resource.name}")

        prompts = await client.list_prompts()
        print("prompts disponibles:")
        for prompt in prompts:
            print(f"- {prompt.name}")


asyncio.run(call_tool("John Doe"))