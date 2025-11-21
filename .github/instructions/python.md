# Python Development Instructions

**Apply To**: `*.py`, Python-related files

## Code Style and Standards

### General Python Conventions

- **PEP 8 Compliance**: Follow PEP 8 style guide strictly
- **Line Length**: Maximum 100 characters (extended from PEP 8's 79 for readability)
- **Imports**: Group in order: standard library, third-party, local. Use absolute imports
- **Naming**:
  - Classes: `PascalCase`
  - Functions/Variables: `snake_case`
  - Constants: `UPPER_SNAKE_CASE`
  - Private members: prefix with single underscore `_private`

### Type Hints

Always use type hints for better code clarity:

```python
from typing import Dict, List, Optional, Tuple

async def process_accounts(
    accounts: List[str],
    proxies: Optional[List[str]] = None,
    timeout: int = 30
) -> Tuple[List[str], List[str]]:
    """Process account list and return valid and invalid accounts."""
    pass
```

### Async/Await Patterns

This repository uses asyncio extensively for the Telegram bot:

- **Always use async/await** for I/O operations
- Use `aiohttp` for HTTP requests (never `requests` in async contexts)
- Use `aiofiles` for file operations
- Properly close sessions and connections:

```python
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()
```

### Error Handling

Implement comprehensive error handling:

```python
try:
    result = await risky_operation()
except aiohttp.ClientError as e:
    logger.error(f"Network error: {e}")
    # Handle gracefully
except Exception as e:
    logger.exception(f"Unexpected error: {e}")
    # Fail safely
finally:
    # Clean up resources
    pass
```

## Telegram Bot Specific

### Bot Architecture

- **Session Management**: Each user has isolated session data
- **State Management**: Use conversation handlers for multi-step interactions
- **Rate Limiting**: Implement per-user rate limiting to prevent abuse
- **Error Messages**: User-friendly error messages in Telegram responses

### Command Handlers

All command handlers should follow this pattern:

```python
async def command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handle /command from user.
    
    Args:
        update: Telegram update object
        context: Bot context with user_data and chat_data
        
    Returns:
        Next conversation state or ConversationHandler.END
    """
    user_id = update.effective_user.id
    logger.info(f"User {user_id} executed /command")
    
    try:
        # Command logic here
        await update.message.reply_text("Response")
        return NEXT_STATE
    except Exception as e:
        logger.error(f"Error in command_handler: {e}")
        await update.message.reply_text("An error occurred. Please try again.")
        return ConversationHandler.END
```

### File Upload Handling

When handling file uploads (combos, proxies):

```python
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle uploaded file."""
    document = update.message.document
    
    # Validate file size
    if document.file_size > MAX_FILE_SIZE:
        await update.message.reply_text("File too large")
        return ConversationHandler.END
    
    # Download and process
    file = await context.bot.get_file(document.file_id)
    file_path = f"/tmp/{document.file_name}"
    
    async with aiofiles.open(file_path, 'wb') as f:
        await f.write(await file.download_as_bytearray())
    
    # Process file content
    return NEXT_STATE
```

## Security Best Practices

### Environment Variables

Always use environment variables for sensitive data:

```python
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CAPTCHA_API_KEY = os.getenv('CAPTCHA_API_KEY')

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN must be set")
```

### Input Validation

Validate all user inputs:

```python
def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_proxy(proxy: str) -> bool:
    """Validate proxy format (host:port or user:pass@host:port)."""
    patterns = [
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$',  # IP:port
        r'^[\w.-]+:\d{1,5}$',  # domain:port
        r'^[\w.-]+:[\w.-]+@[\w.-]+:\d{1,5}$',  # user:pass@host:port
    ]
    return any(re.match(pattern, proxy) for pattern in patterns)
```

### Rate Limiting

Implement rate limiting to prevent abuse:

```python
from collections import defaultdict
from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(list)
    
    def is_allowed(self, user_id: int) -> bool:
        """Check if user is within rate limit."""
        now = datetime.now()
        cutoff = now - timedelta(seconds=self.time_window)
        
        # Remove old requests
        self.requests[user_id] = [
            req_time for req_time in self.requests[user_id]
            if req_time > cutoff
        ]
        
        # Check limit
        if len(self.requests[user_id]) >= self.max_requests:
            return False
        
        self.requests[user_id].append(now)
        return True
```

## Logging

Use structured logging with appropriate levels:

```python
import logging

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Usage
logger.debug("Detailed debug information")
logger.info("General information")
logger.warning("Warning message")
logger.error("Error message")
logger.exception("Error with traceback")  # Use in except blocks
```

## Performance Considerations

### Concurrency

Use asyncio properly for concurrent operations:

```python
# Process multiple items concurrently
results = await asyncio.gather(
    *[process_item(item) for item in items],
    return_exceptions=True
)

# With semaphore to limit concurrency
semaphore = asyncio.Semaphore(10)

async def limited_task(item):
    async with semaphore:
        return await process_item(item)

results = await asyncio.gather(
    *[limited_task(item) for item in items]
)
```

### Memory Management

- Use generators for large datasets
- Close sessions and connections properly
- Clean up temporary files after use
- Avoid keeping large objects in memory

```python
async def process_large_file(filepath: str):
    """Process large file line by line."""
    async with aiofiles.open(filepath, 'r') as f:
        async for line in f:
            # Process one line at a time
            await process_line(line.strip())
```

## Testing

### Unit Tests

Write tests for critical functions:

```python
import pytest
import asyncio

@pytest.mark.asyncio
async def test_validate_email():
    """Test email validation."""
    assert validate_email("test@example.com") == True
    assert validate_email("invalid-email") == False
    assert validate_email("") == False

@pytest.mark.asyncio
async def test_proxy_connection():
    """Test proxy connection handling."""
    proxy = "127.0.0.1:8080"
    result = await test_proxy(proxy)
    assert result is not None
```

### Integration Tests

Test bot commands and workflows:

```python
from telegram.ext import Application
from unittest.mock import Mock, AsyncMock

@pytest.mark.asyncio
async def test_start_command():
    """Test /start command."""
    update = Mock()
    update.message = AsyncMock()
    update.effective_user.id = 12345
    
    context = Mock()
    
    result = await start_command(update, context)
    update.message.reply_text.assert_called_once()
```

## Documentation

All functions and classes must have docstrings:

```python
async def check_account(
    email: str,
    password: str,
    proxy: Optional[str] = None,
    captcha_service: Optional[str] = None
) -> Dict[str, any]:
    """
    Check if account credentials are valid.
    
    Args:
        email: Email address to check
        password: Account password
        proxy: Optional proxy in format host:port or user:pass@host:port
        captcha_service: Optional captcha service (2captcha, anticaptcha, etc.)
    
    Returns:
        Dictionary containing:
            - valid: bool - Whether credentials are valid
            - status: str - Account status
            - data: dict - Extracted account data
            - error: str - Error message if check failed
    
    Raises:
        ValueError: If email format is invalid
        aiohttp.ClientError: If network request fails
    
    Example:
        >>> result = await check_account("test@example.com", "password123")
        >>> print(result['valid'])
        True
    """
    pass
```

## Common Patterns

### Configuration Management

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class BotConfig:
    """Bot configuration."""
    bot_token: str
    captcha_service: Optional[str] = None
    captcha_api_key: Optional[str] = None
    max_threads: int = 10
    timeout: int = 30
    
    @classmethod
    def from_env(cls) -> 'BotConfig':
        """Load configuration from environment variables."""
        return cls(
            bot_token=os.getenv('TELEGRAM_BOT_TOKEN'),
            captcha_service=os.getenv('CAPTCHA_SERVICE'),
            captcha_api_key=os.getenv('CAPTCHA_API_KEY'),
            max_threads=int(os.getenv('MAX_THREADS', '10')),
            timeout=int(os.getenv('TIMEOUT', '30'))
        )
```

### Session Management

```python
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class UserSession:
    """User session data."""
    user_id: int
    combos: List[str] = field(default_factory=list)
    proxies: List[str] = field(default_factory=list)
    results: Dict[str, any] = field(default_factory=dict)
    started_at: Optional[datetime] = None
    
    def reset(self):
        """Reset session data."""
        self.combos.clear()
        self.proxies.clear()
        self.results.clear()
        self.started_at = None
```

## Dependencies

When adding new dependencies:

1. Add to `requirements.txt` with pinned version
2. Test compatibility with existing dependencies
3. Check for security vulnerabilities
4. Update documentation if new features are enabled

Example:
```
# Add new dependency
pip install package-name
pip freeze | grep package-name >> requirements.txt

# Test
pip install -r requirements.txt
python -m pytest
```
