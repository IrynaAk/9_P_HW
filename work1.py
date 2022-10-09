
from asyncore import read
from webbrowser import get
import telebot

# TOKEN = '5623640432:AAEchkVohl7hXhhvtN8h0KsHm81deprdLuk'
# bot = telebot.TeleBot (TOKEN)

# @bot.message_handler()
# def answer_view_data(msg: telebot.types.Message):
#     with open('Data.txt', 'rt', encoding='utf-8') as a:
#         data= a.read()
#         bot.send_message(chat_id=msg.from_user.id, text=f'{data}')


# def get_info ():
#     info = []
#     last_name = input('Введите фамилию: ')
#     info.append(last_name)
#     first_name = input('Введите имя: ')
#     info.append(first_name)
#     phone_number = ''
#     valid =False
#     while not valid:
#         try:
#             phone_number = input('Введите номер телефона: ')
#             if len(phone_number) != 11:
#                 print('В номере телефона должно быть 11 цифр.')
#             else:
#                 phone_number = phone_number
#                 valid = True
#         except:
#             print('Номер телефона должен состоять только из цифр.')
#     info.append(phone_number)
#     description = input('Введите описание: ')
#     info.append(description)
#     print(info)

# # get_info ()

# def write_data():
#     with open('Data.txt', 'a', encoding='utf-8') as a:
#         a.writelines('\n')
#         for i in get_info():
#             a.writelines(f'\n{i}')
        


# Export

def export_data():
    with open('Data.txt', 'r',encoding='utf-8') as a,open ('Export.csv','a', encoding='utf-8') as b:
        b.write(a.read())
        b.write('\n')


# Export with commas

def export_with_commas():
    with open('Data.txt', 'r', encoding='utf-8') as d:
        lst = d.readlines()
    s = ''
    for i, elem in enumerate(lst):
        if elem != '\n':
            s += elem.strip()+', '
        else:
            with open('Export.csv', 'a', encoding='utf-8') as mf:
                mf.write(s + '\n')
            s = ''


# Import

def import_data():
    with open('Import.txt', 'r') as a, open ('Data.txt','a') as b:
        read = a.read()
        read_2 = read.replace(', ', '\n')
        b.writelines('\n')
        b.write(f'\n{read_2}')

    



      