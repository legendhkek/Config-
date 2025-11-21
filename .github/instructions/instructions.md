# Repository Instructions for GitHub Copilot

## Repository Overview

This repository contains professional account checker configurations for OpenBullet 2 and a Telegram bot for Binance email validation. The main components are:

1. **OpenBullet Configurations** (.loli and .opk files): LoliCode/LoliScript configurations for various services
2. **Python Telegram Bot** (binance_telegram_bot.py): Async Python bot with advanced features
3. **Documentation**: Comprehensive guides and technical specifications

## General Guidelines

### Code Quality Standards

- **Security First**: Never commit API keys, tokens, or credentials. Always use environment variables via `.env` files
- **Documentation**: All code changes should be accompanied by updates to relevant documentation files
- **Minimal Changes**: Make surgical, focused changes that address specific issues without breaking existing functionality
- **Testing**: Test all Python changes locally before committing. Run the bot with test data to verify functionality

### File-Specific Conventions

#### Python Files (*.py)

- **Python Version**: Target Python 3.8+ for compatibility
- **Code Style**: Follow PEP 8 conventions
- **Async/Await**: All I/O operations should use async/await patterns (aiohttp, aiofiles, etc.)
- **Type Hints**: Use type hints for function parameters and return values
- **Error Handling**: Comprehensive try/except blocks with proper logging
- **Dependencies**: Add any new dependencies to `requirements.txt` with pinned versions

#### OpenBullet Configurations (*.loli, *.opk)

- **Format**: LoliCode/LoliScript or JSON-based OPK format
- **Comments**: Use LoliScript comments (// or #) to explain complex logic
- **Performance**: Optimize for high CPM (checks per minute) and concurrent bots
- **Security Features**: Include anti-bot evasion, TLS fingerprinting, and proxy rotation
- **Validation**: Always validate configuration structure before committing

#### Documentation (*.md)

- **Consistency**: Match the existing documentation style and formatting
- **Completeness**: Include usage examples, troubleshooting, and feature descriptions
- **Structure**: Use clear headings, bullet points, and code blocks
- **Updates**: When updating code, update corresponding documentation

## Development Workflow

### Python Development

1. **Environment Setup**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Testing**:
   - Test with real Telegram bot token (stored in `.env` or environment variable)
   - Validate proxy handling and captcha service integration
   - Test error handling with invalid inputs

3. **Dependencies**:
   - Use specific versions in requirements.txt (e.g., `package==version`)
   - Test with Python 3.8, 3.9, 3.10, and 3.11 if possible

### Configuration Development

1. **OpenBullet Configs**:
   - Test in OpenBullet 2 with sample data
   - Verify proxy rotation and error handling
   - Validate data extraction patterns

2. **File Naming**:
   - Use descriptive names: `SERVICE.COM.loli` or `service.com.opk`
   - Keep consistent with existing naming conventions

## Common Tasks

### Adding New Dependencies

1. Add to `requirements.txt` with specific version
2. Test installation: `pip install -r requirements.txt`
3. Update documentation if the dependency adds new features

### Updating Telegram Bot

1. Preserve existing session management and user data structures
2. Maintain backwards compatibility with existing bot commands
3. Test all command handlers (`/start`, `/help`, `/check`, `/status`, etc.)
4. Update `TELEGRAM_BOT_SETUP.md` with any new features

### Adding New OpenBullet Configuration

1. Create configuration file with appropriate extension (.loli or .opk)
2. Add documentation section to `README.md`
3. Create dedicated usage guide (e.g., `SERVICE_USAGE_GUIDE.md`)
4. Create technical specs document (e.g., `SERVICE_TECHNICAL_SPECS.md`)

## Security Considerations

### Sensitive Data

- **Never commit**: API keys, tokens, passwords, or credentials
- **Use .env files**: Store secrets in `.env` (already in .gitignore)
- **Example files**: Provide `.env.example` with placeholder values

### API Integration

- **Rate Limiting**: Implement proper rate limiting for all API calls
- **Error Handling**: Handle rate limit errors gracefully with retries
- **Proxy Usage**: Always use proxies for account checking operations

## Testing Guidelines

### Python Code

- Test async operations with real or mock services
- Validate error handling with edge cases
- Check memory leaks in long-running operations
- Test proxy rotation and failover

### OpenBullet Configurations

- Test with sample credential lists
- Verify proxy compatibility (HTTP, HTTPS, SOCKS4, SOCKS5)
- Validate data extraction accuracy
- Check error handling for various response codes

## Documentation Standards

- **Code Examples**: Always include working examples
- **Prerequisites**: List all required dependencies and setup steps
- **Troubleshooting**: Include common issues and solutions
- **Version Info**: Keep version numbers updated in configs and documentation

## Prohibited Actions

- **Do not** modify working configurations without testing
- **Do not** remove security features or anti-bot evasion measures
- **Do not** commit credentials or API keys
- **Do not** break backwards compatibility without clear justification
- **Do not** add dependencies that have known security vulnerabilities

## Notes for Copilot

- This repository contains both Python code and domain-specific configuration files
- When working with .loli or .opk files, treat them as structured text/JSON with special syntax
- Always preserve existing performance optimizations (CPM, bots, threading)
- Maintain the professional documentation style throughout the repository
- Test changes with real-world scenarios when possible
