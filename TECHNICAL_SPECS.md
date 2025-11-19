# Sky.com Advanced Account Checker - Technical Specifications

## Architecture Overview

This document provides detailed technical specifications for the Sky.com Advanced Account Checker Pro configuration (v2.0.0).

## System Requirements

### OpenBullet Compatibility
- **Minimum Version:** OpenBullet 1.2.0
- **Recommended Version:** OpenBullet 2.x or Anomaly
- **Script Type:** LoliScript 2.0
- **Required Features:** 
  - JSON parsing support
  - Advanced threading
  - Proxy management
  - Cookie handling
  - Variable manipulation

### Resource Requirements
- **RAM:** Minimum 4GB, Recommended 8GB+ (for 500 bots)
- **CPU:** Multi-core processor (4+ cores recommended)
- **Network:** Stable connection with low latency
- **Proxy Pool:** Minimum 100 high-quality proxies

## Configuration Parameters

### General Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| SaveEmptyCaptures | Boolean | false | Don't save captures with no data |
| ContinueOnCustom | Boolean | true | Continue checking after CUSTOM status |
| SaveHitsToTextFile | Boolean | true | Save successful checks to file |
| IgnoreResponseErrors | Boolean | false | Fail on response errors |
| MaxRedirects | Integer | 12 | Maximum HTTP redirects |
| NeedsProxies | Boolean | true | Proxy requirement |
| OnlySocks | Boolean | false | Allow HTTP/HTTPS proxies |
| MaxCPM | Integer | 500 | Maximum checks per minute |
| SuggestedBots | Integer | 500 | Recommended concurrent workers |
| ThreadingEnabled | Boolean | true | Enable threading |
| MultiRequestSupport | Boolean | true | Enable multiple concurrent requests |
| ConcurrentRequests | Integer | 500 | Max simultaneous HTTP requests |
| RequestTimeout | Integer | 15000 | Request timeout in milliseconds |
| RetryOnError | Boolean | true | Retry on network errors |
| MaxRetries | Integer | 5 | Maximum retry attempts |

### Advanced General Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| EnableExponentialBackoff | Boolean | true | Enable exponential backoff on retries |
| BackoffMultiplier | Float | 2.0 | Multiply delay by this factor each retry |
| MaxBackoffDelay | Integer | 60000 | Maximum backoff delay (60 seconds) |
| EnableCircuitBreaker | Boolean | true | Enable circuit breaker pattern |
| CircuitBreakerThreshold | Integer | 10 | Failures before circuit opens |
| CircuitBreakerTimeout | Integer | 30000 | Time before retry after circuit opens |
| EnableRequestDeduplication | Boolean | true | Prevent duplicate requests |
| EnableSmartRetry | Boolean | true | Context-aware retry logic |

### Proxy Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| UseProxies | Boolean | true | Enable proxy usage |
| MaxUsesPerProxy | Integer | 20 | Maximum uses before rotation |
| BanProxyAfterGoodStatus | Boolean | false | Don't ban on success |
| BanLoopEvasionOverride | Integer | 15 | Override ban loop threshold |
| ProxyRotationStrategy | String | "RoundRobin" | Rotation algorithm |
| EnableProxyHealthCheck | Boolean | true | Monitor proxy health |
| HealthCheckInterval | Integer | 60000 | Health check interval (60s) |
| HealthCheckTimeout | Integer | 5000 | Health check timeout (5s) |
| EnableProxyScoring | Boolean | true | Score proxies by performance |
| BanProxyOnConsecutiveFailures | Integer | 5 | Ban after consecutive failures |
| ProxyReconnectDelay | Integer | 2000 | Delay before reconnecting (2s) |
| EnableGeoProxyValidation | Boolean | true | Validate proxy geography |
| AllowedProxyCountries | Array | ["US", "UK", "CA", "AU", "IE"] | Allowed countries |
| EnableProxyIPReputation | Boolean | true | Check IP reputation |
| MinProxyReputationScore | Float | 7.5 | Minimum reputation (0-10) |
| EnableStickySession | Boolean | true | Maintain session with proxy |
| SessionPersistenceDuration | Integer | 300000 | Session duration (5 minutes) |

### Threading Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| Enabled | Boolean | true | Enable threading |
| MaxThreads | Integer | 500 | Maximum threads |
| ThreadPoolSize | Integer | 500 | Thread pool size |
| QueueSize | Integer | 5000 | Work queue size |
| UseThreadPool | Boolean | true | Use thread pool |
| EnableDynamicThreading | Boolean | true | Scale threads dynamically |
| MinThreads | Integer | 100 | Minimum active threads |
| ThreadScalingFactor | Float | 1.5 | Scaling multiplier |
| ThreadIdleTimeout | Integer | 30000 | Idle timeout (30s) |
| EnableWorkStealing | Boolean | true | Enable work-stealing algorithm |
| EnableThreadAffinity | Boolean | true | CPU core affinity |
| PriorityQueue | Boolean | true | Priority-based queue |

### Rate Limiting Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| Enabled | Boolean | true | Enable rate limiting |
| MaxCPM | Integer | 500 | Maximum CPM |
| EnforceRateLimit | Boolean | true | Strict enforcement |
| BurstAllowed | Boolean | true | Allow burst requests |
| BurstSize | Integer | 100 | Burst window size |
| BurstDuration | Integer | 5000 | Burst window duration (5s) |
| EnableAdaptiveRateLimiting | Boolean | true | Adapt to server response |
| RateLimitBackoffOnError | Boolean | true | Reduce rate on errors |
| BackoffPercentage | Integer | 30 | Percentage reduction |
| EnableTokenBucket | Boolean | true | Token bucket algorithm |
| TokenRefillRate | Integer | 10 | Tokens per second |
| MaxTokens | Integer | 1000 | Maximum tokens |
| EnableSlidingWindow | Boolean | true | Sliding window tracking |
| WindowSize | Integer | 60000 | Window size (60s) |

### Multi-Request & Connection Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| Enabled | Boolean | true | Enable multi-request |
| MaxConcurrentRequests | Integer | 500 | Maximum concurrent requests |
| RequestQueueing | Boolean | true | Queue requests |
| KeepAlive | Boolean | true | HTTP keep-alive |
| ReuseConnections | Boolean | true | Reuse TCP connections |
| EnableConnectionPooling | Boolean | true | Connection pool |
| MaxConnectionsPerHost | Integer | 50 | Connections per host |
| ConnectionPoolSize | Integer | 200 | Total pool size |
| ConnectionIdleTimeout | Integer | 60000 | Idle timeout (60s) |
| EnableHTTP2 | Boolean | true | HTTP/2 support |
| EnablePipelining | Boolean | true | HTTP pipelining |
| MaxPipelineDepth | Integer | 5 | Pipeline depth |
| EnableRequestCompression | Boolean | true | Compress requests |
| EnableResponseCompression | Boolean | true | Decompress responses |

### Session Management

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| EnableSessionPersistence | Boolean | true | Persist sessions |
| SessionTimeout | Integer | 900000 | Session timeout (15 min) |
| EnableCookieJar | Boolean | true | Cookie management |
| CookiePolicy | String | "AcceptAll" | Cookie acceptance policy |
| EnableSessionRecovery | Boolean | true | Recover failed sessions |
| MaxSessionRetries | Integer | 3 | Recovery retry limit |
| SessionRefreshInterval | Integer | 600000 | Refresh interval (10 min) |

### Cache Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| EnableResponseCache | Boolean | true | Cache HTTP responses |
| CacheTTL | Integer | 300000 | Cache TTL (5 min) |
| MaxCacheSize | Integer | 1000 | Maximum cached items |
| EnableDNSCache | Boolean | true | Cache DNS lookups |
| DNSCacheTTL | Integer | 3600000 | DNS cache TTL (1 hour) |

### Security Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| EnableAntiBotEvasion | Boolean | true | Anti-bot techniques |
| EnableFingerprintRandomization | Boolean | true | Randomize fingerprints |
| EnableCanvasFingerprint | Boolean | true | Canvas fingerprinting |
| EnableWebGLFingerprint | Boolean | true | WebGL fingerprinting |
| EnableAudioFingerprint | Boolean | true | Audio fingerprinting |
| UserAgentRotation | Boolean | true | Rotate user agents |
| EnableTLSFingerprint | Boolean | true | TLS fingerprint mimicking |
| EnableHeaderRandomization | Boolean | true | Randomize headers |
| SimulateHumanBehavior | Boolean | true | Human-like delays |
| RandomDelayMin | Integer | 500 | Minimum delay (ms) |
| RandomDelayMax | Integer | 3000 | Maximum delay (ms) |

### Validation Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| EnableJSONSchemaValidation | Boolean | true | Validate JSON responses |
| EnableDataIntegrityCheck | Boolean | true | Check data integrity |
| EnableAccountQualityScoring | Boolean | true | Calculate quality score |
| MinQualityScore | Float | 5.0 | Minimum quality threshold |
| EnableSubscriptionValidation | Boolean | true | Validate subscription data |
| EnableBillingValidation | Boolean | true | Validate billing data |

### Logging Settings

| Parameter | Type | Value | Description |
|-----------|------|-------|-------------|
| EnableDetailedLogging | Boolean | true | Detailed logs |
| LogLevel | String | "DEBUG" | Logging level |
| LogRequestHeaders | Boolean | true | Log request headers |
| LogResponseHeaders | Boolean | true | Log response headers |
| LogRequestBody | Boolean | false | Log request body |
| LogResponseBody | Boolean | true | Log response body |
| EnablePerformanceMetrics | Boolean | true | Track performance |
| EnableErrorTracking | Boolean | true | Track errors |

## Script Workflow

### Block Execution Sequence

```
1. InitializeSession (Function)
   ├─ Generate session_id
   ├─ Create device_fingerprint
   └─ Set request_timestamp

2. PreflightRequest (Request)
   └─ HEAD https://www.sky.com

3. Delay (800-2000ms)

4. GetSignInPage (Request)
   └─ GET https://www.sky.com/signin

5. Parse Tokens
   ├─ csrf_token (Required, Retry on error)
   ├─ web_session_id (Optional)
   ├─ api_key (Optional)
   └─ client_id (Optional)

6. SetCookie
   └─ sky_session cookie

7. Delay (1200-2500ms)

8. AuthenticationRequest (Request)
   └─ POST https://www.sky.com/api/v1/auth/login

9. Parse Auth Response
   ├─ success
   ├─ auth_token
   ├─ refresh_token
   ├─ user_id
   └─ requires_2fa

10. Conditional Branching
    ├─ If requires_2fa → CUSTOM (2FA Required)
    ├─ If success=true → Jump to ValidateAccount
    └─ If success=false → Jump to HandleError

11. HandleError Block
    ├─ Parse error_msg and error_code
    └─ Route to appropriate status:
        ├─ AUTH_001 / "Invalid credentials" → FAIL
        ├─ "Account locked" → CUSTOM
        ├─ "suspended" → BAN
        ├─ "deactivated" → CUSTOM
        ├─ "expired" → CUSTOM
        ├─ "region" → BAN
        └─ RATE_LIMIT → RETRY (5s delay)

12. ValidateAccount Block
    ├─ Delay (500-1500ms)
    └─ GET https://www.sky.com/api/v1/user/profile

13. Parse Profile Data
    ├─ email
    ├─ first_name
    ├─ last_name
    ├─ phone
    ├─ country
    ├─ subscription_type
    ├─ subscription_status
    ├─ expiry_date
    ├─ is_premium
    └─ subscription_price

14. GetSubscriptionDetails (Request)
    └─ GET https://www.sky.com/api/v1/subscription/details

15. Parse Subscription Data
    ├─ channels
    ├─ addons
    └─ next_billing

16. GetBillingInfo (Request)
    └─ GET https://www.sky.com/api/v1/billing/info

17. Parse Billing Data
    ├─ payment_method
    ├─ card_last4
    └─ balance

18. GetDevices (Request)
    └─ GET https://www.sky.com/api/v1/devices

19. Parse Device Data
    ├─ device_count
    └─ device_types

20. CalculateAccountQuality (Function)
    ├─ Initialize quality_score = 0
    ├─ If subscription_status == 'active' → +3
    ├─ If is_premium == 'true' → +2
    ├─ If payment_method != '' → +2
    ├─ If device_count > 0 → +1
    └─ If expiry_date > current_time → +2

21. Quality Classification
    ├─ If quality_score > 7 → SUCCESS (HIGH QUALITY)
    ├─ If quality_score > 5 → SUCCESS (GOOD QUALITY)
    ├─ If quality_score > 3 → SUCCESS (MEDIUM QUALITY)
    └─ If subscription_status == 'active' → SUCCESS

22. Response Code Checks
    ├─ 429 → RETRY (10s delay + exponential backoff)
    ├─ 403 → BAN (IP Blocked)
    ├─ 401 → FAIL (Unauthorized)
    ├─ 500 → RETRY (max 2 retries)
    ├─ 503 → RETRY (15s delay)
    └─ 200 → SUCCESS
```

## API Endpoints

### Primary Endpoints
1. **https://www.sky.com** - Main domain
2. **https://www.sky.com/signin** - Sign-in page
3. **https://www.sky.com/api/v1/auth/login** - Authentication endpoint
4. **https://www.sky.com/api/v1/user/profile** - User profile
5. **https://www.sky.com/api/v1/subscription/details** - Subscription info
6. **https://www.sky.com/api/v1/billing/info** - Billing information
7. **https://www.sky.com/api/v1/devices** - Device list

## Data Capture Schema

### Captured Variables

| Variable Name | Type | Label | Source |
|---------------|------|-------|--------|
| auth_token | String | Auth Token | Login response |
| refresh_token | String | Refresh Token | Login response |
| user_id | String | User ID | Login response |
| email | String | Email | Profile |
| first_name | String | First Name | Profile |
| last_name | String | Last Name | Profile |
| phone | String | Phone | Profile |
| country | String | Country | Profile |
| subscription_type | String | Subscription Type | Profile |
| subscription_status | String | Subscription Status | Profile |
| expiry_date | String | Expiry Date | Profile |
| is_premium | Boolean | Premium Account | Profile |
| subscription_price | String | Subscription Price | Profile |
| channels | Array | Channels | Subscription details |
| addons | Array | Addons | Subscription details |
| next_billing | String | Next Billing Date | Subscription details |
| payment_method | String | Payment Method | Billing |
| card_last4 | String | Card Last 4 | Billing |
| balance | String | Account Balance | Billing |
| device_count | Integer | Device Count | Devices |
| device_types | Array | Device Types | Devices |
| quality_score | Integer | Quality Score | Calculated |

## Performance Metrics

### Expected Performance
- **Checks Per Minute (CPM):** 400-500 (with quality proxies)
- **Success Rate:** Depends on combo quality
- **Response Time:** 2-5 seconds per check
- **Memory Usage:** ~50-100MB per 100 bots
- **CPU Usage:** Moderate (multi-threaded)

### Optimization Tips
1. Use residential proxies for best results
2. Start with 100 bots and scale gradually
3. Monitor proxy ban rate
4. Adjust rate limiting based on response patterns
5. Enable all caching options

## Error Codes & Handling

| Code | Status | Action | Delay | Backoff |
|------|--------|--------|-------|---------|
| 200 | OK | SUCCESS | - | - |
| 401 | Unauthorized | FAIL | - | - |
| 403 | Forbidden | BAN | - | - |
| 429 | Rate Limited | RETRY | 10s | Yes |
| 500 | Server Error | RETRY | 0s | No |
| 503 | Service Unavailable | RETRY | 15s | No |

### Custom Error Messages
- **AUTH_001:** Invalid credentials → FAIL
- **RATE_LIMIT:** Too many requests → RETRY
- **Account locked:** Security lock → CUSTOM
- **Account suspended:** Banned account → BAN
- **Account deactivated:** Inactive account → CUSTOM
- **Subscription expired:** Expired subscription → CUSTOM
- **Region restricted:** Geo-blocked → BAN

## Quality Score Calculation

```
Algorithm:
  score = 0
  
  if subscription_status == "active":
    score += 3
  
  if is_premium == true:
    score += 2
  
  if payment_method exists:
    score += 2
  
  if device_count > 0:
    score += 1
  
  if expiry_date > current_time:
    score += 2
  
  return score
```

### Score Categories
- **10:** Maximum (all criteria met)
- **8-9:** HIGH QUALITY (premium active with payment)
- **6-7:** GOOD QUALITY (active with subscription)
- **4-5:** MEDIUM QUALITY (basic active account)
- **0-3:** LOW QUALITY (inactive or problematic)

## Security Considerations

### Anti-Bot Evasion Techniques
1. **Fingerprint Randomization:** Unique fingerprints per session
2. **Human Behavior Simulation:** Random delays between actions
3. **TLS Fingerprinting:** Mimics browser TLS signatures
4. **Header Randomization:** Varies timing-related headers
5. **Session Management:** Maintains cookies and session state
6. **User Agent Rotation:** Rotates user agents per check

### Best Practices
- Use high-quality residential proxies
- Enable all anti-bot features
- Monitor ban rates closely
- Respect rate limits
- Use appropriate delays

## Maintenance & Updates

### Version Control
- Current Version: 2.0.0
- Release Date: 2025-11-19
- Last Modified: 2025-11-19

### Future Enhancements
- Machine learning for quality prediction
- Advanced CAPTCHA handling
- Multi-region support
- Enhanced billing validation
- Real-time analytics

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-19  
**Maintained by:** legendhkek
