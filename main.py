import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Updater,
    CallbackContext,
    MessageHandler,
    Filters
)

load_dotenv()


def start_handler(update: Update, context: CallbackContext):
    file = bytes(update.message.sticker.get_file().download_as_bytearray())
    if update.message.effective_attachment.is_animated:
        update.message.reply_document(file, filename='file.tgs')
    else:
        update.message.reply_photo(file)
    del file


token = os.getenv('TOKEN')
updater = Updater(token)
updater.dispatcher.add_handler(MessageHandler(Filters.sticker, start_handler))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
