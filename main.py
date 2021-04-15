import telebot
from telebot import types
Token = '1692941369:AAEr_yZFN3kbPPhnO1VqHZj__BkdeTRpXsc'
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=["start"])
def starter(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_help = types.KeyboardButton(text="Помощь")
    button_filmsearсh = types.KeyboardButton(text="Поиск по названию фильма")
    button_metrosearсh = types.KeyboardButton(text="Поиск по метро")
    button_popularsearсh = types.KeyboardButton(text="Популярное")
    button_cinemalarsearсh = types.KeyboardButton(text="Поиск по кинотеатру")
    keyboard.add(button_filmsearсh, button_metrosearсh, button_help, button_popularsearсh, button_cinemalarsearсh)
    bot.send_message(message.chat,
                     "Чем я могу вам помочь?",
                     reply_markup=keyboard)


bot.polling(none_stop=True)
