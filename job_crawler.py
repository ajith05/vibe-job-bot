"""
Job crawler module that uses OpenAI's GPT to find and extract job postings.
"""
import asyncio
import json
from datetime import datetime
from typing import List, Dict, Optional
import openai
from config import Config


class JobCrawler:
    """Crawler that uses AI to find job postings."""
    
    def __init__(self):
        """Initialize the job crawler with OpenAI client."""
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        self.seen_jobs = set()  # Track jobs we've already posted
        
    async def fetch_jobs(self, keywords: List[str], max_jobs: int = 5) -> List[Dict]:
        """
        Use OpenAI to generate and format job postings based on keywords.
        
        Args:
            keywords: List of job search keywords
            max_jobs: Maximum number of jobs to return
            
        Returns:
            List of job dictionaries with title, company, location, etc.
        """
        try:
            # Create a prompt for GPT to generate job postings
            prompt = self._create_job_search_prompt(keywords, max_jobs)
            
            # Call OpenAI API in a thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None,
                lambda: self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a job search assistant that provides recent job postings. "
                                     "Return job data in JSON format only, no other text."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.7,
                    max_tokens=1500
                )
            )
            
            # Parse the response
            content = response.choices[0].message.content.strip()
            
            # Try to extract JSON from the response
            jobs = self._parse_jobs_response(content)
            
            # Filter out jobs we've already seen
            new_jobs = [job for job in jobs if self._is_new_job(job)]
            
            # Mark these jobs as seen
            for job in new_jobs:
                self._mark_job_as_seen(job)
            
            return new_jobs[:max_jobs]
            
        except Exception as e:
            print(f"Error fetching jobs: {e}")
            return []
    
    def _create_job_search_prompt(self, keywords: List[str], max_jobs: int) -> str:
        """Create a prompt for GPT to search for jobs."""
        keywords_str = ", ".join(keywords)
        return f"""Find {max_jobs} recent job openings for: {keywords_str}

Please provide REAL job postings that are currently available or were recently posted.
Search for actual companies hiring for these positions.

Return the results as a JSON array with the following structure:
[
  {{
    "title": "Job Title",
    "company": "Company Name",
    "location": "City, State/Country",
    "description": "Brief job description (1-2 sentences)",
    "requirements": "Key requirements",
    "posted_date": "Date posted (e.g., 2024-01-15)",
    "apply_url": "https://company-careers-page.com/job-id"
  }}
]

Focus on legitimate, real job postings from recognizable companies. Include a variety of companies and locations."""
    
    def _parse_jobs_response(self, content: str) -> List[Dict]:
        """Parse the AI response to extract job data."""
        try:
            # Try to find JSON in the response
            # Sometimes GPT wraps JSON in markdown code blocks
            if "```json" in content:
                start = content.find("```json") + 7
                end = content.find("```", start)
                content = content[start:end].strip()
            elif "```" in content:
                start = content.find("```") + 3
                end = content.find("```", start)
                content = content[start:end].strip()
            
            jobs = json.loads(content)
            
            # Ensure it's a list
            if isinstance(jobs, dict):
                jobs = [jobs]
            
            # Add timestamp to each job
            for job in jobs:
                job['fetched_at'] = datetime.now().isoformat()
            
            return jobs
            
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON response: {e}")
            print(f"Content: {content}")
            return []
    
    def _is_new_job(self, job: Dict) -> bool:
        """Check if a job posting is new (not seen before)."""
        # Create a unique identifier for the job
        job_id = f"{job.get('company', '')}:{job.get('title', '')}:{job.get('location', '')}"
        return job_id not in self.seen_jobs
    
    def _mark_job_as_seen(self, job: Dict):
        """Mark a job as seen to avoid duplicates."""
        job_id = f"{job.get('company', '')}:{job.get('title', '')}:{job.get('location', '')}"
        self.seen_jobs.add(job_id)
    
    async def search_jobs_continuously(self, callback, interval: int = 3600):
        """
        Continuously search for jobs at specified intervals.
        
        Args:
            callback: Async function to call with new jobs
            interval: Time between checks in seconds
        """
        print(f"Starting continuous job search (checking every {interval} seconds)...")
        
        while True:
            try:
                jobs = await self.fetch_jobs(Config.JOB_KEYWORDS, Config.MAX_JOBS_PER_CHECK)
                
                if jobs:
                    print(f"Found {len(jobs)} new job(s)")
                    await callback(jobs)
                else:
                    print("No new jobs found in this cycle")
                
            except Exception as e:
                print(f"Error in continuous job search: {e}")
            
            # Wait for the next check
            await asyncio.sleep(interval)
