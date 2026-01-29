from .config import config
from typing import Optional

import logging

from .base_consumer import BaseConsumer

logger = logging.getLogger(__name__)

class EventConsumer(BaseConsumer):
    def __init__(self):
        super().__init__()
        logger.info('Initializing completed')

    # прикладная функция-обработчик (переопределяется в классах-наследниках)
    # пустая строка с ошибкой - сигнал к удалению сообщения из очереди - это сообщение обработано
    def processing(self, id_eventlog, json_params) -> dict:
        exec_result = { "retcode": 0, "error": "" }
        # постановка в очередь сообщения для дальнейшей обработки
        publish_data = { "id_eventlog": str(id_eventlog), "data": str(json_params) }
        try:
            exec_result = self.publish(publish_data)
        except Exception as ex:
            exec_result["retcode"] = -2
            exec_result["error"] = str(ex)
        return exec_result
