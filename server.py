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


@mcp.tool()
def dump_ui_hierarchy() -> str:
    """Dump the UI hierarchy of the connected Android device"""
    result = subprocess.run(
        ["adb", "shell", "uiautomator", "dump"], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Error dumping UI hierarchy: {result.stderr}")
    return result.stdout.strip()


@mcp.tool()
def install_apk(apk_path: str) -> str:
    """Install an APK on the connected Android device"""
    result = subprocess.run(
        ["adb", "install", apk_path], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Error installing APK: {result.stderr}")
    return f"APK '{apk_path}' has been installed successfully."


@mcp.tool()
def uninstall_app(package_name: str) -> str:
    """Uninstall an app from the connected Android device"""
    result = subprocess.run(
        ["adb", "uninstall", package_name], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Error uninstalling app '{package_name}': {result.stderr}")
    return f"App '{package_name}' has been uninstalled successfully."


@mcp.tool()
def take_screenshot(output_path: str) -> str:
    """Take a screenshot of the connected Android device"""
    result = subprocess.run(
        ["adb", "exec-out", "screencap", "-p"], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Error taking screenshot: {result.stderr}")
    with open(output_path, "wb") as file:
        file.write(result.stdout.encode("latin1"))
    return f"Screenshot saved to '{output_path}'."


@mcp.tool()
def clear_app_data(package_name: str) -> str:
    """Clear app data for a specific app on the connected Android device"""
    result = subprocess.run(
        ["adb", "shell", "pm", "clear", package_name], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Error clearing app data for '{package_name}': {result.stderr}"
        )
    return f"App data for '{package_name}' has been cleared."


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


@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"
