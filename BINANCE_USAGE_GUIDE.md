# Binance Email Validator - Usage Guide

## Quick Start Guide

This guide will help you get started with the Binance Advanced Email Validator configuration in OpenBullet.

## Prerequisites

Before you begin, make sure you have:
- ✅ OpenBullet 1.2.0 or higher (OpenBullet 2.x recommended)
- ✅ A wordlist with email:password combos
- ✅ Quality proxies (HTTP/HTTPS/SOCKS4/SOCKS5)
- ✅ (Optional) Captcha service account and API key

## Installation

### Step 1: Download Configuration
1. Download `BINANCE.COM.loli` from this repository
2. Place it in your OpenBullet configs folder

### Step 2: Load Configuration
1. Open OpenBullet
2. Go to **Configs** section
3. Click **Load Config**
4. Select `BINANCE.COM.loli`

### Step 3: Configuration Prompts
When you load the configuration, you'll see **6 prompts**. Answer them as follows:

#### Prompt 1: Select Proxy Type
```
Select Proxy Type (HTTP/HTTPS/SOCKS4/SOCKS5)
Default: HTTP
```
**Recommended:** SOCKS5 for best results, HTTPS for good balance

**Example answers:**
- `HTTP` - Standard HTTP proxies
- `HTTPS` - Secure HTTP proxies
- `SOCKS4` - SOCKS4 protocol
- `SOCKS5` - Most versatile option (recommended)

#### Prompt 2: Select Captcha Service
```
Select Captcha Service (2CAPTCHA/ANTICAPTCHA/CAPMONSTER/NONE)
Default: NONE
```
**Recommended:** Start with NONE, add service if you get many captcha challenges

**Example answers:**
- `NONE` - Don't use captcha service (faster, cheaper)
- `2CAPTCHA` - Use 2captcha.com ($2.99/1000 captchas)
- `ANTICAPTCHA` - Use anti-captcha.com ($2.00/1000 captchas)
- `CAPMONSTER` - Use capmonster.cloud ($1.00/1000 captchas, cheapest)

#### Prompt 3: Enter Captcha API Key
```
Enter your Captcha Service API Key (leave empty if NONE)
Default: (empty)
```
**If you selected a captcha service:**
- Enter your API key from the service
- Example: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6`

**If you selected NONE:**
- Just press Enter (leave empty)

#### Prompt 4: Use Advanced Anti-Bot Evasion
```
Use Advanced Anti-Bot Evasion? (YES/NO)
Default: YES
```
**Recommended:** YES for better success rates

**Example answers:**
- `YES` - Enable fingerprinting and evasion (recommended)
- `NO` - Disable advanced evasion (faster but lower success rate)

#### Prompt 5: Retry on Captcha Required
```
Retry on Captcha Required? (YES/NO)
Default: YES
```
**Recommended:** YES if you have captcha service configured, NO otherwise

**Example answers:**
- `YES` - Automatically retry with captcha solving
- `NO` - Fail immediately when captcha is required

#### Prompt 6: Maximum Captcha Retry Attempts
```
Maximum Captcha Retry Attempts
Default: 3
```
**Recommended:** 3 for good balance

**Example answers:**
- `1` - Single retry attempt
- `3` - Three retry attempts (recommended)
- `5` - Five retry attempts (higher success, slower)

## Configuration Examples

### Example 1: Fast Checking (No Captcha)
**Use Case:** Quick checking with good proxies, minimal captcha challenges

```
Proxy Type: SOCKS5
Captcha Service: NONE
Captcha API Key: (empty)
Advanced Evasion: YES
Retry on Captcha: NO
Max Retries: 3
```

**Settings:**
- Bots: 200-300
- Expected CPM: 250-300

### Example 2: Maximum Success Rate (With Captcha)
**Use Case:** Maximum success rate, willing to spend on captcha solving

```
Proxy Type: SOCKS5
Captcha Service: CAPMONSTER
Captcha API Key: your_api_key_here
Advanced Evasion: YES
Retry on Captcha: YES
Max Retries: 5
```

**Settings:**
- Bots: 50-100
- Expected CPM: 100-150

### Example 3: Budget-Friendly
**Use Case:** Good balance between speed and cost

```
Proxy Type: HTTPS
Captcha Service: NONE
Captcha API Key: (empty)
Advanced Evasion: YES
Retry on Captcha: NO
Max Retries: 3
```

**Settings:**
- Bots: 150-200
- Expected CPM: 200-250

## OpenBullet Settings

### Wordlist Configuration
1. **Wordlist Type:** Email:Password or Default
2. **Format:** `email:password`
   ```
   user1@example.com:password123
   user2@gmail.com:mypassword456
   binanceuser@yahoo.com:securepass789
   ```

### Proxy Configuration
1. **Proxy Type:** Match your selection in the prompts
2. **Proxy Format:**
   - HTTP: `ip:port` or `ip:port:user:pass`
   - SOCKS5: `ip:port` or `ip:port:user:pass`
3. **Proxy Sources:**
   - ✅ Residential proxies (best)
   - ✅ Premium datacenter proxies (good)
   - ❌ Free proxies (not recommended)

### Bot Configuration
**Starting Recommendations:**

| Scenario | Bots | CPM Limit |
|----------|------|-----------|
| No Captcha + Good Proxies | 200-300 | 300 |
| No Captcha + Average Proxies | 150-200 | 250 |
| With Captcha + Good Proxies | 50-100 | 150 |
| With Captcha + Average Proxies | 30-50 | 100 |

**Scaling Strategy:**
1. Start with lower bot count (50-100)
2. Monitor success rate and errors
3. Gradually increase if stable
4. Reduce if ban rate increases

## Captured Data

When a check is successful, you'll capture:

| Data Point | Description | Example |
|------------|-------------|---------|
| Email Verified | Email verification status | true/false |
| Email | Account email | user@example.com |
| Account Status | Account status | Active/Inactive |
| KYC Status | KYC verification level | Verified/Unverified |
| 2FA Enabled | Two-factor auth status | true/false |
| VIP Level | VIP tier level | 0-9 |
| Registration Date | Account creation date | 1635789012345 |
| Country | Account country | US |
| User ID | Binance user ID | 123456789 |
| Phone Verified | Phone verification status | true/false |
| Anti-Phishing Enabled | Anti-phishing code status | true/false |
| Withdrawal Whitelist | Whitelist status | true/false |

## Troubleshooting

### Problem: High Captcha Rate
**Symptoms:** Many accounts require captcha

**Solutions:**
1. Enable a captcha service (CapMonster is cheapest)
2. Set RETRY_ON_CAPTCHA to YES
3. Reduce bot count to lower request rate
4. Use better quality residential proxies

### Problem: High Ban Rate
**Symptoms:** Many proxies getting banned

**Solutions:**
1. Use residential proxies instead of datacenter
2. Reduce bot count
3. Enable advanced evasion (if not already)
4. Check proxy country (US, UK preferred)
5. Increase delay between checks

### Problem: Low CPM
**Symptoms:** Checks per minute is very low

**Causes & Solutions:**
- **Captcha enabled:** Normal, 20-30s added per captcha
  - Solution: Disable if not needed
- **Slow proxies:** Network latency
  - Solution: Use faster proxy service
- **Low bot count:** Not enough workers
  - Solution: Increase bot count gradually
- **API rate limiting:** Binance throttling
  - Solution: Spread checks over time, use more proxies

### Problem: CSRF Token Errors
**Symptoms:** "Failed to obtain CSRF token"

**Solutions:**
1. Check proxy connectivity to binance.com
2. Switch to different proxies
3. Verify Binance is accessible in your region
4. Try HTTPS or SOCKS5 proxies
5. Enable advanced evasion

### Problem: All Checks Failing
**Symptoms:** 100% failure rate

**Possible Causes:**
1. **Bad wordlist:** Check combo format (email:password)
2. **Blocked proxies:** All proxies banned
3. **Configuration error:** Check prompt answers
4. **Binance API change:** Page structure changed

**Solutions:**
1. Test with a known valid account
2. Try fresh proxies from different source
3. Reload config and re-enter prompts
4. Check repository for updates

## Performance Optimization

### For Speed (High CPM)
```
✓ Use SOCKS5 proxies
✓ Disable captcha service (set to NONE)
✓ Use 200-300 bots
✓ Use fast residential proxies
✓ Keep advanced evasion enabled
```

### For Success Rate
```
✓ Enable captcha service (CapMonster recommended)
✓ Set retry on captcha to YES
✓ Use high-quality residential proxies
✓ Start with 50-100 bots
✓ Monitor and adjust based on results
```

### For Cost Efficiency
```
✓ Start without captcha service
✓ Use 150-200 bots
✓ Monitor captcha requirement rate
✓ Add captcha service only if needed
✓ Use CapMonster if captcha needed (cheapest)
```

## Captcha Service Setup

### 2Captcha Setup
1. Go to [2captcha.com](https://2captcha.com)
2. Create account and add balance
3. Go to Settings → API Key
4. Copy your API key
5. Enter it in prompt 3

**Cost:** ~$2.99 per 1000 captchas

### Anti-Captcha Setup
1. Go to [anti-captcha.com](https://anti-captcha.com)
2. Create account and add balance
3. Go to Account → API Setup
4. Copy your API key
5. Enter it in prompt 3

**Cost:** ~$2.00 per 1000 captchas

### CapMonster Setup (Recommended)
1. Go to [capmonster.cloud](https://capmonster.cloud)
2. Create account and add balance
3. Go to Dashboard → API Key
4. Copy your API key
5. Enter it in prompt 3

**Cost:** ~$1.00 per 1000 captchas (cheapest)

## Best Practices

### ✅ DO
- Start with low bot count and scale up
- Use quality residential proxies
- Enable advanced evasion
- Monitor ban rates closely
- Keep proxy list fresh
- Check captcha service balance
- Only check accounts you own or have permission to check

### ❌ DON'T
- Use free proxies
- Start with maximum bots immediately
- Ignore high ban rates
- Share your captcha API key
- Check accounts without authorization
- Violate Binance Terms of Service

## Support

For issues or questions:
1. Check this usage guide
2. Read BINANCE_TECHNICAL_SPECS.md for detailed documentation
3. Check README.md for configuration overview
4. Report issues to the repository

## Legal Notice

This configuration is for **authorized testing only**. You must:
- ✅ Only check accounts you own or have permission to check
- ✅ Comply with Binance Terms of Service
- ✅ Follow applicable laws and regulations
- ✅ Use for legitimate security testing purposes

---

**Version:** 1.0.0  
**Last Updated:** 2025-11-20  
**Author:** legendhkek
