# Crear nuevo job:

1. Crear un nuevo archivo en la carpeta `jobs`, preferentemente que el nombre termine en `_job`

2. Copiar y pegar la siguiente plantilla:
```python
from telegram.ext import CallbackContext as _CallbackContext

def callback(context: _CallbackContext):
    pass
```

3. Escribir toda la lógica del comando en la función `callback`

4. En el archivo `cargar_jobs.py` agregar import del nuevo comando y agregar al listado `modulos_jobs`

Ejemplo:
Si tu nuevo comando se llama `nuevo_job` el archivo debería quedar algo así:

```python
...
from jobs import (
    ejemplo_job,
    nuevo_job,  # <--
)
    
modulos_jobs = [
    ejemplo_job,
    nuevo_job,  # <--
]
...
```

5. Y configurarlo dentro de la funcion cargar con el `job_queue`

    > MUY IMPORTANTE: si no le configuras el `name` da error

    ```python
    job_queue.run_once(
        callback=nuevo_job.callback,
        when=10,  # Segundos desde ahora o datetime  
        name="Job de ejemplo UNA VEZ", 
    )
    ```

    ```python
    # Correr todos los lunes y martes a las 10:15 AM
    job_queue.run_daily(
        callback=nuevo_job.callback,
        days=(0, 1),
        time=datetime.time(hour=10, minute=15),
        name="Job de ejemplo LUNES Y MARTES",
    )
    ```

    ```python
    # Correr repetidas veces CADA X CANTIDAD DE TIEMPO
    job_queue.run_repeating(
        callback=ejemplo_job.callback,
        first=1, # Segundos desde ahora
        interval=datetime.timedelta(hours=12),   # Cada cuanto tiempo 
        name="Job de ejemplo CADA 12 HORAS",
    )
    ```