import logging
import dotenv

from telegram.ext import Updater
from telegram.ext import PicklePersistence

import config
import cargar_comandos
import cargar_jobs


def main():
    dotenv.load_dotenv()

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    my_persistence = PicklePersistence(filename=config.get_database_filename())
    updater = Updater(
        token=config.get_bot_token(), 
        persistence=my_persistence,
        use_context=True,
    )
    cargar_comandos.cargar(updater)
    cargar_jobs.cargar(updater)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
