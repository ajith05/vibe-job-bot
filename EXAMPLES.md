# Example Job Posting

## What Job Notifications Look Like in Discord

When the bot finds new jobs, it posts them as rich embeds in your Discord channel:

### Example 1: Full Job Posting

```
┌────────────────────────────────────────────────────────────┐
│ 🎯 Senior Python Developer                                 │
│                                                             │
│ We are looking for an experienced Python developer to      │
│ join our backend team and work on scalable microservices.  │
│                                                             │
│ 🏢 Company                  📍 Location                     │
│ TechCorp Inc.               San Francisco, CA              │
│                                                             │
│ 📅 Posted                                                   │
│ 2024-01-15                                                  │
│                                                             │
│ ✅ Requirements                                             │
│ 5+ years Python experience, Django/Flask, Docker,          │
│ Kubernetes, AWS/GCP                                         │
│                                                             │
│ 🔗 Apply                                                    │
│ Click here to apply                                         │
│                                                             │
│ Posted by Vibe Job Bot • Today at 2:30 PM                  │
└────────────────────────────────────────────────────────────┘
```

### Example 2: Remote Software Engineer

```
┌────────────────────────────────────────────────────────────┐
│ 🎯 Full Stack Software Engineer (Remote)                   │
│                                                             │
│ Join our distributed team building next-generation         │
│ SaaS products. Work from anywhere!                          │
│                                                             │
│ 🏢 Company                  📍 Location                     │
│ Acme Solutions              Remote, Worldwide              │
│                                                             │
│ 📅 Posted                                                   │
│ 2024-01-14                                                  │
│                                                             │
│ ✅ Requirements                                             │
│ React, Node.js, TypeScript, REST APIs, 3+ years           │
│ experience                                                  │
│                                                             │
│ 🔗 Apply                                                    │
│ Click here to apply                                         │
│                                                             │
│ Posted by Vibe Job Bot • Today at 2:30 PM                  │
└────────────────────────────────────────────────────────────┘
```

### Example 3: Entry Level Position

```
┌────────────────────────────────────────────────────────────┐
│ 🎯 Junior Backend Developer                                │
│                                                             │
│ Perfect opportunity for recent graduates or junior          │
│ developers to start their career in backend development.    │
│                                                             │
│ 🏢 Company                  📍 Location                     │
│ StartupXYZ                  New York, NY                   │
│                                                             │
│ 📅 Posted                                                   │
│ 2024-01-16                                                  │
│                                                             │
│ ✅ Requirements                                             │
│ Python or Java, understanding of REST APIs, SQL,           │
│ 0-2 years experience                                        │
│                                                             │
│ 🔗 Apply                                                    │
│ Click here to apply                                         │
│                                                             │
│ Posted by Vibe Job Bot • Today at 2:30 PM                  │
└────────────────────────────────────────────────────────────┘
```

## Bot Commands in Action

### !job check
```
User: !job check

Bot: 🔍 Checking for new jobs...
Bot: [Posts 3 new job embeds]
Bot: ✅ Found and posted 3 new job(s)!
```

### !job status
```
User: !job status

Bot:
┌────────────────────────────────────────┐
│ 🤖 Bot Status                          │
│                                         │
│ Job Bot is running!                     │
│                                         │
│ Check Interval                          │
│ 3600 seconds                            │
│                                         │
│ Keywords                                │
│ python developer, software engineer,    │
│ backend developer                       │
│                                         │
│ Target Channel                          │
│ #job-postings                           │
└────────────────────────────────────────┘
```

### !job help
```
User: !job help

Bot:
┌────────────────────────────────────────┐
│ 📚 Job Bot Commands                    │
│                                         │
│ Available commands for the Job Bot     │
│                                         │
│ !job check                              │
│ Manually check for new jobs             │
│                                         │
│ !job status                             │
│ Show bot status and configuration       │
│                                         │
│ !job help                               │
│ Show this help message                  │
└────────────────────────────────────────┘
```

## Notification Frequency

By default, the bot checks for new jobs every hour (3600 seconds). You can configure this in your `.env` file:

```env
# Check every 30 minutes
CHECK_INTERVAL=1800

# Check every 2 hours
CHECK_INTERVAL=7200

# Check every 6 hours
CHECK_INTERVAL=21600
```

## Typical Daily Activity

With default settings (hourly checks, 5 jobs max per check):

- **9:00 AM**: Bot starts, finds 5 jobs, posts them
- **10:00 AM**: Checks again, finds 2 new jobs, posts them
- **11:00 AM**: Checks again, no new jobs found
- **12:00 PM**: Checks again, finds 3 new jobs, posts them
- And so on throughout the day...

The bot automatically filters out jobs it has already posted, so you never see duplicates!
