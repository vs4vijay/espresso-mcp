# GitHub Copilot Instructions for espresso-mcp

## Project Overview

This repository contains **espresso-mcp**, an MCP (Model Context Protocol) server for the Android Espresso testing framework. The project enables AI assistants to interact with Android devices and emulators through a standardized protocol, providing automated testing capabilities and device control.

### Key Technologies
- **Python 3.10+** - Core language
- **FastMCP** - MCP server framework
- **uv** - Modern Python package and project manager
- **ruff** - Fast Python linter and formatter
- **pytest** - Testing framework
- **ADB (Android Debug Bridge)** - Android device communication

## Architecture

The project follows a clean MCP server architecture:

- **`src/espresso_mcp/server.py`** - Main MCP server implementation with tools and resources
- **`src/espresso_mcp/__init__.py`** - Package initialization
- **`tests/`** - Test suite using pytest
- **`pyproject.toml`** - Project configuration and dependencies
- **`uv.lock`** - Locked dependency versions

### MCP Tools Available
- Android emulator management (list, start, kill)
- Device interaction (tap, swipe, button presses)
- Text input and manipulation
- Screenshot and screen recording
- Device status and information

## Development Setup

### Prerequisites
- Python 3.10 or higher
- Android SDK tools (adb, emulator) for full functionality
- uv package manager

### Initial Setup
```bash
# Clone and navigate to repository
git clone <repository-url>
cd espresso-mcp

# Install dependencies
uv sync --all-extras --dev

# Run the server
uv run espresso-mcp

# Or run in development mode
uv run mcp dev src/espresso_mcp/server.py
```

## Code Style and Standards

### Linting and Formatting
- Use **ruff** for linting and code formatting
- Configuration in `pyproject.toml` with line length of 100 characters
- Target Python 3.10+ features
- Run linting: `uv run ruff check`
- Fix auto-fixable issues: `uv run ruff check --fix`

### Code Conventions
- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return values
- Document all MCP tools with clear docstrings
- Use descriptive variable and function names
- Keep functions focused and single-purpose

### Error Handling
- Use `RuntimeError` for subprocess failures
- Capture and include stderr in error messages
- Validate input parameters before processing
- Handle Android device connection issues gracefully

## Testing

### Running Tests
```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=espresso_mcp

# Run specific test file
uv run pytest tests/test_server.py
```

### Test Guidelines
- Write tests for all new MCP tools and resources
- Mock external dependencies (subprocess calls, Android commands)
- Test both success and error scenarios
- Keep tests isolated and independent
- Use descriptive test names that explain the scenario

## MCP-Specific Guidelines

### Adding New Tools
When adding new MCP tools:
1. Use the `@mcp.tool()` decorator
2. Provide clear, descriptive docstrings
3. Use appropriate type hints
4. Handle errors gracefully with meaningful messages
5. Test on actual Android devices when possible

Example:
```python
@mcp.tool()
def new_android_action(parameter: str) -> str:
    """Clear description of what this tool does"""
    # Validate inputs
    if not parameter:
        raise ValueError("Parameter cannot be empty")
    
    # Execute action
    result = subprocess.run(["adb", "shell", "command"], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Error executing action: {result.stderr}")
    
    return f"Action completed successfully: {result.stdout.strip()}"
```

### Adding Resources
For MCP resources:
- Use `@mcp.resource()` decorator with appropriate URI patterns
- Support both static and dynamic resources
- Return structured data when appropriate
- Document URI patterns clearly

## Building and Publishing

### Build Process
```bash
# Build package
uv build

# Build wheel only
uv build --wheel

# Build without sources
uv build --no-sources
```

### Publishing
```bash
# Publish to PyPI
uv publish
```

## CI/CD Integration

The project uses GitHub Actions for:
- **CI Pipeline** (`ci.yml`) - Lint, test, and build on main branch
- **PR Gate** (`pr-gate.yml`) - Validate pull requests
- **Release** (`release.yml`) - Automated releases

### Pull Request Guidelines
- All PRs must pass linting (`uv run ruff check`)
- All tests must pass (`uv run pytest`)
- Code coverage should not decrease
- Include tests for new functionality
- Update documentation for user-facing changes

## Android Development Considerations

### Device Requirements
- Android device or emulator with USB debugging enabled
- ADB access configured
- Appropriate Android SDK tools installed

### Testing with Real Devices
- Test tools with both emulators and physical devices
- Handle device-specific variations gracefully
- Consider different Android API levels
- Test network connectivity scenarios

## Common Patterns

### Subprocess Execution
```python
result = subprocess.run(
    ["adb", "shell", "command"], 
    capture_output=True, 
    text=True
)
if result.returncode != 0:
    raise RuntimeError(f"Command failed: {result.stderr}")
```

### Input Validation
```python
def validate_coordinates(x: int, y: int) -> None:
    if x < 0 or y < 0:
        raise ValueError("Coordinates must be non-negative")
```

## Debugging

### MCP Inspector
Use the MCP Inspector for testing:
```bash
# Install MCP Inspector
yarn global add @modelcontextprotocol/inspector

# Test the server
yarn run @modelcontextprotocol/inspector python src/espresso_mcp/server.py
```

### Logging
- Use the configured logger for debugging
- Log important state changes
- Include relevant context in log messages

## Dependencies

### Core Dependencies
- `httpx` - HTTP client for API calls
- `mcp[cli]` - MCP server framework with CLI support
- `pillow` - Image processing for screenshots

### Development Dependencies
- `pytest` - Testing framework
- `ruff` - Linting and formatting

When adding new dependencies:
- Add to `dependencies` in `pyproject.toml` for runtime deps
- Add to `dev` dependency group for development-only deps
- Run `uv sync` to update lock file
- Consider security and maintenance implications

## Security Considerations

- Validate all input parameters to prevent injection attacks
- Use subprocess safely with explicit command arrays
- Be cautious with device access and permissions
- Don't log sensitive information (device IDs, personal data)
- Handle authentication tokens securely if needed

## Performance Guidelines

- Use async/await for I/O operations when possible
- Cache device information when appropriate
- Minimize subprocess calls in tight loops
- Consider timeout values for long-running operations
- Handle device disconnection gracefully