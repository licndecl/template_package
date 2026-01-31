from .config import config
from typing import Optional

import logging

from moslic_queue.simple_event_consumer import SimpleEventConsumer
from moslic_queue.publisher import Publisher

logger = logging.getLogger(__name__)

RUNOBECT_NAME = config("runobject_name")

LISTEN_QUEUE_ADDRESSES = config("listen_queue_addresses")
LISTEN_QUEUE_USERNAME = config("listen_queue_username")
LISTEN_QUEUE_PASSWORD = config("listen_queue_password")
LISTEN_QUEUE_NAME = config("listen_queue_name")
LISTEN_QUEUE_VHOST = config("listen_queue_vhost",default="")

PUBLISH_QUEUE_HOST = config("publish_queue_host")
PUBLISH_QUEUE_PORT = config("publish_queue_port", default=5672, cast=int)
PUBLISH_QUEUE_USERNAME = config("publish_queue_username")
PUBLISH_QUEUE_PASSWORD = config("publish_queue_password")
PUBLISH_QUEUE_NAME = config("publish_queue_name")
PUBLISH_QUEUE_VHOST = config("publish_queue_vhost",default="")

class BaseConsumer(SimpleEventConsumer):
    def __init__(self):
        super().__init__(RUNOBECT_NAME, LISTEN_QUEUE_ADDRESSES, LISTEN_QUEUE_NAME, LISTEN_QUEUE_USERNAME, LISTEN_QUEUE_PASSWORD, LISTEN_QUEUE_VHOST)
        logger.info('Initializing completed')

    def publish(self, json_params):
        exec_result = { "retcode": 0, "error": "" }
        try:
            publisher = Publisher(PUBLISH_QUEUE_HOST, PUBLISH_QUEUE_PORT, PUBLISH_QUEUE_USERNAME, PUBLISH_QUEUE_PASSWORD, PUBLISH_QUEUE_VHOST)
            publish_result = publisher.publish(PUBLISH_QUEUE_NAME, str(json_params))
            if "error" in publish_result:
                logger.error(f"Ошибка при постановке сообщения в очередь: {publish_result["error"]}")
                exec_result["retcode"] = -1
                exec_result["error"] = publish_result["error"]
        except Exception as ex:
            exec_result["retcode"] = -1
            exec_result["error"] = str(ex)
        return exec_result

