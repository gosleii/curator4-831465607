import telebot
bot1 = telebot.TeleBot('7310457660:AAG3Bna2Ol-R3J8a7G9xpnYzegV7YTvADt8')

@bot1.message_handler(commands=['start'])
def start(message):
    bot1.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}', parse_mode='Markdown')


@bot1.message_handler(commands=['proverb'])
def home(message):
    bot1.send_message(message.chat.id, 'Без труда не выловишь и рыбку из пруда')


@bot1.message_handler(commands=['quote'])
def quote(message):
    bot1.send_message(message.chat.id, '*Когдатебе тяжело, всегда напоминай себе о том, что если ты сдашься, лучше не станет*\n\n _Майк Тайсон_', parse_mode='Markdown')


@bot1.message_handler(commands=['nickname'])
def nickname_verification(message):
    bot1.send_message(message.chat.id, '_Введите никнейм_', parse_mode='Markdown')
    @bot1.message_handler()
    def nick(message):
        flag = True
        for i in '0123456789':
            if message.text.startswith(i) == True:
                flag = False
                break
        if len(message.text) <= 20 and flag == True and (message.text.endswith('bot') == True or message.text.endswith('Bot') == True):
            bot1.send_message(message.chat.id, 'Ник одобрен!')
        else:
            bot1.send_message(message.chat.id, 'Попробуй придумать другой ник')


bot1.infinity_polling()