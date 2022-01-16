from telegram.ext import CallbackContext as _CallbackContext

def callback(context: _CallbackContext):
    pass
    # chats = context.bot_data["chats"]

    # for chat_id in chats:
    #     context.bot.send_message(
    #         chat_id=chat_id, 
    #         text="Anuncio",
    #     )
