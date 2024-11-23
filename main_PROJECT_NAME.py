import logging
from <PROJECT_NAME>.config import config

<PROJECT_NAME>_PAUSE = config("<PROJECT_NAME>_pause", default=60, cast=int)

################################################################################################
# ТОЧКА ВХОДА В ПРОГРАММУ
if __name__ == '__main__':

    <PROJECT_NAME>_LOG_FILENAME = config("<PROJECT_NAME>_log_filename", default="/var/log/<НАИМЕНОВАНИЕ ИС>/<PROJECT_NAME>/service_.log")
    logging.basicConfig(filename=<PROJECT_NAME>_LOG_FILENAME_LOG_FILENAME, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.debug("log_file = " + <PROJECT_NAME>_LOG_FILENAME)

    """
    # шаблон реализации web-сервиса
    uvicorn.run("<PROJECT_NAME>..api:app", host="0.0.0.0", port=8000, reload=True)
    """

    """
    # шаблон реализации сервиса с циклической обработкой
    print("Запускается цикл обарботки. Для выхода из цикла нажмите Ctrl+C")
    while( True ):
        try:
            logging.info("Что-то делаем...")
            # ...

            # пауза до следующего цикла
            logging.info("спим...")
            time.sleep(<PROJECT_NAME>_PAUSE)
        except KeyboardInterrupt:
            print("Прерывание цикла отправки по требованию пользователя")
            break
        except Exception as ex:
            logging.error("Прерывание цикла обработки ввиду ошибки. %s" % str(ex))

    print("Цикл обработки завершен.")
    """