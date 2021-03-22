import telebot
bot = telebot.TeleBot('1791404745:AAE2EHtv2Dhg-BhOwD8N5lLCk29VdNO4I38')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, а может и неприятно, кто знает, я ведь великий лжец, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет, существо. Не очень рад тебя видеть!')
    else:
        bot.send_message(message.from_user.id, 'Будь вежливой(ым) и отправь мне слово "привет" для начала.')

bot.polling(none_stop=True)

