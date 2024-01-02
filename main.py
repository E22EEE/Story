from telebot import *
from requests import *
from telebot.types import InlineKeyboardMarkup as Mk , 	   InlineKeyboardButton as btn 
Token = "6449900091:AAEA64nljWvoIQyCC_O4N-dxVbquuP9_iPE"
def check_join(idd):
	res = get(f"https://api.telegram.org/bot{Token}/getChatMember?chat_id=@ialhh&user_id={idd}").json()
	if res['ok']:
		x = res['result']['status']
		if (x == "creator" or x == "member" 
		or x == "administrator"):return True
	else:return False

bot = TeleBot(Token)
@bot.message_handler(content_types=['text'])
def join(message):
	idd = message.from_user.id
	sub = Mk().add(
	btn(text=bot.get_chat(f"@ialhh").title,url=f"t.me/ialhh"))
	if message.chat.type =="private":
			if not check_join(idd):
				bot.send_message(message.chat.id,
				f"*You must join* [this channel](t.me/ialhh) *to use me. After joining try again !*", parse_mode="Markdown" , 
				disable_web_page_preview=True,
				reply_markup=sub)
			else:
				bot.send_message(message.chat.id,
				"*Welcome to the mandatory subscription bot ..*",
				parse_mode="Markdown")
				# Complete your code below ! 
bot.infinity_polling()
