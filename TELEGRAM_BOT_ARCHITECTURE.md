# Binance Telegram Bot - Architecture Documentation

## 🏗️ System Architecture

### Overview Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        TELEGRAM USER                             │
│                     (Mobile/Desktop App)                         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ Commands & Files
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    TELEGRAM BOT API                              │
│                   (Telegram Servers)                             │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ python-telegram-bot
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              BINANCE TELEGRAM BOT                                │
│           (binance_telegram_bot.py)                              │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  ConversationHandler                                      │  │
│  │  - Main Menu                                              │  │
│  │  - File Upload States                                     │  │
│  │  - Configuration States                                   │  │
│  │  - Checking States                                        │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Session Manager                                          │  │
│  │  - UserSession objects                                    │  │
│  │  - Per-user configuration                                 │  │
│  │  - Progress tracking                                      │  │
│  │  - Results storage                                        │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  BinanceChecker                                           │  │
│  │  - Account checking logic                                 │  │
│  │  - Proxy rotation                                         │  │
│  │  - Captcha solving                                        │  │
│  │  - API requests                                           │  │
│  └──────────────────────────────────────────────────────────┘  │
└───────────┬─────────────────┬──────────────────┬───────────────┘
            │                 │                  │
            │                 │                  │
            ▼                 ▼                  ▼
   ┌────────────────┐ ┌──────────────┐ ┌────────────────┐
   │  PROXIES       │ │  CAPTCHA     │ │  BINANCE API   │
   │  (HTTP/HTTPS/  │ │  SERVICES    │ │                │
   │   SOCKS4/5)    │ │              │ │  - /en/login   │
   │                │ │ - 2Captcha   │ │  - /bapi/auth  │
   │ User-provided  │ │ - AntiCap    │ │  - /bapi/user  │
   │ proxy list     │ │ - CapMonster │ │                │
   └────────────────┘ └──────────────┘ └────────────────┘
```

## 🔄 Data Flow

### 1. User Interaction Flow

```
User sends /start
    ↓
Bot displays main menu
    ↓
User selects action
    ↓
┌─────────────────────────────────────────────────────────┐
│ Option 1: Upload Combos                                 │
│   → User sends file or text                             │
│   → Bot parses email:password format                    │
│   → Stores in session.combos                            │
│   → Returns to main menu                                │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ Option 2: Upload Proxies                                │
│   → User sends file or text                             │
│   → Bot parses ip:port format                           │
│   → Stores in session.proxies                           │
│   → Returns to main menu                                │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ Option 3: Configure Settings                            │
│   → Shows current configuration                         │
│   → User selects setting to change                      │
│   → Interactive selection/input                         │
│   → Updates session configuration                       │
│   → Returns to config menu or main menu                 │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ Option 4: Start Checking                                │
│   → Validates combos and proxies exist                  │
│   → Shows confirmation with summary                     │
│   → User confirms                                        │
│   → Starts async checking process                       │
│   → Returns to main menu                                │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│ Option 5: View Results                                  │
│   → Shows results summary                               │
│   → Displays sample valid accounts                      │
│   → Option to export full results                       │
│   → Returns to main menu                                │
└─────────────────────────────────────────────────────────┘
```

### 2. Checking Process Flow

```
User clicks "Start Checking"
    ↓
validate_inputs()
    ↓
create_checker_instance()
    ↓
┌────────────────────────────────────────────────────────┐
│ run_checks() - Async Task                              │
│                                                         │
│  For each combo in session.combos:                     │
│      ↓                                                  │
│  Create async task with semaphore                      │
│      ↓                                                  │
│  check_account(email, password)                        │
│      ├─→ get_next_proxy()                              │
│      ├─→ GET /en/login (get CSRF token)                │
│      ├─→ solve_captcha() [if enabled]                  │
│      │    ├─→ submit to captcha service                │
│      │    ├─→ wait 20-25 seconds                       │
│      │    └─→ get captcha response                     │
│      ├─→ POST /bapi/auth/login                         │
│      ├─→ parse response                                │
│      └─→ GET /bapi/account/info [if valid]             │
│      ↓                                                  │
│  Create CheckResult object                             │
│      ↓                                                  │
│  Update session.progress                               │
│      ↓                                                  │
│  Every 10 checks → send_progress_update()              │
│      ↓                                                  │
│  Store result in session.results                       │
│                                                         │
│  After all checks complete:                            │
│      ↓                                                  │
│  send_final_results()                                  │
│      ↓                                                  │
│  export_results() → send file to user                  │
└────────────────────────────────────────────────────────┘
```

### 3. Proxy Rotation Flow

```
check_account() called
    ↓
get_next_proxy()
    ↓
┌────────────────────────────────────────┐
│ Round-robin selection:                 │
│   current_index = proxy_index          │
│   proxy = proxies[current_index]       │
│   proxy_index = (index + 1) % length   │
└────────────────────────────────────────┘
    ↓
Parse proxy string
    ├─→ Split by ':'
    ├─→ Extract ip:port[:user:pass]
    └─→ Format: {proxy_type}://ip:port
    ↓
Return proxy dict
    ↓
Use in aiohttp request
```

### 4. Captcha Solving Flow

```
Login requires captcha
    ↓
solve_captcha(site_key, page_url)
    ↓
┌────────────────────────────────────────────────────────┐
│ Check session.captcha_service                          │
│                                                         │
│ If NONE:                                               │
│   return None                                          │
│                                                         │
│ If 2CAPTCHA:                                           │
│   ├─→ POST to 2captcha.com/in.php                      │
│   ├─→ Receive captcha_id                               │
│   ├─→ Wait 20 seconds                                  │
│   ├─→ GET 2captcha.com/res.php (poll every 5s)        │
│   └─→ Return captcha_response                          │
│                                                         │
│ If ANTICAPTCHA:                                        │
│   ├─→ POST createTask                                  │
│   ├─→ Receive task_id                                  │
│   ├─→ Wait 20 seconds                                  │
│   ├─→ POST getTaskResult (poll every 5s)              │
│   └─→ Return gRecaptchaResponse                        │
│                                                         │
│ If CAPMONSTER:                                         │
│   ├─→ POST createTask                                  │
│   ├─→ Receive task_id                                  │
│   ├─→ Wait 20 seconds                                  │
│   ├─→ POST getTaskResult (poll every 5s)              │
│   └─→ Return gRecaptchaResponse                        │
└────────────────────────────────────────────────────────┘
    ↓
Return captcha token
    ↓
Include in login request
```

## 📦 Component Details

### BinanceTelegramBot Class

**Responsibilities:**
- Initialize Telegram application
- Setup conversation handlers
- Manage user sessions
- Route commands to handlers
- Coordinate checking process

**Key Methods:**
- `start_command()` - Entry point, show main menu
- `handle_menu_selection()` - Route menu actions
- `handle_combo_upload()` - Process combo files
- `handle_proxy_upload()` - Process proxy files
- `show_configuration_menu()` - Display settings
- `handle_settings_selection()` - Update settings
- `confirm_start_checking()` - Validate and confirm
- `run_checks()` - Execute checking process
- `send_progress_update()` - Send progress messages
- `export_results()` - Create and send result files

### UserSession Class

**Data Structure:**
```python
{
    user_id: int,
    combos: [(email, password), ...],
    proxies: ["ip:port", "ip:port:user:pass", ...],
    proxy_type: ProxyType enum,
    captcha_service: CaptchaService enum,
    captcha_api_key: str,
    use_advanced_evasion: bool,
    retry_on_captcha: bool,
    max_captcha_retries: int,
    max_threads: int,
    results: [CheckResult, ...],
    is_checking: bool,
    progress: {
        total: int,
        checked: int,
        valid: int,
        invalid: int,
        errors: int,
        start_time: float
    }
}
```

### BinanceChecker Class

**Responsibilities:**
- Perform account checks
- Manage proxy rotation
- Handle captcha solving
- Make API requests
- Parse responses
- Extract account data

**Key Methods:**
- `check_account(email, password)` - Main check method
- `get_next_proxy()` - Proxy rotation
- `solve_captcha(site_key, url)` - Captcha solving dispatcher
- `_solve_2captcha()` - 2Captcha integration
- `_solve_anticaptcha()` - Anti-Captcha integration
- `_solve_capmonster()` - CapMonster integration

### CheckResult Class

**Data Structure:**
```python
{
    email: str,
    password: str,
    status: "valid" | "invalid" | "error",
    email_verified: bool | None,
    kyc_status: str | None,
    two_fa_enabled: bool | None,
    vip_level: int | None,
    country: str | None,
    account_status: str | None,
    phone_verified: bool | None,
    registration_date: str | None,
    error_message: str | None,
    timestamp: str
}
```

## 🔐 Security Architecture

### API Key Management

```
User inputs captcha API key
    ↓
Stored in UserSession object (memory only)
    ↓
Used for captcha requests
    ↓
NOT logged or saved to disk
    ↓
Cleared when session ends or bot restarts
```

### Proxy Security

```
User uploads proxy list
    ↓
Stored in UserSession.proxies
    ↓
Parsed on-demand for each request
    ↓
Credentials (if present) included in request URL
    ↓
NOT logged in plain text
```

### Environment Variables

```
Bot token from TELEGRAM_BOT_TOKEN env var
    ↓
Loaded at startup
    ↓
Used for Telegram API authentication
    ↓
Never exposed in logs or user messages
```

## ⚡ Performance Optimization

### Multi-threading Architecture

```
User sets max_threads (e.g., 10)
    ↓
Create asyncio.Semaphore(10)
    ↓
┌────────────────────────────────────────┐
│ For each combo:                        │
│   Create async task                    │
│   Tasks wait at semaphore              │
│   Only 10 tasks run concurrently       │
│   When task completes, semaphore free  │
│   Next task starts                     │
└────────────────────────────────────────┘
    ↓
All tasks gathered and awaited
```

### Connection Pooling

```
aiohttp.ClientSession created per check
    ↓
Reused for multiple requests (CSRF, login, info)
    ↓
Automatic connection pooling by aiohttp
    ↓
Timeout: 30 seconds per request
    ↓
Session closed after check complete
```

### Progress Updates

```
Every check increments counter
    ↓
If counter % 10 == 0:
    Send progress update to user
    ↓
Prevents message flood
    ↓
Keeps user informed without spam
```

## 📊 State Machine

### Conversation States

```
States.MAIN_MENU (0)
    ├─→ upload_combos → States.UPLOAD_COMBO (1)
    ├─→ upload_proxies → States.UPLOAD_PROXIES (2)
    ├─→ configure → States.CONFIGURE_SETTINGS (6)
    │   ├─→ set_proxy_type → States.SELECT_PROXY_TYPE (3)
    │   ├─→ set_captcha → States.SELECT_CAPTCHA_SERVICE (4)
    │   └─→ set_captcha_key → States.ENTER_CAPTCHA_KEY (5)
    ├─→ start_check → States.START_CHECKING (7)
    └─→ view_results → States.VIEW_RESULTS (8)

All states can return to MAIN_MENU
All states can be cancelled with /cancel
```

## 🔄 Error Handling

### Error Recovery Flow

```
Exception occurs during check
    ↓
Caught in try/except block
    ↓
Determine error type:
    ├─→ TimeoutError → status="error", msg="timeout"
    ├─→ ConnectionError → status="error", msg="connection"
    ├─→ JSON parse error → status="error", msg="parse"
    └─→ Other → status="error", msg=str(exception)
    ↓
Log error with logger.error()
    ↓
Create CheckResult with error status
    ↓
Continue to next check
    ↓
Don't crash entire checking process
```

### Graceful Degradation

```
If captcha solving fails:
    ↓
Increment retry counter
    ↓
If counter < max_retries:
    Retry with delay
Else:
    Mark as error and continue
    ↓
If all proxies fail:
    ↓
Check without proxy
    ↓
If that fails:
    Mark as error
    ↓
Never crash bot completely
```

## 📈 Scalability

### Current Limits

- **Users**: Unlimited (session-based)
- **Concurrent Threads**: 1-50 per user
- **Combos**: Limited by memory (~1MB per 10k combos)
- **Proxies**: Limited by memory (~1KB per 1k proxies)
- **Results**: Limited by memory and file system

### Future Enhancements

1. **Database Integration**
   - Store results in database
   - Persistent session storage
   - Historical tracking

2. **Distributed Checking**
   - Multiple checker instances
   - Load balancing
   - Shared queue system

3. **Advanced Analytics**
   - Success rate tracking
   - Proxy quality metrics
   - Captcha service comparison

## 🛠️ Deployment Options

### Option 1: Local Development
```
Developer machine
    ├─→ Python 3.8+
    ├─→ Install requirements
    ├─→ Set TELEGRAM_BOT_TOKEN
    └─→ Run bot directly
```

### Option 2: VPS/Cloud Server
```
Cloud server (AWS/DigitalOcean/etc)
    ├─→ Install Python
    ├─→ Clone repository
    ├─→ Install requirements
    ├─→ Set environment variables
    ├─→ Run with screen/tmux
    └─→ Or use systemd service
```

### Option 3: Docker (Future)
```
Docker container
    ├─→ Dockerfile with Python
    ├─→ Install dependencies
    ├─→ Environment variables via -e or .env
    └─→ docker run command
```

## 📝 Code Quality

### Metrics

- **Lines of Code**: ~1,100
- **Functions**: 30+
- **Classes**: 6
- **Error Handlers**: Complete coverage
- **Documentation**: Inline comments + external docs
- **Type Hints**: Extensive use of typing
- **Async/Await**: Full async implementation

### Testing Coverage

- ✅ Syntax validation
- ✅ Import verification
- ✅ Manual testing of core flows
- ⚠️ Unit tests: Not yet implemented
- ⚠️ Integration tests: Not yet implemented

---

**Version:** 1.0.0  
**Last Updated:** 2025-11-20  
**Author:** legendhkek
