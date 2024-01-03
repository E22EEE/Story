from config import Config
import telebot
import requests
tokzz=Config.TG_BOT_TOKEN
bot = telebot.TeleBot("tokzz")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ارسل ال ip.")



@bot.message_handler(func=lambda message: True)
def ip_lookup(message):
    try:
        ip_address = message.text
        response = requests.get("http://ip-api.com/json/" + ip_address)

        if response.status_code == 200:
            data = response.json()
            output = "IP Address: " + data["query"] + "\n"
            output += "الحالة: " + data["status"] + "\n"
            output += "القارة: " + data.get("continent", "N/A") + "\n"
            output += "كود القارة: " + data.get("continentCode", "N/A") + "\n"
            output += "الدولة: " + data["country"] + "\n"
            output += "كود الدولة: " + data["countryCode"] + "\n"
            output += "منطقة: " + data["region"] + "\n"
            output += "اسم المنطقة: " + data["regionName"] + "\n"
            output += "المدينة: " + data["city"] + "\n"
            output += "يصرف: " + data.get("district", "N/A") + "\n"
            output += "رمز بريدي: " + data["zip"] + "\n"
            output += "خط العرض: " + str(data["lat"]) + "\n"
            output += "خط الطول: " + str(data["lon"]) + "\n"
            output += "الوحدة الزمنية: " + data["timezone"] + "\n"
            output += "عوض: " + str(data.get("offset", "N/A")) + "\n"
            output += "عملة: " + data.get("currency", "N/A") + "\n"
            output += "ISP: " + data["isp"] + "\n"
            output += "منضمة: " + data["org"] + "\n"
            output += "AS: " + data["as"] + "\n"
            output += "AS Name: " + data.get("asname", "N/A") + "\n"
            output += "Mobile: " + str(data.get("mobile", "N/A")) + "\n"
            output += "Proxy: " + str(data.get("proxy", "N/A")) + "\n"
            output += "Hosting: " + str(data.get("hosting", "N/A")) + "\n"

            bot.reply_to(message, output)
        else:
            bot.reply_to(message, "Failed to get data from API")
    except:
        bot.reply_to(message, "An error occurred. Please try again.")




bot.polling()
