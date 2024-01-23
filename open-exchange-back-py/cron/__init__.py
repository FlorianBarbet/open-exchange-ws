import os

from apscheduler.triggers.cron import CronTrigger

from .configuration import scheduler
from .rates_of_today import job


scheduler.add_job(func=rates_of_today.job,
                  trigger=CronTrigger.from_crontab(os.getenv('RATES_OF_DAY_CRON', default="0 2 * * *")))
