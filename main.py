from fastmcp import  FastMCP
import  random
import  json

# create the fastmcp server instance
mcp = FastMCP("Simple Calculator MCP Server")

@mcp.tool
def add(a:int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

# generate the random number in given range
@mcp.tool
def random_number(min_val: int, max_val: int) -> int:
    """Generate a random integer between min_val and max_val."""
    return random.randint(min_val, max_val)

# resource: server information
@mcp.resource("info://server")
def server_info() -> str:
    """Return server information."""
    info = {
        "name": "Simple Calculator MCP Server",
        "version": "1.0.0",
        "description": "A simple MCP server that provides addition and random number generation functionalities.",
        "tools": ["add", "random_number"],
        "author": "Sumit dhanorkar"
    }
    return json.dumps(info, indent=4)



if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
