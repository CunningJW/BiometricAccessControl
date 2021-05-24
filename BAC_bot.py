import telebot
from telebot import types
import subprocess
import time
import sys

bot = telebot.TeleBot('1706542177:AAFuKi6E9b0EcEi2F_M0ZNDrYB9VA7oA9nA')


class Registrator:
    #сюда дописать нормальный класс, предположительно отдельно
    occupied = False
    process = None

class Recognizer:
    #сюда дописать нормальный класс, предположительно отдельно
    status = False
    process = None


reg = Registrator()
rec = Recognizer()

@bot.message_handler(commands=['hello', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Выберите команду:', reply_markup = markup)

@bot.message_handler(commands=['register'])
def send_welcome(message):
    if reg.occupied:
        bot.send_message(message.from_user.id,"В данный момент происходит регистрация")
    else:
        reg.occupied = True
        bot.send_message(message.from_user.id,"Регистрирую пользователя в системе...")
        reg_process = subprocess.run(['python','registration.py','-user', str(message.from_user.id)])
        bot.send_message(message.from_user.id,"Регистрация прошла успешно")


@bot.message_handler(commands=['start_cam'])
def send_welcome(message):
    rec.process = subprocess.Popen(['python','test.py'])
    bot.send_message(message.from_user.id,"Запуск камеры...")


@bot.message_handler(commands=['stop_cam'])
def send_welcome(message):
    rec.process.terminate()
    bot.send_message(message.from_user.id,"Остановка камеры...")

# @bot.message_handler(commands=['test_1'])
# def test1(message):
#     kek.status = not kek.status
#     bot.send_message(message.from_user.id,"Статус: {0}".format(kek.status))
#
# @bot.message_handler(commands=['test_2'])
# def test2(message):
#     if kek.status:
#         bot.send_message(message.from_user.id, 'Можно регистрироваться')
#     else:
#         bot.send_message(message.from_user.id, 'Процесс занят')


markup = types.ReplyKeyboardMarkup()
itembtnStartCam = types.KeyboardButton('/start_cam')
itembtnStopCam = types.KeyboardButton('/stop_cam')
itembtnRegister = types.KeyboardButton('/register')
# itembtnTest1 = types.KeyboardButton('/test_1')
# itembtnTest2 = types.KeyboardButton('/test_2')
markup.row(itembtnStartCam, itembtnStopCam)
markup.row(itembtnRegister)
# markup.row(itembtnTest1, itembtnTest2)







bot.polling(none_stop=True)
