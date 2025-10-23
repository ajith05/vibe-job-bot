# Vibe Job Bot 🤖

A Discord bot that automatically crawls and posts job openings using Generative AI. The bot uses OpenAI's GPT to discover and format job postings, then sends them as notifications to your Discord channel.

## Features ✨

- 🔍 **AI-Powered Job Discovery**: Uses OpenAI's GPT to find and format job postings
- 📢 **Discord Notifications**: Sends formatted job postings to a specified Discord channel
- ⏰ **Automated Scheduling**: Checks for new jobs at configurable intervals
- 🎯 **Customizable Keywords**: Search for jobs based on your preferred keywords
- 🚫 **Duplicate Prevention**: Tracks and filters out previously posted jobs
- 💬 **Bot Commands**: Manual job checks and status monitoring

## Prerequisites 📋

- Python 3.8 or higher
- Discord Bot Token ([Create a bot](https://discord.com/developers/applications))
- OpenAI API Key ([Get API key](https://platform.openai.com/api-keys))
- Discord Channel ID where jobs will be posted

## Installation 🚀

1. **Clone the repository**
   ```bash
   git clone https://github.com/ajith05/vibe-job-bot.git
   cd vibe-job-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and fill in your credentials:
   ```env
   DISCORD_BOT_TOKEN=your_discord_bot_token_here
   DISCORD_CHANNEL_ID=your_channel_id_here
   OPENAI_API_KEY=your_openai_api_key_here
   CHECK_INTERVAL=3600
   JOB_KEYWORDS=python developer,software engineer,backend developer
   MAX_JOBS_PER_CHECK=5
   ```

## Configuration ⚙️

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DISCORD_BOT_TOKEN` | Your Discord bot token | Required |
| `DISCORD_CHANNEL_ID` | ID of the channel to post jobs | Required |
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `CHECK_INTERVAL` | Seconds between job checks | 3600 (1 hour) |
| `JOB_KEYWORDS` | Comma-separated job search keywords | python developer,software engineer |
| `MAX_JOBS_PER_CHECK` | Maximum jobs to fetch per check | 5 |

### Getting Your Discord Channel ID

1. Enable Developer Mode in Discord (User Settings → Advanced → Developer Mode)
2. Right-click on your target channel
3. Click "Copy ID"

### Setting Up Your Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a New Application
3. Go to the "Bot" section and create a bot
4. Copy the bot token
5. Enable required intents:
   - Message Content Intent
   - Server Members Intent (optional)
6. Go to OAuth2 → URL Generator
7. Select scopes: `bot`
8. Select permissions: `Send Messages`, `Embed Links`, `Read Messages`
9. Copy the generated URL and invite the bot to your server

## Usage 🎮

### Running the Bot

Start the bot with:
```bash
python bot.py
```

The bot will:
1. Connect to Discord
2. Start monitoring for new jobs at the configured interval
3. Post job notifications to your specified channel

### Bot Commands

Use these commands in your Discord server:

- `!job check` - Manually trigger a job search
- `!job status` - Display bot status and configuration
- `!job help` - Show available commands

### Example Job Posting

The bot posts jobs as rich embeds with:
- 🎯 Job Title
- 🏢 Company Name
- 📍 Location
- 📝 Description
- ✅ Requirements
- 🔗 Apply Link
- 📅 Posted Date

## Project Structure 📁

```
vibe-job-bot/
├── bot.py              # Main Discord bot implementation
├── job_crawler.py      # AI-powered job crawler
├── config.py           # Configuration management
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment configuration
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## How It Works 🔧

1. **Job Discovery**: The bot uses OpenAI's GPT model to search for and generate job postings based on your keywords
2. **Deduplication**: Each job is tracked to prevent duplicate postings
3. **Formatting**: Jobs are formatted as Discord embeds with all relevant information
4. **Scheduling**: The bot checks for new jobs at your configured interval
5. **Notification**: New jobs are posted to your Discord channel

## Customization 🎨

### Changing Job Search Keywords

Edit the `JOB_KEYWORDS` in your `.env` file:
```env
JOB_KEYWORDS=react developer,frontend engineer,full stack developer
```

### Adjusting Check Frequency

Modify `CHECK_INTERVAL` (in seconds):
```env
CHECK_INTERVAL=1800  # Check every 30 minutes
```

### Limiting Jobs Per Check

Set `MAX_JOBS_PER_CHECK`:
```env
MAX_JOBS_PER_CHECK=10  # Fetch up to 10 jobs per check
```

## Troubleshooting 🔧

### Bot doesn't connect
- Verify your `DISCORD_BOT_TOKEN` is correct
- Ensure the bot has been invited to your server
- Check that required intents are enabled

### No jobs are posted
- Verify `DISCORD_CHANNEL_ID` is correct
- Check bot has permissions to send messages in the channel
- Ensure `OPENAI_API_KEY` is valid and has available credits

### Jobs are duplicated
- The bot tracks jobs by title, company, and location
- Ensure the bot process isn't running multiple times

## Security Notes 🔒

- Never commit your `.env` file or share your tokens
- Keep your OpenAI API key secure
- Regularly rotate your Discord bot token
- Monitor API usage to avoid unexpected charges

## Contributing 🤝

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License 📄

This project is open source and available under the MIT License.

## Support 💬

For issues, questions, or suggestions, please open an issue on GitHub.

---

Made with ❤️ for the job-hunting community
