# server.py
import httpx
from mcp.server.fastmcp import FastMCP
import subprocess

# Create an MCP server
mcp = FastMCP("Espresso-MCP")


@mcp.tool()
def list_avds() -> list:
    """List all available Android Virtual Devices (AVDs)"""
    result = subprocess.run(["emulator", "-list-avds"], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Error listing AVDs: {result.stderr}")
    return result.stdout.splitlines()


@mcp.tool()
def list_emulators() -> list:
    """List all running Android Emulators"""
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Error listing emulators: {result.stderr}")
    lines = result.stdout.splitlines()
    print("---lines", lines)
    emulators = [line.split()[0] for line in lines[1:] if "emulator" in line]
    return emulators


@mcp.tool()
def start_emulator(emulator_name: str) -> str:
    """Start an Android Emulator by name"""
    result = subprocess.Popen(
        ["emulator", "-avd", emulator_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return f"Emulator '{emulator_name}' is starting."


@mcp.tool()
def kill_emulator(emulator_name: str) -> str:
    """Kill a specific Android Emulator"""
    result = subprocess.run(
        ["adb", "-s", emulator_name, "emu", "kill"], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Error killing emulator '{emulator_name}': {result.stderr}")
    return f"Emulator '{emulator_name}' has been killed."


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
async def fetch_weather(city: str) -> str:
    """Fetch current weather for a city"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.weather.com/{city}")
        return response.text


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"
