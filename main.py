import API as keys
from telegram.ext import *
import Response as res
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

print("bot has start...")


def start_command(update, context):
    update.message.reply_text('type something random to get started')
    # update.message.reply_text(main_menu_message(), reply_markup=main_menu_keyboard())


def help_command(update, context):
    update.message.reply_text('type something random to get started')


def downloader(update, context):
    context.bot.get_file(update.message.document).download()
    # writing to a custom file
    with open("custom/Book1.xls", 'wb') as f:
        context.bot.get_file(update.message.document).download(out=f)


def telegram_automate_command(update, context):
    # update.message.reply_text('type something random to get started')
    text = str(update.message.text).lower()
    if 'tools' in text:
        update.message.reply_text(res.main_menu_message(), reply_markup=res.main_menu_keyboard())

    elif 'tool' in text:
        update.message.reply_text(res.main_menu_message(), reply_markup=res.main_menu_keyboard())
    else:
        response = res.sample_respones(text, update)
        update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(CallbackQueryHandler(res.main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(res.option_one, pattern='m1'))
    # dp.add_handler(CallbackQueryHandler(res.option_two, pattern='m2'))

    updater.dispatcher.add_handler(MessageHandler(Filters.document, downloader))

    dp.add_handler(MessageHandler(Filters.text, telegram_automate_command))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
