from core import sprinkler as sprinkler_release
from core import send_email
from .models import Scheduler, Sprinkler
import time
import logging

logger = logging.getLogger(__name__)


def sprinkler_job():
    logger.debug("beginning crontab sprinkler job")
    try:
        sprinkler_object = sprinkler_release.Sprinkler()
        # scheduler = Scheduler.objects.get(pk=1)
        # to do

        sprinkler_list = Sprinkler.objects.order_by('order')
        for sprinkler in sprinkler_list:
            sprinkler_object.init_GPIO(int(sprinkler.GPIO_pin), sprinkler_object.GPIO_TYPE["output"])
            sprinkler_object.deactivate(int(sprinkler.GPIO_pin))
            sprinkler_object.activate(int(sprinkler.GPIO_pin))
            time.sleep(int(sprinkler.duration))
            sprinkler_object.deactivate(int(sprinkler.GPIO_pin))
        send_email.send_email_with_subject(recipient='breazuadrian@gmail.com', subject='Sprinklers job finished',
                                           body="Sprinklers 1,2,3 and 4 finished their job successfully")
    except Exception as e:
        send_email.send_email_with_subject(recipient='breazuadrian@gmail.com', subject='Sprinklers job failed',
                                           body="Sprinklers 1,2,3 and 4 did not start. " + e)
        logger.error("crontab sprinkler job exception {0}".format(e))
    finally:
        logger.debug("end crontab sprinkler job")