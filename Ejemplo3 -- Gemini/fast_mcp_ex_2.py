from fastmcp import FastMCP

server = FastMCP("ChatAOS")

@server.tool()
def dechipher_text (text) :
    return text[::-1]

if __name__ == "__main__":
    server.run(transport="sse", host="0.0.0.0", port=8000)