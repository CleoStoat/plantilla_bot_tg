from telegram import Update as _Update
from telegram.ext import CallbackContext as _CallbackContext


name = "floppaaaaaa"
description = "el peor comando de todos"
def cmd(update: _Update, context: _CallbackContext):
    update.effective_message.reply_text(text="Usaste el comando floppa")
