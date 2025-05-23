# espresso-mcp

A MCP Server for the Espresso Android Test Framework, designed to enhance testing capabilities and streamline development workflows.

<a href="https://glama.ai/mcp/servers/@vs4vijay/espresso-mcp">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@vs4vijay/espresso-mcp/badge" />
</a>

## Installation

- Python 3.x
- uv: `pip install uv`

```bash
uv tool install espresso-mcp
```

## Usage

- On Claude: Add below JSON config to the file `claude_desktop_config.json`

```json
{
  "mcpServers": {
    "terminal": {
      "command": "uv",
      "args": ["pip", "run", "espresso-mcp", "--timeout-ms", "30000"]
    }
  }
}
```

## Available Tools

The following tools are available in the `espresso-mcp` project:

- **list_avds**: List all available Android Virtual Devices (AVDs).
- **list_emulators**: List all running Android Emulators.
- **start_emulator**: Start an Android Emulator by name.
- **kill_emulator**: Kill a specific Android Emulator.
- **dump_ui_hierarchy**: Dump the UI hierarchy of the connected Android device.
- **open_uri**: Open a URI on the connected Android device.
- **list_apps**: List all installed apps on the connected Android device.
- **install_app**: Install an APK on the connected Android device.
- **start_app**: Start a specific app on the connected Android device.
- **stop_app**: Stop a specific app on the connected Android device.
- **uninstall_app**: Uninstall an app from the connected Android device.
- **clear_app_data**: Clear app data for a specific app on the connected Android device.
- **take_screenshot**: Take a screenshot of the connected Android device.
- **record_screen**: Record the screen of the connected Android device for a specified duration.
- **press_button**: Simulate a button press on the connected Android device.
- **type_text**: Type text on the connected Android device.
- **tap**: Simulate a tap on the connected Android device at specific coordinates.
- **swipe**: Perform a swipe gesture in a specific direction on the connected Android device.

## Resources

The following resources are available:

- **config://app**: Retrieve static configuration data.
- **greeting://{name}**: Get a personalized greeting.

---

## Local Setup

- Python 3.x
- uv: `pip install uv`

```bash
# Install dependencies
uv sync
# OR
uv sync --frozen --all-extras --dev

# Run Server
uv run espresso-mcp

# Run in Dev Mode
uv run mcp dev server.py
```

## Debugging

- Use MCP Inspector

```bash
# Install MCP Inspector
yarn global add @modelcontextprotocol/inspector

# Test MCP Server
yarn run @modelcontextprotocol/inspector python server.py
```

## Testing and Linting

```bash
uv run pytest

uv run ruff check
```

## Publishing

```bash
# Build the package
uv build

# Upload to PyPI
uv publish
```

---

### Developement Notes

```bash

uv init espresso-mcp

uv add "mcp[cli]"

uv run mcp dev server.py


uv tool run espresso-mcp

```
