"""
Configuration management for the Discord Job Bot.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for bot settings."""
    
    # Discord Settings
    DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    DISCORD_CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')
    
    # OpenAI Settings
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Job Crawler Settings
    CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', 3600))
    JOB_KEYWORDS = os.getenv('JOB_KEYWORDS', 'python developer,software engineer').split(',')
    MAX_JOBS_PER_CHECK = int(os.getenv('MAX_JOBS_PER_CHECK', 5))
    
    @classmethod
    def validate(cls):
        """Validate required configuration."""
        required_vars = {
            'DISCORD_BOT_TOKEN': cls.DISCORD_BOT_TOKEN,
            'DISCORD_CHANNEL_ID': cls.DISCORD_CHANNEL_ID,
            'OPENAI_API_KEY': cls.OPENAI_API_KEY,
        }
        
        missing_vars = [var for var, value in required_vars.items() if not value]
        
        if missing_vars:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_vars)}\n"
                "Please check your .env file or environment configuration."
            )
        
        return True
