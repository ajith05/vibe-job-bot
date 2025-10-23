# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Discord Job Bot System                       │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────┐          ┌──────────────────┐
│   User / Admin   │          │  Discord Server  │
│                  │          │                  │
│  Issues commands │◄────────►│   Bot Channel    │
│  !job check      │          │                  │
│  !job status     │          │  Receives job    │
│  !job help       │          │  notifications   │
└──────────────────┘          └──────────────────┘
                                      ▲
                                      │
                                      │ Posts formatted
                                      │ job embeds
                                      │
                    ┌─────────────────┴──────────────────┐
                    │                                     │
                    │       Discord Bot (bot.py)         │
                    │                                     │
                    │  ┌──────────────────────────────┐  │
                    │  │  Command Handlers            │  │
                    │  │  - Manual job check          │  │
                    │  │  - Status display            │  │
                    │  │  - Help information          │  │
                    │  └──────────────────────────────┘  │
                    │                                     │
                    │  ┌──────────────────────────────┐  │
                    │  │  Scheduled Tasks             │  │
                    │  │  - Periodic job checks       │  │
                    │  │  - Job deduplication         │  │
                    │  │  - Embed formatting          │  │
                    │  └──────────────────────────────┘  │
                    │                                     │
                    └─────────────────┬──────────────────┘
                                      │
                                      │ Requests jobs
                                      │
                                      ▼
                    ┌────────────────────────────────────┐
                    │                                     │
                    │   Job Crawler (job_crawler.py)     │
                    │                                     │
                    │  ┌──────────────────────────────┐  │
                    │  │  AI-Powered Search           │  │
                    │  │  - Keyword-based queries     │  │
                    │  │  - Job data extraction       │  │
                    │  │  - Response parsing          │  │
                    │  └──────────────────────────────┘  │
                    │                                     │
                    │  ┌──────────────────────────────┐  │
                    │  │  Deduplication Engine        │  │
                    │  │  - Track seen jobs           │  │
                    │  │  - Filter duplicates         │  │
                    │  └──────────────────────────────┘  │
                    │                                     │
                    └─────────────────┬──────────────────┘
                                      │
                                      │ API calls
                                      │
                                      ▼
                    ┌────────────────────────────────────┐
                    │                                     │
                    │      OpenAI API (GPT-3.5)          │
                    │                                     │
                    │  - Natural language understanding  │
                    │  - Job information generation      │
                    │  - Structured data formatting      │
                    │                                     │
                    └────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────┐
│                     Configuration (config.py)                    │
│                                                                   │
│  Environment Variables:                                          │
│  - DISCORD_BOT_TOKEN    - Bot authentication                    │
│  - DISCORD_CHANNEL_ID   - Target channel                        │
│  - OPENAI_API_KEY       - OpenAI authentication                 │
│  - CHECK_INTERVAL       - Frequency of checks                   │
│  - JOB_KEYWORDS         - Search terms                          │
│  - MAX_JOBS_PER_CHECK   - Result limit                          │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

1. **Initialization**
   ```
   start.py → Load config.py → Validate environment → Initialize bot
   ```

2. **Job Discovery** (Scheduled)
   ```
   Bot Timer → JobCrawler.fetch_jobs() → OpenAI API → Parse response
   ```

3. **Job Posting**
   ```
   New jobs → Format as embeds → Post to Discord channel
   ```

4. **Manual Commands**
   ```
   User command → Bot handler → Execute action → Send response
   ```

## Component Responsibilities

### bot.py (Main Discord Bot)
- Manages Discord connection and events
- Handles user commands
- Schedules periodic job checks
- Formats and posts job notifications
- Creates rich embeds for job listings

### job_crawler.py (AI Job Crawler)
- Interfaces with OpenAI API
- Generates job search prompts
- Parses AI responses into structured data
- Tracks seen jobs to prevent duplicates
- Provides async job fetching

### config.py (Configuration Manager)
- Loads environment variables
- Validates required settings
- Provides centralized configuration access
- Handles default values

### start.py (Startup Script)
- Validates environment setup
- Checks dependencies
- Provides user-friendly error messages
- Launches the bot

## Key Features

### 1. AI-Powered Job Discovery
- Uses GPT-3.5-turbo for intelligent job search
- Generates prompts based on keywords
- Extracts structured job data from AI responses

### 2. Smart Deduplication
- Tracks jobs by company, title, and location
- Prevents duplicate notifications
- Maintains seen jobs in memory

### 3. Rich Discord Integration
- Beautiful embeds with job details
- Command system for manual control
- Status monitoring and help commands

### 4. Flexible Configuration
- Environment-based settings
- Customizable check intervals
- Adjustable search parameters

### 5. Error Handling
- Graceful API error handling
- Validation before startup
- Informative error messages
