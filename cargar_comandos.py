from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import BotCommand

from comandos import (
    start_cmd,
    help_cmd,
    floppa,
    registrar_chat,
    ver_id,
)
    
modulos_comandos = [
    start_cmd,
    help_cmd,
    floppa,
    registrar_chat,
    ver_id,
]


def cargar(updater: Updater) -> None:
    dispatcher = updater.dispatcher
    bot_commands = []

    for modulo_cmd in modulos_comandos:
        cmd_handler = CommandHandler(modulo_cmd.name, modulo_cmd.cmd)
        dispatcher.add_handler(cmd_handler)
        bot_commands.append(BotCommand(modulo_cmd.name, modulo_cmd.description))
        
    
    updater.bot.set_my_commands(bot_commands)