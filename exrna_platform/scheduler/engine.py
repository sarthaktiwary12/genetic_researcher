"""Research scheduler using APScheduler with PostgreSQL job store.

Registers recurring campaigns (daily PubMed, weekly synthesis, monthly
hypothesis review) and supports on-demand campaign launches.
"""

import asyncio
import logging
from datetime import datetime
from typing import Optional

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

from exrna_platform.scheduler.campaigns import CampaignType, CAMPAIGN_TEMPLATES
from exrna_platform.scheduler.progress import ProgressTracker

logger = logging.getLogger(__name__)


class ResearchScheduler:
    """Manages scheduled and on-demand research campaigns.

    Uses APScheduler with PostgreSQL job store for persistence across restarts.
    """

    def __init__(
        self,
        postgres_url: str,
        progress_tracker: Optional[ProgressTracker] = None,
    ):
        # Convert async URL to sync for APScheduler
        sync_url = postgres_url.replace("+asyncpg", "")

        self.scheduler = AsyncIOScheduler(
            jobstores={
                "default": SQLAlchemyJobStore(url=sync_url),
            },
            job_defaults={
                "coalesce": True,
                "max_instances": 1,
                "misfire_grace_time": 3600,
            },
        )
        self.progress = progress_tracker
        self._campaign_runners = {}

    def register_runner(self, campaign_type: CampaignType, runner_func):
        """Register an async function to handle a campaign type.

        Args:
            campaign_type: The campaign type enum.
            runner_func: Async callable(campaign_id, config) -> dict.
        """
        self._campaign_runners[campaign_type] = runner_func
        logger.info(f"Registered runner for {campaign_type.value}")

    def start(self):
        """Start the scheduler."""
        self.scheduler.start()
        logger.info("Research scheduler started")

    def shutdown(self, wait: bool = True):
        """Shutdown the scheduler."""
        self.scheduler.shutdown(wait=wait)
        logger.info("Research scheduler shut down")

    def setup_recurring_jobs(self):
        """Register all default recurring jobs from campaign templates."""
        for campaign_type, template in CAMPAIGN_TEMPLATES.items():
            if template.cron_schedule:
                job_id = f"recurring_{campaign_type.value}"
                self.scheduler.add_job(
                    self._run_campaign,
                    trigger=CronTrigger(**template.cron_schedule),
                    id=job_id,
                    name=template.name,
                    kwargs={
                        "campaign_type": campaign_type,
                        "config": template.default_config,
                    },
                    replace_existing=True,
                )
                logger.info(
                    f"Scheduled recurring job: {template.name} "
                    f"(cron: {template.cron_schedule})"
                )

    async def launch_campaign(
        self,
        campaign_type: CampaignType,
        config: Optional[dict] = None,
        name: Optional[str] = None,
    ) -> str:
        """Launch an on-demand campaign.

        Args:
            campaign_type: Type of campaign to run.
            config: Override config (merged with template defaults).
            name: Custom campaign name.

        Returns:
            Campaign ID.
        """
        template = CAMPAIGN_TEMPLATES.get(campaign_type)
        if not template:
            raise ValueError(f"Unknown campaign type: {campaign_type}")

        merged_config = {**(template.default_config or {}), **(config or {})}
        campaign_name = name or template.name

        # Create campaign record
        campaign_id = None
        if self.progress:
            campaign_id = await self.progress.create_campaign(
                name=campaign_name,
                campaign_type=campaign_type.value,
                config=merged_config,
                budget_limit=template.budget_limit,
                crop=merged_config.get("crop"),
            )

        # Schedule for immediate execution
        job_id = f"ondemand_{campaign_type.value}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.scheduler.add_job(
            self._run_campaign,
            trigger=None,  # Run immediately
            id=job_id,
            name=campaign_name,
            kwargs={
                "campaign_type": campaign_type,
                "config": merged_config,
                "campaign_id": campaign_id,
            },
        )

        logger.info(f"Launched campaign: {campaign_name} (id={campaign_id})")
        return campaign_id or job_id

    async def _run_campaign(
        self,
        campaign_type: CampaignType,
        config: dict,
        campaign_id: Optional[str] = None,
    ):
        """Execute a campaign using its registered runner."""
        runner = self._campaign_runners.get(campaign_type)
        if not runner:
            logger.error(f"No runner registered for {campaign_type.value}")
            if self.progress and campaign_id:
                await self.progress.mark_failed(
                    campaign_id, f"No runner for {campaign_type.value}"
                )
            return

        if self.progress and campaign_id:
            await self.progress.mark_running(campaign_id)

        try:
            result = await runner(campaign_id, config)

            if self.progress and campaign_id:
                await self.progress.mark_completed(campaign_id, result)

            logger.info(f"Campaign {campaign_type.value} completed: {result}")

        except Exception as e:
            logger.error(f"Campaign {campaign_type.value} failed: {e}", exc_info=True)
            if self.progress and campaign_id:
                await self.progress.mark_failed(campaign_id, str(e))

    def get_scheduled_jobs(self) -> list[dict]:
        """Return list of all scheduled jobs."""
        jobs = []
        for job in self.scheduler.get_jobs():
            jobs.append({
                "id": job.id,
                "name": job.name,
                "next_run_time": str(job.next_run_time) if job.next_run_time else None,
                "trigger": str(job.trigger),
            })
        return jobs

    def pause_job(self, job_id: str):
        """Pause a scheduled job."""
        self.scheduler.pause_job(job_id)
        logger.info(f"Paused job: {job_id}")

    def resume_job(self, job_id: str):
        """Resume a paused job."""
        self.scheduler.resume_job(job_id)
        logger.info(f"Resumed job: {job_id}")

    def remove_job(self, job_id: str):
        """Remove a scheduled job."""
        self.scheduler.remove_job(job_id)
        logger.info(f"Removed job: {job_id}")


async def main():
    """Standalone scheduler worker entry point."""
    import os
    from dotenv import load_dotenv
    load_dotenv()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    postgres_url = os.getenv(
        "POSTGRES_URL",
        "postgresql+asyncpg://exrna:exrna_research@localhost:5432/exrna_platform",
    )

    scheduler = ResearchScheduler(postgres_url=postgres_url)
    scheduler.setup_recurring_jobs()
    scheduler.start()

    logger.info("Scheduler worker running. Press Ctrl+C to stop.")
    try:
        while True:
            await asyncio.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
