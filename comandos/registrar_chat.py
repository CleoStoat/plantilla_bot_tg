from telegram import Update as _Update
from telegram.ext import CallbackContext as _CallbackContext


name = "registrar"
description = "Registra el chat"
def cmd(update: _Update, context: _CallbackContext):

    # Crear lista de chats si es que no existe
    if "chats" not in context.bot_data:
        context.bot_data["chats"] = set()

    chat_id = update.effective_chat.id

    context.bot_data["chats"].add(chat_id)

    update.effective_message.reply_text(
        text=f"Agregado chat con id {chat_id}"
    )

    update.effective_message.reply_text(
        text=f"Lista de ids: {str(context.bot_data['chats'])}"
    )
