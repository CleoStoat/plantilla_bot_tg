# Crear nuevo comando:

1. Crear un nuevo archivo en la carpeta `comandos`, preferentemente que el nombre termine en `_cmd`

2. Copiar y pegar la siguiente plantilla:
```python
from telegram import Update as _Update
from telegram.ext import CallbackContext as _CallbackContext


name = "NOMBRE_COMANDO"
description = "DESCRIPCION DEL COMANDO"
def cmd(update: _Update, context: _CallbackContext):
    pass

```
(Tener en cuenta que `name` no debe contener caracteres raros o espacios)

3. Escribir toda la lógica del comando en la función `cmd`

4. En el archivo `cargar_comandos.py` agregar import del nuevo comando y agregar al listado `modulos_comandos`

Ejemplo:
Si tu nuevo comando se llama `nuevo_cmd` el archivo debería quedar algo así:

```python
...
from comandos import (
    start_cmd,
    help_cmd,
    nuevo_cmd,  # <--
)
    
modulos_comandos = [
    start_cmd,
    help_cmd,
    nuevo_cmd,  # <--
]
...
```
