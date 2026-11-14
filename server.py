
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Hello MCP")

@mcp.tool()
def get_greeting(name: str) -> str:
    """Return a greeting for a student."""
    return f"Hello, {name}! Your first MCP tool works."

@mcp.tool()
def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

if __name__ == "__main__":
    mcp.run()
