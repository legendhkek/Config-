# OpenBullet Configuration Repository

## 🎯 Repository Overview

This repository contains **professional account checker configurations** for OpenBullet 2, featuring real API requests, high performance, and comprehensive data extraction capabilities.

## 📦 Available Configurations

### 1. 🔐 Binance.com - Advanced Email Validator (NEW!)
**File:** `BINANCE.COM.loli`  
**Version:** 1.0.0  
**Category:** Cryptocurrency Exchange  
**Created:** 2025-11-20

Advanced email validator with comprehensive captcha support:
- **CPM**: 300 checks per minute
- **Bots**: 300 concurrent workers
- **Method**: Real API requests with anti-bot evasion
- **Data Capture**: Email verification status, account details, KYC status, 2FA status, VIP level
- **Format**: LoliCode/LoliScript

**Advanced Features:**
- **All Proxy Types Support**: HTTP, HTTPS, SOCKS4, SOCKS5
- **Multiple Captcha Services**: 
  - 2Captcha integration
  - Anti-Captcha integration
  - CapMonster integration
  - Configurable retry logic
- **Interactive Configuration**: Prompts for all settings on startup
  - Proxy type selection
  - Captcha service selection
  - API key configuration
  - Advanced evasion options
  - Retry behavior settings
- **Advanced Anti-Bot Evasion**:
  - Canvas fingerprinting
  - WebGL fingerprinting
  - Audio fingerprinting
  - Device fingerprinting
  - Session management
- **Comprehensive Data Extraction**:
  - Email verification status
  - Account status
  - KYC verification level
  - 2FA status
  - VIP level
  - Registration date
  - Country
  - Phone verification
  - Anti-phishing settings
  - Withdrawal whitelist status
- **Smart Error Handling**:
  - Automatic retry on rate limits
  - Captcha retry logic
  - CSRF token refresh
  - Session recovery

**Configuration Prompts:**
When you load this configuration, you'll be prompted for:
1. **Proxy Type**: Choose between HTTP, HTTPS, SOCKS4, or SOCKS5
2. **Captcha Service**: Select 2CAPTCHA, ANTICAPTCHA, CAPMONSTER, or NONE
3. **Captcha API Key**: Enter your captcha service API key (if applicable)
4. **Advanced Evasion**: Enable/disable advanced anti-bot techniques
5. **Retry on Captcha**: Configure automatic retry behavior
6. **Max Captcha Retries**: Set maximum retry attempts for captcha solving

**Usage Tips:**
- Use high-quality residential proxies for best results
- Configure your captcha service API key for automatic captcha solving
- Enable advanced evasion for better success rates
- Start with 100-150 bots and scale up based on proxy quality
- Monitor captcha retry count to optimize performance

### 2. ✈️ Lufthansa.com - Miles & More (NEW!)
**File:** `LUFTHANSA.COM.loli`  
**Version:** 1.0.0  
**Category:** Airlines  
**Created:** 2025-11-20

Real API-based Miles & More account checker:
- **CPM**: 200 checks per minute
- **Bots**: 200 concurrent workers
- **Method**: Direct API requests (no browser)
- **Data Capture**: Member number, status level, miles balance, name, email
- **Format**: LoliCode/LoliScript

**Features:**
- OAuth2 authentication
- Profile data extraction
- Miles balance retrieval
- Status tier detection

### 3. ✈️ British Airways - Executive Club (NEW!)
**File:** `BRITISHAIRWAYS.COM.loli`  
**Version:** 1.0.0  
**Category:** Airlines  
**Created:** 2025-11-20

Real API-based Executive Club account checker:
- **CPM**: 200 checks per minute
- **Bots**: 200 concurrent workers
- **Method**: Direct API requests (no browser)
- **Data Capture**: Membership number, tier level, Avios balance, name, email
- **Format**: LoliCode/LoliScript

**Features:**
- Session-based authentication
- Executive Club profile data
- Avios balance capture
- Tier status detection (Blue/Bronze/Silver/Gold)

### 4. 📺 Sky.com - Advanced Account Checker Pro (TLS Edition)
**File:** `sky.com.opk`  
**Version:** 2.1.0  
**Category**: Streaming  
**Updated:** 2025-11-19

Enterprise-grade checker with advanced TLS 1.3 fingerprinting:
- **CPM**: 500 checks per minute
- **Bots**: 500 concurrent workers
- **Security**: TLS 1.3, modern cipher suites, GREASE support
- **Data Capture**: Subscription, billing, profile, devices
- **Format**: OpenBullet (OPK) with LoliScript

---

# Sky.com Advanced Account Checker Pro - TLS Edition - Configuration Guide

## Overview

This is an **enterprise-grade** Sky.com account checker configuration designed for OpenBullet with **advanced TLS 1.3 fingerprinting** and comprehensive SSL/TLS security features. Includes intelligent retry mechanisms, comprehensive data extraction, anti-bot evasion, session management, 2FA detection, proxy health monitoring, and performance optimizations. **Full OPK format support with TLS.**

**Version:** 2.1.0  
**Author:** legendhkek  
**Category:** Streaming  
**Last Updated:** 2025-11-19

### 🔐 TLS Edition Highlights

- **TLS 1.3** with automatic fallback to TLS 1.2/1.1
- **Modern Cipher Suites** (7 secure algorithms)
- **GREASE Support** for anti-fingerprinting
- **Perfect Forward Secrecy** (ECDHE with 384-bit curves)
- **Session Resumption** for faster connections
- **OCSP Stapling** for certificate validation
- **ALPN Negotiation** (HTTP/2 preferred)
- **15 TLS Extensions** mimicking Chrome 120
- **OPK Format** with full TLS integration

## Key Features

### 🔐 Advanced TLS/SSL Security (NEW in v2.1)
- **TLS Version:** TLS 1.3 (primary) with fallback to TLS 1.2 and TLS 1.1
- **Fingerprint Profile:** Chrome 120 Modern browser emulation
- **Cipher Suites:** 7 modern, secure cipher algorithms including:
  - TLS_AES_128_GCM_SHA256
  - TLS_AES_256_GCM_SHA384
  - TLS_CHACHA20_POLY1305_SHA256
  - ECDHE_ECDSA with AES-GCM
  - ECDHE_RSA with AES-GCM
- **Signature Algorithms:** 8 algorithms (ECDSA, RSA-PSS, RSA-PKCS1)
- **Supported Groups:** x25519, secp256r1, secp384r1
- **ALPN Protocols:** HTTP/2 (h2) with HTTP/1.1 fallback
- **Perfect Forward Secrecy:** Enabled with ECDHE curve secp384r1
- **Session Tickets:** Enabled for session resumption
- **OCSP Stapling:** Enabled for certificate validation
- **SNI (Server Name Indication):** Enabled
- **TLS Extensions:** 15 extensions including:
  - server_name, extended_master_secret
  - supported_groups, key_share
  - signature_algorithms, status_request (OCSP)
  - application_layer_protocol_negotiation
  - psk_key_exchange_modes, compress_certificate
  - application_settings (HTTP/2 settings)
- **GREASE:** Enabled (cipher suite, extension, version randomization)
- **Extension Order Randomization:** Enabled for anti-fingerprinting
- **TLS 1.3 0-RTT:** Disabled for security
- **Certificate Verification:** Strict (no self-signed)
- **DHE Key Size:** 2048-bit minimum
- **Record Size Limit:** 16384 bytes

### 🚀 Performance Optimizations
- **CPM:** 500 (Checks Per Minute)
- **Bots:** 500 concurrent workers
- **Concurrent Requests:** 500 simultaneous connections
- **Connection Pooling:** 200 connections with 50 per host
- **HTTP/2 Support:** Enabled for faster multiplexed requests
- **HTTP Pipelining:** Depth of 5 for optimized request batching
- **Request/Response Compression:** Enabled for bandwidth optimization

### 🔒 Security & Anti-Bot Evasion
- **TLS Fingerprinting:** Mimics real browser TLS signatures
- **Fingerprint Randomization:** Canvas, WebGL, and Audio fingerprints
- **User Agent Rotation:** Dynamic UA switching
- **Header Randomization:** Randomized timing headers
- **Human Behavior Simulation:** Random delays (500-3000ms)
- **Device Fingerprinting:** Unique device IDs per session

### 🔄 Advanced Retry Logic
- **Exponential Backoff:** 2x multiplier, max 60s delay
- **Circuit Breaker:** Stops after 10 consecutive failures (30s timeout)
- **Smart Retry:** Context-aware retry decisions
- **Max Retries:** 5 attempts with intelligent backoff
- **Request Deduplication:** Prevents duplicate requests

### 🌐 Proxy Management
- **Rotation Strategy:** Round-robin with health checks
- **Health Monitoring:** 60-second interval checks
- **Proxy Scoring:** Quality-based proxy selection
- **Auto-Ban:** Ban after 5 consecutive failures
- **Geo Validation:** Supports US, UK, CA, AU, IE
- **IP Reputation:** Minimum score 7.5/10
- **Sticky Sessions:** 5-minute session persistence

### 🧵 Advanced Threading
- **Dynamic Threading:** Auto-scales from 100 to 500 threads
- **Work Stealing:** Load balancing across threads
- **Thread Affinity:** CPU core optimization
- **Priority Queue:** Critical requests processed first
- **Queue Size:** 5,000 items

### 📊 Rate Limiting
- **Adaptive Rate Limiting:** Adjusts based on response patterns
- **Token Bucket Algorithm:** 10 tokens/sec, 1000 max
- **Burst Support:** 100 requests in 5 seconds
- **Sliding Window:** 60-second window tracking
- **Backoff on Error:** 30% reduction on rate limit detection

### 💾 Caching & Session Management
- **Response Cache:** 5-minute TTL, 1000 items max
- **DNS Cache:** 1-hour TTL for faster lookups
- **Session Persistence:** 15-minute timeout
- **Cookie Jar:** Full cookie management
- **Session Recovery:** Automatic recovery with 3 retries

### 📈 Data Extraction

The configuration captures comprehensive account information:

#### Profile Data
- Email address
- First name
- Last name
- Phone number
- Country

#### Subscription Details
- Subscription type
- Subscription status (active/inactive)
- Expiry date
- Premium status
- Price
- Available channels
- Active addons
- Next billing date

#### Billing Information
- Payment method
- Card last 4 digits
- Account balance

#### Device Information
- Device count
- Device types

#### Authentication Tokens
- Auth token
- Refresh token
- User ID

### 🎯 Account Quality Scoring

The config includes an intelligent quality scoring system (0-10 scale):

- **HIGH QUALITY (8-10):** Premium active accounts with payment methods
  - Active subscription: +3 points
  - Premium account: +2 points
  - Payment method on file: +2 points
  - Valid expiry date: +2 points
  - Registered devices: +1 point

- **GOOD QUALITY (6-7):** Active accounts with subscription
- **MEDIUM QUALITY (4-5):** Basic active accounts
- **LOW QUALITY (0-3):** Inactive or problematic accounts

### 🛡️ Error Handling

Advanced error detection and handling:

- **Invalid Credentials** → FAIL
- **Account Locked** → CUSTOM (security lock)
- **Account Suspended** → BAN
- **Account Deactivated** → CUSTOM
- **Subscription Expired** → CUSTOM
- **Region Restricted** → BAN
- **Rate Limited** → RETRY (with backoff)
- **2FA Required** → CUSTOM (valid credentials noted)
- **IP Blocked** → BAN proxy
- **Server Error (500/503)** → RETRY

### 📝 Logging & Debugging

- **Log Level:** DEBUG
- **Request/Response Headers:** Logged
- **Response Body:** Logged
- **Performance Metrics:** Enabled
- **Error Tracking:** Comprehensive error logs

## Configuration Structure

### File: `sky.com.opk`

The configuration is structured in JSON format with the following sections:

1. **Metadata:** Name, version, author, description
2. **Settings:** All configuration parameters
   - General settings
   - Proxy settings
   - Threading configuration
   - Rate limiting
   - Multi-request settings
   - Session management
   - Cache settings
   - Security settings
   - Validation settings
   - Logging settings
3. **Script:** LoliScript blocks defining the check workflow
4. **ConfigSpecs:** Summary of capabilities and features

## Workflow

### 1. Initialization Phase
- Generate unique session ID
- Create device fingerprint
- Set request timestamp

### 2. Connection Phase
- Preflight HEAD request to test connectivity
- Human-like delay (800-2000ms)

### 3. Authentication Setup
- GET request to sign-in page
- Parse CSRF token, session ID, API key, client ID
- Set session cookies
- Simulate form fill time (1200-2500ms)

### 4. Login Request
- POST to authentication endpoint
- Include device fingerprint and session data
- Parse response for success, auth tokens, 2FA requirement

### 5. Validation Phase (if successful)
- Page transition delay (500-1500ms)
- Request user profile
- Request subscription details
- Request billing information
- Request device information

### 6. Quality Assessment
- Calculate account quality score
- Categorize account (HIGH/GOOD/MEDIUM/LOW)

### 7. Result Classification
- SUCCESS: Valid, active account
- FAIL: Invalid credentials
- CUSTOM: Special cases (2FA, locked, deactivated, expired)
- BAN: Proxy/IP issues, suspended accounts
- RETRY: Temporary errors

## Usage

### Input Format
The configuration expects credentials in the format:
```
email:password
```

Example:
```
user@example.com:MyPassword123
john.doe@sky.com:SecurePass456
```

### Proxy Configuration
Proxies are **required** for this configuration. Supported formats:
- HTTP/HTTPS proxies
- SOCKS4/SOCKS5 proxies (if OnlySocks is enabled)

Recommended proxy locations: US, UK, CA, AU, IE

### OpenBullet Settings
When loading this configuration in OpenBullet:

1. **Wordlist Type:** Email:Password or Credentials
2. **Proxy Type:** HTTP/HTTPS recommended
3. **Bots:** Start with 100-200, scale up to 500 based on proxy quality
4. **Capture Settings:** Enable all captures to get full account data

> **Import Tip:** Use the `sky.com.opk` file in this repository when importing into OpenBullet. Older downloads with the `.opk.txt` suffix will not appear in the OpenBullet file picker.

## Performance Tips

1. **Start Conservative:** Begin with 100-200 bots and scale up
2. **Quality Proxies:** Use high-quality, residential proxies for best results
3. **Monitor Rate Limits:** The config handles rate limiting, but use appropriate delays
4. **Proxy Rotation:** Enable proxy rotation for sustained high-speed checking
5. **Connection Pooling:** Enabled by default for optimal performance

## Troubleshooting

### High Ban Rate
- Check proxy quality (should have reputation score >7.5)
- Reduce bot count temporarily
- Ensure proxies are from allowed countries

### Low CPM
- Increase bot count (up to 500)
- Check proxy speed and health
- Verify threading is enabled
- Check for network latency

### Frequent Retries
- May indicate rate limiting - reduce CPM temporarily
- Check proxy IP reputation
- Verify circuit breaker isn't triggering

### No Data Captured
- Check that "SaveEmptyCaptures" is false
- Verify authentication is successful
- Check network connectivity to Sky.com API endpoints

## Advanced Features Summary

### TLS/SSL Security (NEW)
✅ TLS 1.3 Fingerprinting  
✅ Modern Cipher Suites (7 algorithms)  
✅ GREASE Support  
✅ ALPN Negotiation (HTTP/2)  
✅ Perfect Forward Secrecy  
✅ Session Resumption  
✅ OCSP Stapling  
✅ SNI Support  
✅ 15 TLS Extensions  
✅ Extension Order Randomization  
✅ Chrome 120 Browser Emulation  

### Core Features
✅ Exponential Backoff  
✅ Circuit Breaker  
✅ Connection Pooling  
✅ Anti-Bot Evasion  
✅ Fingerprint Randomization  
✅ Session Management  
✅ 2FA Detection  
✅ Account Quality Scoring  
✅ Geo Validation  
✅ Smart Retry Logic  
✅ Proxy Health Monitoring  
✅ Dynamic Threading  
✅ Adaptive Rate Limiting  
✅ JSON Schema Validation  
✅ Comprehensive Data Extraction  
✅ Multi-Stage Authentication  
✅ Device Fingerprinting  
✅ Token Refresh Support  
✅ Billing Data Capture  
✅ Subscription Validation  

## Security Notice

This configuration is intended for **authorized testing and validation purposes only**. Users are responsible for:
- Complying with Sky.com Terms of Service
- Obtaining proper authorization
- Following applicable laws and regulations
- Using appropriate rate limits
- Respecting privacy and data protection laws

## Support & Updates

For issues, suggestions, or contributions:
- **Author:** legendhkek
- **Repository:** Config-
- **Version:** 2.0.0

## Changelog

### Version 2.1.0 (2025-11-19) - TLS Edition
- **NEW: Advanced TLS 1.3 Configuration**
  - TLS 1.3 with automatic fallback to 1.2/1.1
  - Chrome 120 Modern fingerprint profile
  - 7 modern cipher suites (AES-GCM, ChaCha20-Poly1305)
  - 8 signature algorithms (ECDSA, RSA-PSS, RSA-PKCS1)
  - 3 supported groups (x25519, secp256r1, secp384r1)
  - ALPN protocol negotiation (HTTP/2 preferred)
  - Perfect Forward Secrecy with ECDHE secp384r1
  - Session resumption and session tickets
  - OCSP stapling for certificate validation
  - SNI (Server Name Indication) support
  - 15 TLS extensions for realistic fingerprint
  - GREASE enabled (cipher, extension, version randomization)
  - Extension order randomization
  - Strict certificate verification
  - 2048-bit DHE minimum key size
- **OPK Format:** Full support with TLS integration
- Renamed to "Sky.com Advanced Account Checker Pro - TLS Edition"
- Updated metadata and version to 2.1.0

### Version 2.0.0 (2025-11-19)
- Complete rewrite with enterprise-grade features
- Increased CPM from 200 to 500
- Increased concurrent workers from 200 to 500
- Added exponential backoff and circuit breaker
- Implemented connection pooling (HTTP/2, pipelining)
- Added comprehensive anti-bot evasion
- Enhanced proxy management with health checks and scoring
- Implemented dynamic threading with work stealing
- Added adaptive rate limiting with token bucket
- Enhanced session management and caching
- Added account quality scoring system
- Expanded data extraction (profile, subscription, billing, devices)
- Improved error handling with smart retry logic
- Added 2FA detection
- Enhanced logging and debugging capabilities

### Version 1.0.0 (2025-11-19)
- Initial release with basic features
- CPM 200, Bots 200
- Basic authentication flow
- Simple data capture

---

**Built with ❤️ for advanced account checking**
