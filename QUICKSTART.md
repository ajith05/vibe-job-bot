# Quick Start Guide

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

3. **Configure your .env file with:**
   - Discord Bot Token (from https://discord.com/developers/applications)
   - Discord Channel ID (Enable Developer Mode in Discord, right-click channel)
   - OpenAI API Key (from https://platform.openai.com/api-keys)

## Running the Bot

### Option 1: Using the startup script (Recommended)
```bash
python start.py
```

### Option 2: Direct execution
```bash
python bot.py
```

## Discord Bot Setup

1. Go to https://discord.com/developers/applications
2. Create New Application
3. Navigate to "Bot" section
4. Create a bot and copy the token
5. Enable these Intents:
   - Message Content Intent
   - Server Members Intent (optional)
6. Generate invite URL:
   - Go to OAuth2 → URL Generator
   - Select scope: `bot`
   - Select permissions:
     - Send Messages
     - Embed Links
     - Read Messages/View Channels
7. Use the URL to invite bot to your server

## Getting Your Channel ID

1. Enable Developer Mode in Discord:
   - User Settings → Advanced → Developer Mode
2. Right-click on your target channel
3. Click "Copy ID"
4. Paste this ID in your .env file

## Bot Commands

Once running, use these commands in Discord:

- `!job check` - Manually search for new jobs
- `!job status` - View bot status and configuration  
- `!job help` - Show help message

## Configuration Options

Edit `.env` to customize:

- `CHECK_INTERVAL` - Seconds between automatic checks (default: 3600 = 1 hour)
- `JOB_KEYWORDS` - Comma-separated search terms (e.g., "python developer,software engineer")
- `MAX_JOBS_PER_CHECK` - Maximum jobs per search (default: 5)

## Troubleshooting

### Bot doesn't connect
- Verify `DISCORD_BOT_TOKEN` is correct
- Check bot is invited to your server
- Ensure required intents are enabled

### No jobs posted
- Verify `DISCORD_CHANNEL_ID` is correct
- Check bot has permission to post in the channel
- Ensure `OPENAI_API_KEY` is valid

### Rate limiting
- Increase `CHECK_INTERVAL` to reduce API calls
- Decrease `MAX_JOBS_PER_CHECK` to fetch fewer jobs

## Support

For issues or questions, please open an issue on GitHub.
