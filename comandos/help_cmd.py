from telegram import Update as _Update
from telegram.ext import CallbackContext as _CallbackContext


name = "help"
description = "Ayuda del bot"
def cmd(update: _Update, context: _CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="AYUDA")
