from config import Config
try:
	import telebot
	from telebot import types,TeleBot
	import requests
	from requests import post,get
except ImportError as e:
	print(e)
bot = TeleBot("5288347532:AAE5n7Yhx9zClkHO_ptVR2Y6Fv3u2OtEJGA");
User = "uaiuu";
Id = -1001803422591
@bot.message_handler(commands=["start"])
def Start(message):
	id = message.from_user.id
	Req = requests.get(f"https://api.telegram.org/bot{bot}/getchatmember?chat_id=@{User}&user_id={id}").text
	if id == User or 'member' in Req or 'creator' in Req or 'administartor':
		bot.reply_to(message,'''*• اهلا وسهلا تم التحقق بأنك مشترك في قناة البوت ✅ .*''',parse_mode='Markdown')
	else:
			Key = types.InlineKeyboardMarkup(row_width=1)
			Ch = types.InlineKeyboardButton("• اشترك الان",url=f"tg://user?id=-100{Id}")
			Key.add(Ch)
			bot.reply_to(message,f'''**• عزيزي عليك الاشتراك في قناة البوت لتتمكن من استخدامه ⁉️ | @{User} .**''',reply_markup=Key)
bot.infinity_polling(True)
# - - DeV CODE —> @A7aac
#The CODe Is Not Test !.
