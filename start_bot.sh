#!/bin/bash
# Start script for Binance Telegram Bot

echo "=================================="
echo "Binance Telegram Bot Starter"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if requirements are installed
if ! python3 -c "import telegram" &> /dev/null; then
    echo ""
    echo "📦 Installing requirements..."
    pip3 install -r requirements.txt
    
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install requirements"
        exit 1
    fi
    echo "✅ Requirements installed"
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo ""
    echo "⚠️  Warning: .env file not found"
    echo "Creating from .env.example..."
    cp .env.example .env
    echo ""
    echo "❌ Please edit .env file and add your TELEGRAM_BOT_TOKEN"
    echo "Then run this script again."
    exit 1
fi

# Load .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Check if token is set
if [ -z "$TELEGRAM_BOT_TOKEN" ] || [ "$TELEGRAM_BOT_TOKEN" = "your_bot_token_here" ]; then
    echo ""
    echo "❌ Error: TELEGRAM_BOT_TOKEN not configured"
    echo "Please edit .env file and set your bot token"
    exit 1
fi

echo ""
echo "✅ Configuration loaded"
echo ""
echo "🚀 Starting Binance Telegram Bot..."
echo ""
echo "Press Ctrl+C to stop"
echo "=================================="
echo ""

# Start the bot
python3 binance_telegram_bot.py
