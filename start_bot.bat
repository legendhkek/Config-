@echo off
REM Start script for Binance Telegram Bot (Windows)

echo ==================================
echo Binance Telegram Bot Starter
echo ==================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo [OK] Python found
python --version

REM Check if requirements are installed
python -c "import telegram" >nul 2>&1
if errorlevel 1 (
    echo.
    echo [INFO] Installing requirements...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Failed to install requirements
        pause
        exit /b 1
    )
    echo [OK] Requirements installed
)

REM Check if .env file exists
if not exist .env (
    echo.
    echo [WARNING] .env file not found
    echo Creating from .env.example...
    copy .env.example .env
    echo.
    echo [ERROR] Please edit .env file and add your TELEGRAM_BOT_TOKEN
    echo Then run this script again.
    pause
    exit /b 1
)

REM Load .env file (simple version for Windows)
for /f "tokens=1,2 delims==" %%a in (.env) do (
    if not "%%a"=="" if not "%%b"=="" (
        set %%a=%%b
    )
)

REM Check if token is set
if "%TELEGRAM_BOT_TOKEN%"=="" (
    echo.
    echo [ERROR] TELEGRAM_BOT_TOKEN not configured
    echo Please edit .env file and set your bot token
    pause
    exit /b 1
)

if "%TELEGRAM_BOT_TOKEN%"=="your_bot_token_here" (
    echo.
    echo [ERROR] TELEGRAM_BOT_TOKEN not configured
    echo Please edit .env file and set your bot token
    pause
    exit /b 1
)

echo.
echo [OK] Configuration loaded
echo.
echo Starting Binance Telegram Bot...
echo.
echo Press Ctrl+C to stop
echo ==================================
echo.

REM Start the bot
python binance_telegram_bot.py

pause
