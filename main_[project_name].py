import logging
import time     # для циклически исполняющихся сервисов
import uvicorn  # для web-сервисов на FastAPI

from <project_name>.config import config

# для сервисов обработки событий
from <project_name>.event_consumer import EventConsumer

<PROJECT_NAME>_LOG_FILENAME = config("<project_name>_log_filename", default="/var/log/<owner_name>/<project_name>/service_.log")
logging.basicConfig(filename=<PROJECT_NAME>_LOG_FILENAME, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=config("log_level",logging.INFO))
# если требуется отдельная настройка уровня логирования для некоторых компонентов, в данном случае для модуля suds
# logging.getLogger('suds').setLevel(logging.INFO)
logging.debug("log_file = " + <PROJECT_NAME>_LOG_FILENAME)

# для циклически исполняющихся сервисов
<PROJECT_NAME>_PAUSE = config("<project_name>_pause", default=60, cast=int)

# для web-сервисов
HOST = config("host", default="0.0.0.0")
PORT = config("port", default=8091, cast=int)

################################################################################################
# ТОЧКА ВХОДА В ПРОГРАММУ
if __name__ == '__main__':
    """
    # шаблон реализации web-сервиса
    uvicorn.run("<project_name>.api:app", host=HOST, port=PORT, reload=True, log_config=None)
    """

    """
    # шаблон реализации сервиса с циклической обработкой
    print("Запускается цикл обработки. Для выхода из цикла нажмите Ctrl+C")
    while( True ):
        try:
            logging.info("Что-то делаем...")
            # ...

            # пауза до следующего цикла
            logging.info("спим...")
            time.sleep(<PROJECT_NAME>_PAUSE)
        except KeyboardInterrupt:
            print("Прерывание цикла обработки по требованию пользователя")
            break
        except Exception as ex:
            logging.error("Прерывание цикла обработки ввиду ошибки. %s" % str(ex))

    print("Цикл обработки завершен.")
    """

    """
    # шаблон реализации сервиса обработки событий
    print("Запускается цикл обработки сообщений из очереди. Для выхода из цикла нажмите Ctrl+C")
    while( True ):
        try:
            logging.info('Создание объекта прослушивания...')

            # начнем прослушивать входящую очередь
            consumer = EventConsumer()
            
            logging.info('Запуск прослушивания...')
            # непосредственно начало прослушивания
            consumer.listen()

        except KeyboardInterrupt:
            print("Прерывание цикла обработки по требованию пользователя")
            break
        except Exception as ex:
            logging.error("Прерывание цикла обработки ввиду ошибки. %s" % str(ex))

    print("Цикл обработки сообщений из очереди завершен.")
    """