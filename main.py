import telebot
from telebot import types
from popular import popular

bot = telebot.TeleBot('1692941369:AAEr_yZFN3kbPPhnO1VqHZj__BkdeTRpXsc')


# Импортируем типы из модуля, чтобы создавать кнопки


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу про актуальные фильмы.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_search_by_movie = types.InlineKeyboardButton(text='Поиск по названию фильма', callback_data='film')
        # И добавляем кнопку на экран
        keyboard.add(key_search_by_movie)
        key_search_by_metro = types.InlineKeyboardButton(text='Поиск по метро', callback_data='film')
        keyboard.add(key_search_by_metro)
        key_cinema_search = types.InlineKeyboardButton(text='Поиск по кинотеатру', callback_data='film')
        keyboard.add(key_cinema_search)
        key_popular = types.InlineKeyboardButton(text='Популярное', callback_data='film')
        keyboard.add(key_popular)
        key_help = types.InlineKeyboardButton(text='Помощь', callback_data='help')
        keyboard.add(key_help)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери что вы хотите сделать', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'help':
        msg = "- |поиск по названию фильма| данная функция позволит вам найти именно ту кинокартину, которую Вы ищите. " \
              "Вводите название как заявлено прокатчиком.\n\n- |поиск по метро| данная функция подскажет Вам где будет " \
              "удобнее посмотреть фильм исходя из места положения станции метро.\n\n- |поиск по кинотеатру данная| " \
              "функция " \
              "покажет Вам список фильмов, которые на данный момент в прокате в заданной сети кинотеатров.\n\n- " \
              "|популярное| " \
              "данная функция выдаст Вам список киноновинок.\n\n- |помощь| данная функция подскажет какая кнопка за " \
              "что " \
              "отвечает если Вы вдруг забудете."
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "film":
        msg = '\n<--------------->\n'.join([''.join(x) for x in popular()])
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
