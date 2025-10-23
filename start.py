#!/usr/bin/env python3
"""
Startup script for the Discord Job Bot.
This script validates configuration and starts the bot.
"""
import sys
import os

def check_environment():
    """Check if required environment variables are set."""
    print("🔍 Checking environment configuration...")
    
    required_vars = [
        'DISCORD_BOT_TOKEN',
        'DISCORD_CHANNEL_ID',
        'OPENAI_API_KEY'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("\n❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n💡 Please create a .env file with your configuration.")
        print("   You can copy .env.example and fill in your values:")
        print("   cp .env.example .env")
        return False
    
    print("✅ All required environment variables are set")
    return True

def check_dependencies():
    """Check if required packages are installed."""
    print("\n🔍 Checking dependencies...")
    
    required_packages = {
        'discord': 'discord.py',
        'dotenv': 'python-dotenv',
        'openai': 'openai'
    }
    
    missing_packages = []
    for package, pip_name in required_packages.items():
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(pip_name)
    
    if missing_packages:
        print("\n❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n💡 Install missing packages with:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False
    
    print("✅ All required dependencies are installed")
    return True

def main():
    """Main startup function."""
    print("=" * 60)
    print("🤖 Discord Job Bot - Startup")
    print("=" * 60)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("\n🚀 Starting bot...")
    print("=" * 60)
    print()
    
    # Import and run the bot
    try:
        from bot import main as bot_main
        import asyncio
        asyncio.run(bot_main())
    except KeyboardInterrupt:
        print("\n\n👋 Bot stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error starting bot: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
