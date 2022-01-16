from telegram import Update as _Update
from telegram.ext import CallbackContext as _CallbackContext


name = "ver_id"
description = "Ver el id de este chat"
def cmd(update: _Update, context: _CallbackContext):
    chat_id = update.effective_chat.id

    update.effective_message.reply_text(
        text=f"ID de este chat: {chat_id}"
    )
