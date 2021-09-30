import asyncio
from datetime import datetime
import requests as requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import AutoCreateUserContact as autoCreate


def sample_respones(input_text, update):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "greeting"):
        name = update.message.from_user.first_name
        return "hello!! How can I help you " + name + "?"

    elif user_message in ("time", "times", "date"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    elif user_message in ("how are you", "how are you?", "how are you doing", "how are you doing?", "how are you going",
                          "how are you going?"):
        return "hello!! I am simple, How about you?"

    elif user_message in (
            "good morning", "good afternoon", "good evening", "good night", "morning", "afternoon", "evening", "night"):
        now = datetime.now().hour
        for h in range(0, 24):
            session = get_part_of_day(h)
        return "Good " + session

    else:
        return "There is something wrong, please try again later"


def get_part_of_day(hour):
    return (
        "Morning!!!" + " 🌅🌅🌅" if 5 <= hour <= 11
        else
        "Afternoon!!!" if 12 <= hour <= 17
        else
        "Evening!!!" + " 🌆🌆🌆" if 18 <= hour <= 22
        else
        "Night!!!" + " 🌃🌃🌃"
    )


def main_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=main_menu_message(),
        reply_markup=main_menu_keyboard())


#
async def option_one(update, context):
    autoCreate.createUserContact()
    with open("members-import-contact.csv", "rb") as file:
        await context.bot.send_document(chat_id=update.callback_query.message.chat.id, document=file,
                                  filename='members-import-contact.csv')


def main_menu_message():
    return 'There are three way to reset your password:'


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Import contact to telegram', callback_data='m1')],
                [InlineKeyboardButton('Scrap contact from telegram group/channel', callback_data='m2',
                                      url="https://t.me/joinchat/WNrNCIYcDp5xXRET")],
                [InlineKeyboardButton('Add contact to telegram group/channel', callback_data='m3',
                                      url="https://t.me/Piseth_Soeng")]]
    return InlineKeyboardMarkup(keyboard)
