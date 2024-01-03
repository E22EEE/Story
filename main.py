from config import Config
import requests
import telebot
from telebot import types
from timeit import default_timer as timer
from kvsqlite.sync import Client

owner = 5154904380

token = Config.TG_BOT_TOKEN

db = Client("ipInfo.sqlite", "users")

bot = telebot.TeleBot(
    token,
    skip_pending=True,
    parse_mode="markdown",
    disable_web_page_preview=True
    )

def sendN(msg, lang):
    bot.send_message(owner, f'''*- مستخدم جديد:
أسمه:* [{msg.from_user.first_name}](tg://user?id={msg.from_user.id})*.
أيديه:* `{msg.from_user.id}`.
*يوزره: @{msg.from_user.username}.
لغه الادخال: {lang}*
ـ————————————'''.replace("@None", "لايوجد"))

@bot.message_handler(commands=["start"])
def welcome(msg):
    idu = msg.from_user.id
    ArMsg = f"*اهلا وسهلا* [{msg.from_user.first_name}](tg://user?id={idu}).\n*في بوت معلومات الايبي\nفقط ارسل الايبي.*"
    EnMsg = f"*Welcome* [{msg.from_user.first_name}](tg://user?id={idu}).\n*To IP Information Bot\n Just send Me the IP.*"
    if idu == owner:
        btns = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("الاحصائيات", callback_data="stats")
        btn2 = types.InlineKeyboardButton("اذاعة", callback_data="brod")
        btn3 = types.InlineKeyboardButton("أرسل التخزين", callback_data="file")
        btns.row(btn2, btn1)
        btns.row(btn3)
        bot.reply_to(msg, "*أهلا بك عزيزي المالك*", reply_markup=btns)
    if db.exists(f"user_{idu}") and db.get(f"user_{idu}")["lang"] == "ar":
        btn = types.InlineKeyboardMarkup(row_width=1)
        dev = types.InlineKeyboardButton("المطور", "t.me/K_x_G")
        lang = types.InlineKeyboardButton("تغير اللغة", callback_data="Clang")
        btn.row(lang)
        btn.row(dev)
        bot.reply_to(msg, ArMsg, reply_markup=btn)
    if db.exists(f"user_{idu}") and db.get(f"user_{idu}")["lang"] == "en":
        btn = types.InlineKeyboardMarkup(row_width=1)
        dev = types.InlineKeyboardButton("Dev", "t.me/K_x_G")
        lang = types.InlineKeyboardButton("Change Language", callback_data="Clang")
        btn.row(lang)
        btn.row(dev)
        bot.reply_to(msg, EnMsg, reply_markup=btn)
    if not db.exists(f"user_{idu}"):
        btns = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("العربية", callback_data="ar")
        btn2 = types.InlineKeyboardButton("English", callback_data="en")
        btns.row(btn2, btn1)
        bot.reply_to(msg, '''*أهلا بك عزيزي ، أختر لغتك من فضلك.
ـ=================
ـwelcome bro, Please choose your language
ـ=================*''', reply_markup=btns)

@bot.message_handler(func=lambda message: True)
def send(msg):
    idu = msg.from_user.id
    ip = msg.text
    rq = requests.get(f'http://ip-api.com/json/{ip}?fields=60551167',timeout=3)
    data = rq.json()
    if data["status"] == "success":
        lat = data["lat"]
        lon = data["lon"]
        loc = f"{lat}, {lon}"
        if db.exists(f"user_{idu}") and db.get(f"user_{idu}")["lang"] == "ar":
            bot.send_location(msg.chat.id, latitude=lat ,longitude=lon, horizontal_accuracy=data["offset"])
            bot.reply_to(msg, f'''*- معلومات الايبي* `{ip}`:*
القارة: {data["continent"]}.
الدولة: {data["country"]}.
المحافظة: {data["regionName"]}.
المدينة: {data["city"]}.
خطوط الطول و العرض:* `{loc}`.
*المنطقة الزمنية: {data["timezone"]}.
شركة الإتصالات: {data['org']}.
هل الايبي تابع لأستضافة: {data["hosting"]}.
هل الايبي بروكسي: {data['proxy']}.
------ ------- ------- -------*
[تابعنا للمزيد](t.me/teamon404)'''.replace("False", "لا").replace("True", "نعم"))
        if db.exists(f"user_{idu}") and db.get(f"user_{idu}")["lang"] == "en":
            bot.send_location(msg.chat.id, latitude=lat ,longitude=lon, horizontal_accuracy=data["offset"])
            bot.reply_to(msg, f'''*- inFo* `{ip}`:*
Continent: {data["continent"]}.
Country: {data["country"]}.
Region: {data["regionName"]}.
City: {data["city"]}.
lat & lon:* `{loc}`.
*Timezone: {data["timezone"]}.
Telecom Company: {data['org']}.
Is Host?: {data["hosting"]}.
Is Proxy?: {data['proxy']}.
------ ------- ------- -------*
[Follow us](t.me/teamon404)'''.replace("False", "No").replace("True", "Yes"))
        else:
            btns = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton("العربية", callback_data="ar")
            btn2 = types.InlineKeyboardButton("English", callback_data="en")
            btns.row(btn2, btn1)
            bot.reply_to(msg, '''*أهلا بك عزيزي ، أختر لغتك من فضلك.
ـ=================
ـwelcome bro, Please choose your language
ـ=================*''', reply_markup=btns)
    else:
        if db.exists(f"user_{idu}") and db.get(f"user_{idu}")["lang"] == "ar":
            bot.reply_to(msg, "*حدث خطأ، تأكد من القيمة المدخلة أو حاول لاحقًا*")
        if db.exists(f"user_{idu}") and db.get(f"user_{idu}")["lang"] == "en":
            bot.reply_to(msg, "*An error occurred, verify the value entered or try again later*")
        else:
            btns = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton("العربية", callback_data="ar")
            btn2 = types.InlineKeyboardButton("English", callback_data="en")
            btns.row(btn2, btn1)
            bot.reply_to(msg, '''*أهلا بك عزيزي ، أختر لغتك من فضلك.
ـ=================
ـwelcome bro, Please choose your language
ـ=================*''', reply_markup=btns)

def Brod(bot,message):
    ids = []
    keys = db.keys("user_%")
    for id in keys:
        ids.append(int(db.get(id[0])["id"]))
    i ,F ,T = 0,0,0
    start   = timer()
    brodMM  = bot.send_message(
        chat_id=message.from_user.id,
        text=f"""بدأت الاذاعة:
عدد المستخدمين : {len(ids)}
نجحت لـ : {T}/{T+F}  -  0%
فشلت لـ : {F}/{T+F}  -  0%
تم الارسال لـ : 0%"""
    )
    for Id in ids:
        i = i+1
        try:
            bot.copy_message(
                chat_id=Id,
                message_id=message.id,
                from_chat_id=message.chat.id,
            )
            T = T+1
        except Exception as e:
            print(e)
            F = F+1
        if i%2==0:
            bot.edit_message_text(
                    chat_id=brodMM.chat.id,
                    message_id=brodMM.id,
                    text=f"""بدأت الاذاعة:
    عدد المستخدمين  : {len(ids)}
    نجحت لـ : {T}/{T+F}  -  {round((T/(T+F))*100,2)}%
    فشلت لـ : {F}/{T+F}  -  {round((F/(T+F))*100,2)}%
    تم الارسال لـ : {round(((T+F)/len(ids))*100,2)}%"""
                )
    end = timer()
    ttt = end-start
    bot.edit_message_text(
                chat_id=brodMM.chat.id,
                message_id=brodMM.id,
                text=f"""أنتهت الاذاعة:
عدد المستخدمين : {len(ids)}
نجحت لـ : {T}/{T+F}  -  {round((T/(T+F))*100,2)}%
فشلت لـ : {F}/{T+F}  -  {round((F/(T+F))*100,2)}%
تم الارسال لـ : {round(((T+F)/len(ids))*100,2)}%
استغرقت الاذاعة: {round(ttt/60,1)} دقائق"""
            )

def brodM(msg):
    if msg.text == 'cancel':
        bot.reply_to(
            msg,
            "تم الالغاء"
        )
        return
    Brod(
        bot=bot,
        message=msg,
    )

@bot.callback_query_handler(func=lambda call: True)
def calldata(call):
    idu = call.from_user.id
    if call.data == "backAd":
        bt = types.InlineKeyboardMarkup(row_width=1)
        btn11 = types.InlineKeyboardButton("الاحصائيات", callback_data="stats")
        btn22 = types.InlineKeyboardButton("اذاعة", callback_data="brod")
        btn33 = types.InlineKeyboardButton("أرسل التخزين", callback_data="file")
        bt.row(btn22, btn11)
        bt.row(btn33)
        bot.edit_message_text(text="*أهلا بك عزيزي المالك*", chat_id=idu, message_id=call.message.id,reply_markup=bt)
    if call.data == "stats":
        b = types.InlineKeyboardMarkup(row_width=1)
        ba = types.InlineKeyboardButton("رجوع",callback_data="backAd")
        b.row(ba)
        qa = len(db.keys("user_%"))
        bot.edit_message_text(f"*أهلا بك عزيزي المالك في قسم الاحصائيات\nعدد مستخدمين البوت: {qa}.*", chat_id=idu, message_id=call.message.id,reply_markup=b)
    elif call.data == "brod":
        bot.send_message(idu, "ارسل الرسالة او `cancel` للالغاء")
        bot.register_next_step_handler(call.message, brodM)
    elif call.data == "file":
        bot.send_document(idu, open("ipInfo.sqlite","rb"))
    elif call.data == "ar":
        btn = types.InlineKeyboardMarkup(row_width=1)
        dev = types.InlineKeyboardButton("المطور", "t.me/K_x_G")
        lang = types.InlineKeyboardButton("تغير اللغة", callback_data="Clang")
        btn.row(lang)
        btn.row(dev)
        bot.edit_message_text(f"*اهلا وسهلا* [{call.from_user.first_name}](tg://user?id={idu}).\n*في بوت معلومات الايبي\nفقط ارسل الايبي.*", chat_id=idu, message_id=call.message.id, reply_markup=btn)
        db.set(f"user_{idu}",{"id":idu,"lang":"ar"})
        sendN(call, "Ar")
    elif call.data == "en":
        btn = types.InlineKeyboardMarkup(row_width=1)
        dev = types.InlineKeyboardButton("Dev", "t.me/K_x_G")
        lang = types.InlineKeyboardButton("Change Language", callback_data="Clang")
        btn.row(lang)
        btn.row(dev)
        bot.edit_message_text(f"*Welcome* [{call.from_user.first_name}](tg://user?id={idu}).\n*To IP Information Bot\n Just send Me the IP.*", chat_id=idu, message_id=call.message.id, reply_markup=btn)
        db.set(f"user_{idu}",{"id":idu,"lang":"en"})
        sendN(call, "En")
    elif call.data == "Clang":
        if db.exists(f"user_{idu}") and db.get(f"user_{idu}")["lang"] == "ar":
            db.set(f"user_{idu}",{"id":idu,"lang":"en"})
            bot.edit_message_text(f"*Done Change The Language to English\nSend /start*", chat_id=idu, message_id=call.message.id)
        elif db.exists(f"user_{idu}") and db.get(f"user_{idu}")["lang"] == "en":
            db.set(f"user_{idu}",{"id":idu,"lang":"ar"})
            bot.edit_message_text(f"*تم تغيير اللغة الى العربية\nأرسل /start*", chat_id=idu, message_id=call.message.id)

print("-- Bot Started...")
bot.infinity_polling()
