import telebot
import time

bot = telebot.TeleBot('5799483261:AAE7meD3rM9xAj1vz-IZgFYa-CpeNOvc2-Q')

tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))

del_buttons = telebot.types.ReplyKeyboardRemove()
 
buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Комплексные'),
             telebot.types.KeyboardButton('Рациональные'),
             telebot.types.KeyboardButton('Получить логи'),
             telebot.types.KeyboardButton('Ещё не определился'))
 
buttons2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2.row(telebot.types.KeyboardButton('+'),
             telebot.types.KeyboardButton('-'))
buttons2.row(telebot.types.KeyboardButton('*'),
             telebot.types.KeyboardButton('/'))
 
 
# @bot.message_handler(commands=['log'])
# def get_log(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id,
#                      text='Лог программы',
#                      reply_markup=del_buttons)
#     bot.send_document(chat_id=msg.from_user.id, document=open('Log_calc.log', 'rb'))
 
 
# @bot.message_handler(content_types=['document'])
# def hello(msg: telebot.types.Message):
#     file = bot.get_file(msg.document.file_id)
#     downloaded_file = bot.download_file(file.file_path)
#     with open(msg.document.file_name, 'wb') as f_out:
#         f_out.write(downloaded_file)
    # Открываем и импортируем
 
 
@bot.message_handler()
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Здравствуйте.\nВыберите режим работы калькулятора.',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)
    with open('Log_calc.txt', 'a', encoding='utf-8') as a:
        a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
        a.writelines('\n')

 
 
def answer(msg: telebot.types.Message):
    if msg.text == 'Комплексные':
        bot.register_next_step_handler(msg, complex_first_value_real)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите действительную часть первого числа: ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        with open('Log_calc.txt', 'a', encoding='utf-8') as a:
            a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
            a.writelines('\n')
    elif msg.text == 'Рациональные':
        bot.register_next_step_handler(msg, rational_first_value)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите первое число: ',
                         reply_markup=del_buttons)
        with open('Log_calc.txt', 'a', encoding='utf-8') as a:
            a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
            a.writelines('\n')
    elif msg.text == 'Получить логи':
        bot.send_message(chat_id=msg.from_user.id,
                        text='Лог программы',
                        reply_markup=del_buttons)
        bot.send_document(chat_id=msg.from_user.id, document=open('Log_calc.log', 'rb'))
    elif msg.text == 'Ещё не определился':
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Возвращайтесь, когда определитесь.')
        with open('Log_calc.txt', 'a', encoding='utf-8') as a:
            a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
            a.writelines('\n')
    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки.')
        with open('Log_calc.txt', 'a', encoding='utf-8') as a:
            a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
            a.writelines('\n') 
        bot.send_message(chat_id=msg.from_user.id, text='Выберите режим работы калькулятора.', reply_markup=buttons1)


def complex_first_value_real(msg: telebot.types.Message):
    user_info = {}
    user_info['a1_real'] = msg.text
    msg = bot.send_message(msg.chat.id, 'Введите мнимую часть первого числа без символа i: ')
    bot.register_next_step_handler(msg, complex_first_value_imag, user_info)
    with open('Log_calc.txt', 'a', encoding='utf-8') as a:
        a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
        a.writelines('\n') 


def complex_first_value_imag(msg: telebot.types.Message, user_info):
    user_info['a1_imag'] = msg.text
    msg = bot.send_message(msg.chat.id, 'Введите действительную часть второго числа: ')
    bot.register_next_step_handler(msg, complex_second_value_real, user_info)
    with open('Log_calc.txt', 'a', encoding='utf-8') as a:
        a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
        a.writelines('\n') 

def complex_second_value_real(msg: telebot.types.Message, user_info):
    user_info['a2_real'] = msg.text
    msg = bot.send_message(msg.chat.id, 'Введите мнимую часть второго числа без символа i: ')
    bot.register_next_step_handler(msg, complex_second_value_imag, user_info)
    with open('Log_calc.txt', 'a', encoding='utf-8') as a:
        a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
        a.writelines('\n') 

def complex_second_value_imag(msg: telebot.types.Message, user_info):
    user_info['a2_imag'] = msg.text
    msg = bot.send_message(msg.chat.id, 'Выберите действие: ', reply_markup = buttons2)
    bot.register_next_step_handler(msg, complex_counter, user_info)
    with open('Log_calc.txt', 'a', encoding='utf-8') as a:
        a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
        a.writelines('\n') 

def complex_counter(msg: telebot.types.Message, user_info):

    a1_real_int = int(user_info['a1_real'])
    a1_imag_int = int(user_info['a1_imag'])
    a2_real_int = int(user_info['a2_real'])
    a2_imag_int = int(user_info['a2_imag'])

    if msg.text =='+':
        msg = bot.send_message(msg.chat.id, f'Результат: {a1_real_int + a2_real_int}  + ({a1_imag_int + a2_imag_int}i)', 
                               reply_markup=buttons1)
    elif msg.text =='-':
        msg = bot.send_message(msg.chat.id, f'Результат: {a1_real_int - a2_real_int}  + ({a1_imag_int - a2_imag_int}i)', 
                               reply_markup=buttons1)
    elif msg.text =='*':
        msg = bot.send_message(msg.chat.id, f'Результат: {a1_real_int * a2_real_int  - a1_imag_int * a2_imag_int} + ({a1_imag_int * a2_real_int + a1_real_int * a2_imag_int}i)', 
                               reply_markup=buttons1)
    elif msg.text =='/':
        msg = bot.send_message(msg.chat.id, f'Результат: {(a1_real_int * a2_real_int + a1_imag_int * a2_imag_int) / (a2_real_int**2 + a2_imag_int**2)} + ({(a1_imag_int * a2_real_int - a1_real_int * a2_imag_int) /(a2_real_int**2 + a2_imag_int**2) }i)', 
                               reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)
    with open('Log_calc.txt', 'a', encoding='utf-8') as a:
        a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
        a.writelines('\n') 


# rational:
 
def rational_first_value(msg: telebot.types.Message):
    user_info = {}
    user_info['a1'] = msg.text
    msg = bot.send_message(msg.chat.id, 'Введите второе число:')
    bot.register_next_step_handler(msg, rational_second_value, user_info)
    with open('Log_calc.txt', 'a', encoding='utf-8') as a:
        a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
        a.writelines('\n') 


def rational_second_value(msg: telebot.types.Message, user_info):
    user_info['a2'] = msg.text
    msg = bot.send_message(msg.chat.id, 'Выберите действие: ', reply_markup = buttons2)
    bot.register_next_step_handler(msg, rational_counter, user_info)
    with open('Log_calc.txt', 'a', encoding='utf-8') as a:
        a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
        a.writelines('\n') 


def rational_counter(msg: telebot.types.Message, user_info):
    a1_f = float(user_info['a1'])
    a2_f = float(user_info['a2'])
    if msg.text =='+':
        msg = bot.send_message(msg.chat.id, f'Результат: {a1_f + a2_f}', reply_markup=buttons1)
    elif msg.text =='-':
        msg = bot.send_message(msg.chat.id, f'Результат: {a1_f - a2_f}', reply_markup=buttons1)
    elif msg.text =='*':
        msg = bot.send_message(msg.chat.id, f'Результат: {a1_f * a2_f}', reply_markup=buttons1)
    elif msg.text =='/':
        msg = bot.send_message(msg.chat.id, f'Результат: {a1_f / a2_f}', reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)
    with open('Log_calc.txt', 'a', encoding='utf-8') as a:
        a.writelines(f'Time: {tconv(msg.date)} User ID: {msg.from_user.id}; Text: {msg.text}; ')
        a.writelines('\n')  
 
bot.polling()