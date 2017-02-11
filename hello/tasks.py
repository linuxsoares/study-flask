from __future__ import absolute_import
from celery import Celery
import logging
import settings
from settings.production import celery

logger = logging.getLogger(__file__)

@celery.task(name="tasks.add")
def add(x, y):
    logger.info(
        'result: {}'.format(x + y)
    )
    return (x + y)

if __name__ == "__main__":
    celery.start()
