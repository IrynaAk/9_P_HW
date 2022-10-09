import work1 as w1
import telebot
from telebot import types

TOKEN = '5623640432:AAEchkVohl7hXhhvtN8h0KsHm81deprdLuk'
bot = telebot.TeleBot (TOKEN)


@bot.message_handler(commands=['start'])
def choice(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    view_pb = types.KeyboardButton('Просмотр')
    add_pb = types.KeyboardButton('Добавление')
    export_pb = types.KeyboardButton('Экспорт')
    import_pb = types.KeyboardButton('Импорт')
    exit_pb = types.KeyboardButton('Выход')

    markup.add(view_pb, add_pb, export_pb, import_pb, exit_pb)
    # bot.send_message(chat_id=msg.from_user.id, text=f'Выберите действие:')
    bot.send_message(chat_id=msg.from_user.id, text=f'Выберите действие:', reply_markup = markup)


@bot.message_handler()
def answer(msg: telebot.types.Message):
    if msg.text == 'Просмотр':
        bot.send_message(chat_id=msg.from_user.id, text=f'Вы выбрали {msg.text}')
        with open('Data.txt', 'rt', encoding='utf-8') as a:
            data= a.read()
            bot.send_message(chat_id=msg.from_user.id, text=f'{data}')
    elif msg.text == 'Добавление':
        bot.send_message(chat_id=msg.from_user.id, text=f'Вы выбрали {msg.text}. Введите фамилию, имя, телефон, описание через запятую.')
        bot.register_next_step_handler(msg, get_info_bot)
    elif msg.text == 'Экспорт':
        bot.send_message(chat_id=msg.from_user.id, 
                         text=f'Вы выбрали {msg.text}. Выберите вариант выгрузки: 1 - экспорт в столбик, 2 - экспорт в строку')
        bot.register_next_step_handler(msg, export_bot)
    elif msg.text == 'Импорт':
        bot.send_message(chat_id=msg.from_user.id, 
                         text=f'Вы выбрали {msg.text}. Сохраните файл с названием \'Import.txt\' в папке проекта. Подтвердите сохранение набрав слово \'да\'')
        bot.register_next_step_handler(msg, import_bot)
    elif msg.text == 'Выход':
        bot.send_message(chat_id=msg.from_user.id, 
                         text=f'До встречи! Для возобновления работы наберите команду start')
    else:
        bot.send_message(chat_id=msg.from_user.id, 
                         text=f'Чтобы вернуться в основное меню, наберите команду start и выберите нужный вариант.')
        return


def export_bot (msg: telebot.types.Message):
    if msg.text == '1':
        w1.export_data()        
        bot.send_message(chat_id=msg.from_user.id, 
                         text=f'Выгрузка закончена.Проверьте файл Export.csv в папке проекта. \
                         Для продолжения работы наберите команду start.')
    elif msg.text == '2':
        w1.export_with_commas()
        bot.send_message(chat_id=msg.from_user.id, 
                         text=f'Выгрузка закончена.Проверьте файл Export.csv в папке проекта. \
                         Для продолжения работы наберите команду start.')
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Выбран неверный вариант.')


def import_bot (msg: telebot.types.Message):
    if msg.text == 'да':
        w1.import_data()      
        bot.send_message(chat_id=msg.from_user.id, text=f'Импорт закончен, для продолжения работы наберите команду start.')
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Выбран неверный вариант.')



def get_info_bot (msg: telebot.types.Message):
    info = msg.text.split(', ')
    with open('Data.txt', 'a', encoding='utf-8') as a:
        a.writelines('\n')
        for i in info:
            a.writelines(f'\n{i}')
    bot.send_message(chat_id=msg.from_user.id, text=f'Данные внесены. Для продолжения работы наберите команду start.')


bot.polling()