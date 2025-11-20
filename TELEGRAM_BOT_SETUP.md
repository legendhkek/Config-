# Binance Email Validator - Telegram Bot Setup Guide

## 🤖 Overview

This advanced Telegram bot provides a user-friendly interface for checking Binance accounts with extensive proxy and captcha support.

## ✨ Features

### Core Functionality
- ✅ **Interactive Telegram Interface** - Easy-to-use menu system
- ✅ **All Proxy Types** - HTTP, HTTPS, SOCKS4, SOCKS5, Residential, Datacenter, Rotating
- ✅ **10 Captcha Services** - 2Captcha, Anti-Captcha, CapMonster, DeathByCaptcha, ImageTyperz, AZCaptcha, CaptchaCoder, CapSolver, TrueCaptcha
- ✅ **Real-time Progress** - Live updates during checking
- ✅ **Multi-threading** - Configurable concurrent checks (1-50 threads)
- ✅ **Result Export** - Automatic export to text files
- ✅ **Session Management** - Per-user configuration storage
- ✅ **Advanced Error Handling** - Automatic retry and error recovery

### Advanced Features
- 🛡️ **Anti-Bot Evasion** - Toggle advanced fingerprinting
- 🔄 **Smart Retry Logic** - Configurable captcha retry attempts
- 📊 **Statistics Tracking** - CPM, success rate, and more
- 💾 **Data Extraction** - Email verified, KYC status, 2FA, VIP level, country
- 🔐 **Secure** - API keys stored per-session only

## 📋 Prerequisites

### System Requirements
- Python 3.8 or higher
- 2GB RAM minimum (4GB recommended)
- Internet connection
- Linux/Mac/Windows

### Required Accounts
1. **Telegram Bot Token** (Required)
   - Get from [@BotFather](https://t.me/BotFather)
   
2. **Captcha Service API Key** (Optional but recommended)
   - [2Captcha](https://2captcha.com) - $2.99/1000 solves
   - [Anti-Captcha](https://anti-captcha.com) - $2.00/1000 solves
   - [CapMonster](https://capmonster.cloud) - $1.00/1000 solves (cheapest)
   - [DeathByCaptcha](https://deathbycaptcha.com) - $1.39/1000 solves
   - [ImageTyperz](https://www.imagetyperz.com) - $1.50/1000 solves
   - [AZCaptcha](https://azcaptcha.com) - $1.00/1000 solves
   - [CaptchaCoder](https://www.captchacoder.com) - $1.50/1000 solves
   - [CapSolver](https://www.capsolver.com) - $0.80/1000 solves
   - [TrueCaptcha](https://truecaptcha.org) - $1.00/1000 solves

## 🚀 Installation

### Step 1: Install Python Dependencies

```bash
# Clone or download the repository
cd /path/to/Config-

# Install required packages
pip install -r requirements.txt
```

### Step 2: Get Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the prompts:
   - Choose a name for your bot (e.g., "My Binance Checker")
   - Choose a username (must end in 'bot', e.g., "mybinance_checker_bot")
4. Copy the bot token (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)
5. Save it securely - you'll need it to run the bot

### Step 3: Configure Environment

#### Option A: Using Environment Variable (Recommended)

**Linux/Mac:**
```bash
export TELEGRAM_BOT_TOKEN='your_bot_token_here'
```

**Windows (Command Prompt):**
```cmd
set TELEGRAM_BOT_TOKEN=your_bot_token_here
```

**Windows (PowerShell):**
```powershell
$env:TELEGRAM_BOT_TOKEN='your_bot_token_here'
```

#### Option B: Using .env File

Create a file named `.env` in the same directory as the bot:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

### Step 4: Run the Bot

```bash
python3 binance_telegram_bot.py
```

You should see:
```
INFO - Starting Binance Telegram Bot...
INFO - Application started
```

## 📱 Using the Bot

### Initial Setup

1. **Start the bot** in Telegram by searching for your bot's username
2. Send `/start` command
3. You'll see the main menu with options

### Workflow

#### 1️⃣ Upload Combo List

**Format:** `email:password` (one per line)

**Example:**
```
user1@example.com:password123
user2@gmail.com:mypass456
binance@yahoo.com:secure789
```

**Methods:**
- Upload as .txt file
- Paste directly in chat

#### 2️⃣ Upload Proxy List

**Format:** `ip:port` or `ip:port:user:pass` (one per line)

**Example:**
```
192.168.1.1:8080
proxy.example.com:3128:myuser:mypass
10.0.0.1:1080
```

**Methods:**
- Upload as .txt file
- Paste directly in chat

#### 3️⃣ Configure Settings

**Available Options:**

| Setting | Description | Options |
|---------|-------------|---------|
| **Proxy Type** | Protocol to use | HTTP, HTTPS, SOCKS4, SOCKS5, Residential, Datacenter, Rotating |
| **Proxy Category** | Quality tracking | Residential, Datacenter, Mobile, Rotating |
| **Captcha Service** | Solving service | NONE, 2Captcha, Anti-Captcha, CapMonster, DeathByCaptcha, ImageTyperz, AZCaptcha, CaptchaCoder, CapSolver, TrueCaptcha |
| **Captcha API Key** | Your service key | Your API key string (some services need user:key format) |
| **Advanced Evasion** | Anti-bot features | ON/OFF |
| **Retry on Captcha** | Auto-retry | YES/NO |
| **Proxy Rotation** | Rotate proxies | ON/OFF |
| **Max Retries** | Retry limit | 1-10 |
| **Max Threads** | Concurrent checks | 1-50 (default: 10) |

**Recommended Settings:**

**Fast Checking (No Captcha):**
```
Proxy Type: SOCKS5
Captcha Service: NONE
Advanced Evasion: ON
Max Threads: 20
```

**High Success Rate (With Captcha):**
```
Proxy Type: SOCKS5
Captcha Service: CapMonster (cheapest)
Captcha API Key: your_key
Advanced Evasion: ON
Retry on Captcha: YES
Max Retries: 3
Max Threads: 10
```

#### 4️⃣ Start Checking

1. Click "▶️ Start Checking"
2. Review configuration summary
3. Click "✅ Start Now"
4. Monitor progress with `/status` command

#### 5️⃣ View Results

- Results are displayed in real-time
- Detailed results exported to file automatically
- Contains:
  - Email and password
  - Email verification status
  - KYC status
  - 2FA enabled/disabled
  - VIP level
  - Country
  - Account status

## 🎛️ Commands

| Command | Description |
|---------|-------------|
| `/start` | Start bot and show main menu |
| `/status` | Check current checking progress |
| `/cancel` | Cancel current operation |
| `/help` | Show help message |

## 📊 Understanding Results

### Result Statuses

| Status | Meaning | Action |
|--------|---------|--------|
| **Valid** ✅ | Credentials work | Account details captured |
| **Invalid** ❌ | Wrong credentials | Not saved |
| **Error** ⚠️ | Technical issue | Review error message |

### Captured Data Points

For valid accounts, the bot captures:

1. ✅ **Email Verified** - Email verification status
2. 🆔 **KYC Status** - Verification level (Verified/Unverified/Pending)
3. 🔐 **2FA Enabled** - Two-factor authentication status
4. ⭐ **VIP Level** - VIP tier (0-9)
5. 🌍 **Country** - Account country
6. 📊 **Account Status** - Active/Inactive/Suspended
7. 📱 **Phone Verified** - Phone verification status
8. 📅 **Registration Date** - When account was created

## 🔧 Advanced Configuration

### Proxy Recommendations

| Proxy Type | Speed | Success Rate | Cost | Recommended |
|------------|-------|--------------|------|-------------|
| Residential SOCKS5 | Fast | Very High | High | ⭐⭐⭐⭐⭐ |
| Residential HTTP | Fast | High | High | ⭐⭐⭐⭐ |
| Datacenter SOCKS5 | Very Fast | Medium | Low | ⭐⭐⭐ |
| Datacenter HTTP | Very Fast | Low | Very Low | ⭐⭐ |
| Free Proxies | Slow | Very Low | Free | ❌ Not Recommended |

### Thread Configuration

| Threads | Use Case | Proxy Requirement | Expected CPM |
|---------|----------|-------------------|--------------|
| 1-5 | Testing/Slow proxies | Any | 10-50 |
| 5-10 | Normal checking | Good quality | 50-150 |
| 10-20 | Fast checking | High quality | 150-250 |
| 20-50 | Maximum speed | Premium quality | 250-400 |

**Note:** Without captcha solving, CPM can be 2-3x higher.

### Captcha Service Comparison

| Service | Cost/1000 | Speed | Success Rate | API Docs |
|---------|-----------|-------|--------------|----------|
| **CapMonster** | $1.00 | Fast | High | [Link](https://capmonster.cloud/api) |
| **Anti-Captcha** | $2.00 | Very Fast | Very High | [Link](https://anti-captcha.com/apidoc) |
| **2Captcha** | $2.99 | Fast | Very High | [Link](https://2captcha.com/api-docs) |

**Recommendation:** Start with CapMonster for best cost/performance ratio.

## ⚠️ Troubleshooting

### Bot Won't Start

**Problem:** `TELEGRAM_BOT_TOKEN environment variable not set!`

**Solution:**
```bash
# Set the token
export TELEGRAM_BOT_TOKEN='your_token_here'

# Or create .env file
echo "TELEGRAM_BOT_TOKEN=your_token_here" > .env
```

### High Error Rate

**Possible Causes:**
1. Bad proxy quality
2. Rate limiting
3. Binance API changes

**Solutions:**
1. Use better quality proxies (residential recommended)
2. Reduce thread count
3. Enable "Retry on Captcha"
4. Check if proxies are working with other services

### Low CPM

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Captcha solving enabled | Adds 20-30s per check - disable if not needed |
| Slow proxies | Use faster proxy service |
| Low thread count | Increase threads (10-20 recommended) |
| Network latency | Use proxies closer to Binance servers |

### Captcha Not Solving

**Check:**
1. ✅ API key is correct
2. ✅ Sufficient balance in captcha service
3. ✅ Service is selected (not NONE)
4. ✅ Internet connection stable

**Test API Key:**
```bash
# 2Captcha
curl "http://2captcha.com/res.php?key=YOUR_KEY&action=getbalance"

# Anti-Captcha
curl -X POST https://api.anti-captcha.com/getBalance \
  -H "Content-Type: application/json" \
  -d '{"clientKey":"YOUR_KEY"}'
```

### Bot Not Responding

**Solutions:**
1. Restart the bot
2. Check internet connection
3. Verify bot token is valid
4. Check Python process is running:
   ```bash
   ps aux | grep binance_telegram_bot
   ```

## 📈 Performance Optimization

### For Maximum Speed

```
✅ Use SOCKS5 proxies (fastest)
✅ Set captcha to NONE (if possible)
✅ Use 20-30 threads
✅ Use high-speed residential proxies
✅ Enable advanced evasion (prevents bans)
```

**Expected:** 250-400 CPM

### For Maximum Success Rate

```
✅ Use residential SOCKS5 proxies
✅ Enable captcha service (CapMonster)
✅ Use 5-10 threads
✅ Enable advanced evasion
✅ Enable retry on captcha
✅ Set max retries to 3-5
```

**Expected:** 100-150 CPM, 80-90% success rate

### For Cost Efficiency

```
✅ Start without captcha
✅ Use 10-15 threads
✅ Monitor captcha requirement rate
✅ Add captcha service only if needed
✅ Use CapMonster if captcha needed
```

**Expected:** 200-250 CPM, balanced costs

## 🔒 Security Best Practices

### ✅ DO:
- Keep your bot token private
- Use environment variables for sensitive data
- Run bot on secure server/VPS
- Use quality, trusted proxies
- Monitor bot activity
- Only check accounts you own or have permission to check

### ❌ DON'T:
- Share your bot token publicly
- Hardcode API keys in scripts
- Use free/public proxies for sensitive checks
- Run on shared/untrusted computers
- Share captcha API keys
- Check accounts without authorization

## 🐛 Error Messages

| Error | Meaning | Solution |
|-------|---------|----------|
| `Failed to get CSRF token` | Can't connect to Binance | Check proxy, try different one |
| `Request timeout` | Slow connection | Use faster proxies, reduce threads |
| `Invalid credentials` | Wrong email/password | Normal - combo is invalid |
| `Captcha required` | Binance wants captcha | Enable captcha service |
| `No valid combos found` | Bad format | Check combo format (email:password) |
| `No valid proxies found` | Bad format | Check proxy format (ip:port) |

## 📞 Support & Updates

### Getting Help

1. **Read this guide** first
2. **Check troubleshooting** section
3. **Review error messages** for clues
4. **Test with known working combo** to isolate issue

### Reporting Issues

When reporting issues, include:
- Python version (`python --version`)
- Bot version (from bot file header)
- Error message (full text)
- Steps to reproduce
- Configuration used (without API keys)

## 📄 File Structure

```
Config-/
├── binance_telegram_bot.py      # Main bot script
├── requirements.txt              # Python dependencies
├── TELEGRAM_BOT_SETUP.md        # This file
├── BINANCE.COM.loli             # OpenBullet config
├── BINANCE_TECHNICAL_SPECS.md   # Technical documentation
├── BINANCE_USAGE_GUIDE.md       # Usage guide
└── .env                         # Environment variables (create this)
```

## 🚀 Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Telegram bot created with @BotFather
- [ ] Bot token saved in environment or .env file
- [ ] (Optional) Captcha service account created
- [ ] (Optional) Captcha API key obtained
- [ ] Bot script started (`python3 binance_telegram_bot.py`)
- [ ] Bot opened in Telegram
- [ ] Combos uploaded
- [ ] Proxies uploaded
- [ ] Settings configured
- [ ] Ready to check!

## 🎓 Example Session

```
1. Upload combos (100 accounts)
2. Upload proxies (20 SOCKS5)
3. Configure:
   - Proxy Type: SOCKS5
   - Captcha: CapMonster
   - API Key: your_key
   - Threads: 10
4. Start checking
5. Monitor with /status
6. Results:
   - 100 checked in 5 minutes
   - 15 valid accounts found
   - File exported automatically
7. Done!
```

## 📚 Additional Resources

- **OpenBullet Config:** See `BINANCE.COM.loli` for standalone checking
- **Technical Docs:** See `BINANCE_TECHNICAL_SPECS.md` for API details
- **Usage Guide:** See `BINANCE_USAGE_GUIDE.md` for OpenBullet usage

## ⚖️ Legal Notice

This bot is for **authorized testing only**. Users must:
- ✅ Only check accounts they own or have permission to check
- ✅ Comply with Binance Terms of Service
- ✅ Follow applicable laws and regulations
- ✅ Use for legitimate security testing purposes

**Unauthorized access to computer systems is illegal.**

---

**Version:** 1.0.0  
**Last Updated:** 2025-11-20  
**Author:** legendhkek  
**License:** For authorized use only
