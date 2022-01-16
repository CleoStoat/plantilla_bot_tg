import os
from dotenv import load_dotenv

load_dotenv()

credentials = {
    "TOKEN": "token",
    # "STORE_CHAT_ID": "0",
    # "OWNER_ID": "0",
}

defaults = {
    "NOMBRE_ARCHIVO_BASE_DE_DATOS": "BASE_DE_DATOS"
}

defaults.update(credentials)

def get_env(env: str):
    result = os.getenv(env)
    if result is None:
        return defaults[env]
    return result


def get_bot_token() -> str:
    return get_env("TOKEN")

# def get_store_chat_id() -> int:
#     return int(get_env("STORE_CHAT_ID"))

# def get_owner_id() -> int:
#     return int(get_env("OWNER_ID"))

def get_database_filename() -> str:
    return get_env("NOMBRE_ARCHIVO_BASE_DE_DATOS")
