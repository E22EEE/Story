from config import Config
import telebot
bot = telebot.TeleBot(Config.TG_BOT_TOKEN )
@bot.message_handler(commands=['start'])
def hej(message):
 bot.reply_to(message,"*اهلا عزيزي ارسل النص المراد قلبه *",parse_mode="markdown")
 bot.register_next_step_handler(message,t)
def t(message):
 m = message.text
 a = m[::-1]
 bot.reply_to(message,f"""*
النص - {m}

التعديل - *{a}""",parse_mode="markdown")
bot.polling() 
