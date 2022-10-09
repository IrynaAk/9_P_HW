import telebot
import calc_bot as cb
 
bot = telebot.TeleBot('5799483261:AAE7meD3rM9xAj1vz-IZgFYa-CpeNOvc2-Q')

buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Комплексные'),
             telebot.types.KeyboardButton('Рациональные'),
             telebot.types.KeyboardButton('Ещё не определился'))
 
buttons2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2.row(telebot.types.KeyboardButton('+'),
             telebot.types.KeyboardButton('-'))
buttons2.row(telebot.types.KeyboardButton('*'),
             telebot.types.KeyboardButton('/'))
 
 
@bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Лог программы\newcoiywgecowegcouwefoyewfov',
                     reply_markup=cb.del_buttons)
    bot.send_document(chat_id=msg.from_user.id, document=open('TestBot.log', 'rb'))
 
 
@bot.message_handler(content_types=['document'])
def hello(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, 'wb') as f_out:
        f_out.write(downloaded_file)
    # Открываем и импортируем
 
 
@bot.message_handler()
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Здравствуйте.\nВыберите режим работы калькулятора.',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)
 
 
def answer(msg: telebot.types.Message):
    # if msg.text == 'Комплексные':
    #     bot.register_next_step_handler(msg, cb.complex_counter)
    #     bot.send_message(chat_id=msg.from_user.id,
    #                      text='Введите выражение с комплексными числами.',
    #                      reply_markup=telebot.types.ReplyKeyboardRemove())
    if msg.text == 'Рациональные':
        bot.register_next_step_handler(msg, rational_first_value)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите первое число: ',
                         reply_markup=cb.del_buttons)
    elif msg.text == 'Ещё не определился':
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Возвращайтесь, когда определитесь.')
    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки.')
 
        bot.send_message(chat_id=msg.from_user.id, text='Выберите режим работы калькулятора.', reply_markup=buttons1)

def rational_first_value(msg: telebot.types.Message):
    user_info = {}
    user_info['a1'] = msg.text
    msg = bot.send_message(msg.chat.id, 'Введите второе число:')
    bot.register_next_step_handler(msg, rational_secondt_value)


def rational_secondt_value(msg: telebot.types.Message, user_info):
    user_info['a2'] = msg.text
    msg = bot.send_message(msg.chat.id, 'Выберите действие: ', reply_markup=cb.buttons2)
    bot.register_next_step_handler(msg, rational_counter)


def rational_counter(msg: telebot.types.Message, user_info):
    a1_f = float(user_info['a1'])
    a2_f = float(user_info['a2'])
    if msg =='+':
        result = a1_f + a2_f
    elif msg =='-':
        result = a1_f - a2_f
    elif msg =='*':
        result = a1_f * a2_f
    elif msg =='/':
        result = a1_f / a2_f
    msg = bot.send_message(msg.chat.id, f'Результат: {result} ')


bot.polling()