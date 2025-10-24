"""
Discord bot for posting job notifications.
"""
import discord
from discord.ext import commands, tasks
import asyncio
from typing import List, Dict
from config import Config
from job_crawler import JobCrawler


class JobBot(commands.Bot):
    """Discord bot that posts job updates to a channel."""
    
    def __init__(self):
        """Initialize the Discord bot."""
        intents = discord.Intents.default()
        intents.message_content = True
        
        super().__init__(
            command_prefix='!job ',
            intents=intents,
            help_command=None
        )
        
        self.job_crawler = JobCrawler()
        self.target_channel_id = int(Config.DISCORD_CHANNEL_ID)
        
    async def setup_hook(self):
        """Set up the bot after login."""
        # Start the job checking loop
        self.check_jobs.start()
        
    async def on_ready(self):
        """Called when the bot is ready."""
        print(f'Logged in as {self.user.name} (ID: {self.user.id})')
        print(f'Monitoring channel ID: {self.target_channel_id}')
        print('Bot is ready!')
        print('------')
    
    @tasks.loop(seconds=Config.CHECK_INTERVAL)
    async def check_jobs(self):
        """Periodically check for new jobs."""
        try:
            print("Checking for new jobs...")
            jobs = await self.job_crawler.fetch_jobs(
                Config.JOB_KEYWORDS,
                Config.MAX_JOBS_PER_CHECK
            )
            
            if jobs:
                await self.post_jobs(jobs)
            else:
                print("No new jobs found")
                
        except Exception as e:
            print(f"Error in job checking loop: {e}")
    
    @check_jobs.before_loop
    async def before_check_jobs(self):
        """Wait for the bot to be ready before starting the loop."""
        await self.wait_until_ready()
        print("Job checking loop starting...")
    
    async def post_jobs(self, jobs: List[Dict]):
        """
        Post job listings to the Discord channel.
        
        Args:
            jobs: List of job dictionaries to post
        """
        channel = self.get_channel(self.target_channel_id)
        
        if not channel:
            print(f"Error: Could not find channel with ID {self.target_channel_id}")
            return
        
        for job in jobs:
            embed = self._create_job_embed(job)
            try:
                await channel.send(embed=embed)
                print(f"Posted job: {job.get('title', 'Unknown')} at {job.get('company', 'Unknown')}")
            except Exception as e:
                print(f"Error posting job: {e}")
    
    def _create_job_embed(self, job: Dict) -> discord.Embed:
        """
        Create a Discord embed for a job posting.
        
        Args:
            job: Job dictionary
            
        Returns:
            Discord Embed object
        """
        # Choose color based on job type or use a default
        embed = discord.Embed(
            title=f"🎯 {job.get('title', 'New Job Posting')}",
            description=job.get('description', 'No description available'),
            color=discord.Color.blue(),
            url=job.get('apply_url', '')
        )
        
        # Add company information
        if job.get('company'):
            embed.add_field(
                name="🏢 Company",
                value=job['company'],
                inline=True
            )
        
        # Add location
        if job.get('location'):
            embed.add_field(
                name="📍 Location",
                value=job['location'],
                inline=True
            )
        
        # Add posted date
        if job.get('posted_date'):
            embed.add_field(
                name="📅 Posted",
                value=job['posted_date'],
                inline=True
            )
        
        # Add requirements
        if job.get('requirements'):
            embed.add_field(
                name="✅ Requirements",
                value=job['requirements'],
                inline=False
            )
        
        # Add apply link if available
        if job.get('apply_url'):
            embed.add_field(
                name="🔗 Apply",
                value=f"[Click here to apply]({job['apply_url']})",
                inline=False
            )
        
        # Add footer with timestamp
        embed.set_footer(text="Posted by Vibe Job Bot")
        embed.timestamp = discord.utils.utcnow()
        
        return embed


# Bot commands
def setup_commands(bot: JobBot):
    """Set up bot commands."""
    
    @bot.command(name='check')
    async def manual_check(ctx):
        """Manually trigger a job check."""
        await ctx.send("🔍 Checking for new jobs...")
        
        jobs = await bot.job_crawler.fetch_jobs(
            Config.JOB_KEYWORDS,
            Config.MAX_JOBS_PER_CHECK
        )
        
        if jobs:
            await bot.post_jobs(jobs)
            await ctx.send(f"✅ Found and posted {len(jobs)} new job(s)!")
        else:
            await ctx.send("ℹ️ No new jobs found at this time.")
    
    @bot.command(name='status')
    async def status(ctx):
        """Check bot status."""
        embed = discord.Embed(
            title="🤖 Bot Status",
            description="Job Bot is running!",
            color=discord.Color.green()
        )
        
        embed.add_field(
            name="Check Interval",
            value=f"{Config.CHECK_INTERVAL} seconds",
            inline=True
        )
        
        embed.add_field(
            name="Keywords",
            value=", ".join(Config.JOB_KEYWORDS),
            inline=False
        )
        
        embed.add_field(
            name="Target Channel",
            value=f"<#{bot.target_channel_id}>",
            inline=True
        )
        
        await ctx.send(embed=embed)
    
    @bot.command(name='help')
    async def help_command(ctx):
        """Show available commands."""
        embed = discord.Embed(
            title="📚 Job Bot Commands",
            description="Available commands for the Job Bot",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="!job check",
            value="Manually check for new jobs",
            inline=False
        )
        
        embed.add_field(
            name="!job status",
            value="Show bot status and configuration",
            inline=False
        )
        
        embed.add_field(
            name="!job help",
            value="Show this help message",
            inline=False
        )
        
        await ctx.send(embed=embed)


async def main():
    """Main function to run the bot."""
    try:
        # Validate configuration
        Config.validate()
        
        # Create and set up the bot
        bot = JobBot()
        setup_commands(bot)
        
        # Run the bot
        await bot.start(Config.DISCORD_BOT_TOKEN)
        
    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"Error running bot: {e}")
        raise


if __name__ == '__main__':
    asyncio.run(main())
