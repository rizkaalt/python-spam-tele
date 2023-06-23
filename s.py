import telebot

bot = telebot.TeleBot('6230438718:AAHruSOW9tP1Ymu5dTlyrUjVZhkNRBKDBRs')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selamat datang di bot spam Rizka! Silakan gunakan perintah /spam untuk memulai spam ke diri sendiri 🗿.")

@bot.message_handler(commands=['spam'])
def send_spam(message):
    for i in range(99999):
        bot.reply_to(message, "P")

bot.polling()

print('LAG MAMPOS')	
executor.start_polling(dp)