from config import Config

from pyrogram import Client, filters, types 
from requests import get
import json
import asyncio 

# bot helpers 
BOT_MESSAGE = {
    'JOIN_CHANLL':
                u'⦁ عذراً عليك الاشتراك في قناة البوت اولاً 🌵.\n⦁ رآبط القناة : @{}'
                u'',
    'DONE_JOIN_CHANNL':
                    u'تم التحقق من الاشتراك ✅ \n ارسل /start'
                    u''
}

def CHECK_JOIN_KEYBOARD(Channl: str):
    return types.InlineKeyboardMarkup([
        [
            types.InlineKeyboardButton(text='⦁ GIF متحركات ملصقات تمبلر', url=f't.me/{Channl}'),

        ]
    ])
def CHECK_JOIN_KEYBOARD(Channl: str):
    return types.InlineKeyboardMarkup([
        [
            types.InlineKeyboardButton(text='تحقق ♻️', callback_data='checkjoin')
        ]
    ])
def REDRESH_LANSHER(text: str):
    return types.InlineKeyboardMarkup([
        [
            types.InlineKeyboardButton(text=text, callback_data='NOT')
        ]
    ])

## api chack member join from channls
async def CHECK_USER_JOIN(api_key, channls_join: list, user_id : int):
    c ,r = None ,False
    statues = ['administrator','creator','member','restricted']
    for channl in channls_join:
        url =f"https://api.telegram.org/bot{api_key}/getChatMember?chat_id=@{channl}&user_id={str(user_id)}"
        respons = get(url)
        JSObj = json.loads(respons.text) 
        user_state = JSObj['result']['status']
        if user_state in statues:
            r = True 
        else : 
            r = False
            c = channl
            return r,c
    return r,c

API_KEY = '5288347532:AAE5n7Yhx9zClkHO_ptVR2Y6Fv3u2OtEJGA'
BOT_CHANNL = ['uaiuu']
app = Client(
    'rad',
    bot_token=API_KEY, 
    api_id=22119881 , # userbot api id  
    api_hash='95f5f60466a696e33a34f297c734d048' # userbot api hash
)

@app.on_message(filters.regex('^/start$') & filters.private)
async def START_BOT(_, message: types.Message):
    chat_id, message_id, user_id = message.chat.id, message.id, message.from_user.id
    join_, channl = await CHECK_USER_JOIN(API_KEY,BOT_CHANNL, user_id)
    if not join_:
        await app.send_message(chat_id=chat_id, text=BOT_MESSAGE['JOIN_CHANLL'].format(channl), reply_markup=CHECK_JOIN_KEYBOARD(channl))
        return 
    await app.send_message(chat_id, '- ياهلا حياك 🌵.\n⦁ قناة البوت : @uaiuu .\n⦁ مطور البوت : @zEezzz .')


@app.on_callback_query(filters.regex('^checkjoin$'))
async def CHAECK_JOIN(_, query: types.CallbackQuery):
    await app.edit_message_text(text='انتظر قليلاً .', reply_markup=REDRESH_LANSHER('تحقق ♻️'), chat_id=query.message.chat.id, message_id=query.message.id)
    await asyncio.sleep(0.3)
    join_, channl = await CHECK_USER_JOIN(API_KEY, BOT_CHANNL, query.from_user.id)
    if not join_:
        await app.edit_message_text(text=BOT_MESSAGE['JOIN_CHANLL'].format(channl), reply_markup=CHECK_JOIN_KEYBOARD(channl) ,chat_id= query.message.chat.id, message_id=query.message.id)    
        await app.answer_callback_query(query.id, '❌ تأكد من الاشتراك في القناة و اعد النحاولة ❌.', show_alert=True)  
        return
    await app.edit_message_text(text=BOT_MESSAGE['DONE_JOIN_CHANNL'], chat_id= query.message.chat.id, message_id=query.message.id)



asyncio.run(app.run())
