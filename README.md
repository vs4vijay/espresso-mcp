# espresso-mcp

A MCP Server for the Espresso Android Test Framework, designed to enhance testing capabilities and streamline development workflows.

## Available Tools

The following tools are available in the `espresso-mcp` project:

- **list_avds**: List all available Android Virtual Devices (AVDs).
- **list_emulators**: List all running Android Emulators.
- **start_emulator**: Start an Android Emulator by name.
- **kill_emulator**: Kill a specific Android Emulator.
- **dump_ui_hierarchy**: Dump the UI hierarchy of the connected Android device.
- **list_apps**: List all installed apps on the connected Android device.
- **install_app**: Install an APK on the connected Android device.
- **start_app**: Start a specific app on the connected Android device.
- **stop_app**: Stop a specific app on the connected Android device.
- **uninstall_app**: Uninstall an app from the connected Android device.
- **clear_app_data**: Clear app data for a specific app on the connected Android device.
- **take_screenshot**: Take a screenshot of the connected Android device.
- **press_button**: Simulate a button press on the connected Android device.
- **tap**: Simulate a tap on the connected Android device at specific coordinates.
- **swipe**: Perform a swipe gesture in a specific direction on the connected Android device.
- **open_uri**: Open a URI on the connected Android device.

## Resources

The following resources are available:

- **config://app**: Retrieve static configuration data.
- **greeting://{name}**: Get a personalized greeting.

## Local Development

- uv install

```bash
uv run mcp dev server.py
```

---

### Developement Notes

```bash

uv init espress-mcp

uv add "mcp[cli]"

uv run mcp dev server.py

```
