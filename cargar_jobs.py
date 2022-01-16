from telegram.ext import Updater
import datetime

from jobs import (
    ejemplo_job,
)
    
modulos_jobs = [
    ejemplo_job,
]



def cargar(updater: Updater) -> None:
    job_queue = updater.job_queue

    # ------------------------------
    # vvv Cargar jobs a partir de aquí vvv
    #------------------------------

    # Correr el job_ejemplo UNA VEZ dentro de 10 segundos
    job_queue.run_once(
        callback=ejemplo_job.callback,
        when=10,    # Si es un numero es "segundos a partir de ahora"
        # Si es un datetime es la fecha/hora en la cual ejecuta por primera vez:
        # when=datetime.datetime.now() + datetime.timedelta(days=1),
        name="Job de ejemplo UNA VEZ",
    )

    # Correr todos los lunes y martes a las 10:15 AM
    job_queue.run_daily(
        callback=ejemplo_job.callback,
        days=(0, 1),
        time=datetime.time(hour=10, minute=15),
        name="Job de ejemplo LUNES Y MARTES",
    )

    # Correr repetidas veces CADA X CANTIDAD DE TIEMPO
    job_queue.run_repeating(
        callback=ejemplo_job.callback,
        first=1, # Segundos desde ahora
        interval=datetime.timedelta(hours=12),
        name="Job de ejemplo CADA 12 HORAS",
    )


