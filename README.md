NAME: SK ADIL  
REG NO: 261FB04035

# Hello MCP Server

A small Model Context Protocol (MCP) server that exposes two tools: a greeting tool and a number-adder tool.

## Tools

- `get_greeting(name)`: Returns a greeting for the supplied name.
- `add_numbers(a, b)`: Returns the sum of two integers.

## Requirements

- Python
- The `mcp` package with CLI extras (`mcp[cli]`)

## Run

On Windows, run the server using the project's virtual environment:

```powershell
.venv\Scripts\python.exe server.py
```

The server communicates over the MCP transport configured by the Python MCP SDK.
