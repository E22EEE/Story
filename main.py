from config import Config
from pyrogram import enums
import pyshorteners ,requests , asyncio
from pyrogram import Client, filters ,enums
from pyrogram.types import Message
from pyrogram.types import *
from pyrogram import Client , filters
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
from pyrogram.enums import ChatMemberStatus
from datetime import datetime
from random import choice, randint 
from pyrogram import Client, filters 
from pyrogram.types import (
  InlineKeyboardMarkup,
  InlineKeyboardButton,
  CallbackQuery
)
import os
#os.system("pip install pyrogram && pip install tgcrypto && pip install pyromod && clear")

from pyrogram import Client, filters, idle
from pyromod import listen
from pyrogram.enums import ParseMode, ChatMemberStatus  
import os
import random
import sqlite3
import re
from requests import *
rickthon = Client("rickthon - Pyrogram",
api_id=Config.APP_ID,
api_hash=Config.API_HASH,
bot_token=Config.TG_BOT_TOKEN )
''
LOG = -1002123739799

db = sqlite3.connect('rotbah.db',check_same_thread=False)
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS msgtext (chat_id TEXT, user_id TEXT)")

def add_chat_message_0text(chat_id,user_id):
  try:
    cr.execute(f"insert into msgtext (chat_id,user_id) values ('{chat_id}', '{user_id}')")
    db.commit()
    return True
  except Exception as e:
    return e

def show_chat_message_0text(chat_id,user_id):
  try:
    cr.execute(f"select * from msgtext where chat_id = '{chat_id}' and user_id = '{user_id}'")
    return cr.fetchall()
  except Exception as e:
    return e

     
@rickthon.on_message(filters.text & filters.private)    
async def short(rickthon, message):
       e= message.text
       ur = f"https://dev-urltopac.pantheonsite.io/bbbbbi.php?url={e}"
       u = requests.get(ur).json()
       g = u["url"][0]["url"]
       h = u["meta"]["title"]
       await rickthon.send_video(message.chat.id,g,
       f"الوصف : {h}")

mutes = []
@rickthon.on_message(filters.regex("^كتم$") & filters.group)
async def mute(app,message):
   member = await message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await message.reply("**Only chat admins can use this command**")
   else:
     if not message.reply_to_message:
       return await message.reply("**• You must reply to an user first**")
     member = await message.chat.get_member(message.reply_to_message.from_user.id)
     if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       return await message.reply("**You can't mute chat admin**")
     chat_id = str(message.chat.id)
     user_id = str(message.reply_to_message.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
     if x in mutes:
       return await message.reply("**This user already muted in this chat**")
     else:
       mutes.append(x)
       return await message.reply("**{} has muted successfully by {} .**".format(message.reply_to_message.from_user.mention,message.from_user.mention))
       
@rickthon.on_message(filters.regex("^الغاء الكتم$") & filters.group)
async def unmute(app,message):
   member = await message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await message.reply("**Only chat admins can use this command**")
   else:
     if not message.reply_to_message:
       return await message.reply("**• You must reply to an user first**")
     member = await message.chat.get_member(message.reply_to_message.from_user.id)
     if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       return await message.reply("**You can't unmute chat admin**")
     chat_id = str(message.chat.id)
     user_id = str(message.reply_to_message.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
     if not x in mutes:
       return await message.reply("**This user already unmuted in this chat**")
     else:
       mutes.remove(x)
       return await message.reply("**{} has unmuted successfully by {} .**".format(message.reply_to_message.from_user.mention,message.from_user.mention))

@rickthon.on_message(filters.command("dmutes") & filters.group)
def get_dmute(app, message):
   if len(mutes) == 0: return
   member = message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return message.reply("**Only chat admins can use this command**")
   ch = message.chat.id
   c = 0
   text = "• Mutes list in this chat :\n\n"
   for a in mutes:
     chat_id = int(a.split("@")[0])
     user_id = int(a.split("@")[1])
     if chat_id == ch:
        user = rickthon.get_users(user_id)
        text += f"- {user.mention}\n"
        c += 1
   if c == 0: return message.reply("**No one muted in this chat**")
   message.reply(f"**{text}**")

@rickthon.on_message(filters.group)
def del_msg(_,m):
   if m.from_user:
     chat_id = str(m.chat.id)
     user_id = str(m.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
   for a in mutes:
     if a == x: 
       m.delete()
       break




@rickthon.on_message(filters.regex("^كت$") & filters.group)
@rickthon.on_edited_message(filters.regex("^كت$") & filters.group)
async def game_6(client, message):
   f = "rancutt"
   t = message.chat.id
   r = randint(2, 141)
   a = await rickthon.get_messages("rancutt", r)
   id = message.from_user.id
   await message.reply(
      f"- ‹ {message.from_user.mention} ›\n{a.text}",
      reply_markup=InlineKeyboardMarkup(
      [
      [
      InlineKeyboardButton("التالي", callback_data=f"cut:{id}")
      ]
      ]
      )
   )
   
@rickthon.on_message(filters.regex("^رسائلي$") & filters.group)
async def delrdood(app,message):
   await message.reply(f"-› عدد رسائلك : {len(show_chat_message_0text(message.chat.id,message.from_user.id))}")

@rickthon.on_message(filters.text & filters.group, group=1)
async def gettt_rd(app, message):
   add_chat_message_0text(message.chat.id,message.from_user.id)


@rickthon.on_message(filters.regex("^ايدي$"))
async def myid(_,message):
   user = await message.chat.get_member(message.from_user.id)
   if user.status == ChatMemberStatus.OWNER:
      status = "المالك"
   elif user.status == ChatMemberStatus.ADMINISTRATOR:
      status = "المشرف"
   elif user.status == ChatMemberStatus.MEMBER:
      status = "العضو"
   a = await rickthon.get_chat(message.from_user.id)
   usr = await rickthon.get_chat(message.from_user.id)
   name = message.from_user.mention
   if message.from_user.username == None:
         user = "لايوجد"
   else:
         user = message.from_user.username
   id = message.from_user.id
   bio = a.bio
   caption = "اسمك : {}\nمعرفك : @{}\nايديك : `{}`\nرتبتك : {}\n- {}"
   if a.photo:
      async for photo in rickthon.get_chat_photos(message.from_user.id, limit=1):
         await message.reply_photo(
            photo.file_id,
            caption=caption.format(name,user,id,status,bio)
         )
   else:
      await message.reply(caption.format(name,user,id,status,bio))
 
@rickthon.on_message(filters.regex("^ايديه$"))
async def herid(_, message):
   user = await message.chat.get_member(message.reply_to_message.from_user.id)
   if user.status == ChatMemberStatus.OWNER:
      status = "المالك"
   elif user.status == ChatMemberStatus.ADMINISTRATOR:
      status = "المشرف"
   elif user.status == ChatMemberStatus.MEMBER:
      status = "العضو"
   a = await rickthon.get_chat(message.reply_to_message.from_user.id)
   usr = await rickthon.get_chat(message.from_user.id)
   name = message.reply_to_message.from_user.first_name
   if message.from_user.username == None:
         user = "لايوجد"
   else:
         user = message.reply_to_message.from_user.username
         id = message.reply_to_message.from_user.id
   bio = a.bio
   caption = "اسمه : {}\nمعرفه : @{}\nايديه : `{}`\nرتبته : {}\n- {}"
   if a.photo:
      async for photo in rickthon.get_chat_photos(message.reply_to_message.from_user.id, limit=1):
         await message.reply_photo(
            photo.file_id,
            caption=caption.format(name,user,id,status,bio)
         )
   else:
      await message.reply(caption.format(name,user,id,status,bio))
            

admin = 5582470474

#_____ انشاء قاعدة البيانات___
conn = sqlite3.connect('abd.db')

conn.execute('''CREATE TABLE IF NOT EXISTS USERS
         (CHAT_ID  PRIMARY KEY    NOT NULL,
         RANK            STRING     NOT NULL);''')

conn.close()


#____تخزين الرتب + ايدايات الاعضاء ___
def control_rank(CHAT_ID, RANK):
    connect = sqlite3.connect('abd.db')
    conn = connect.cursor()
    conn.execute('SELECT RANK FROM USERS WHERE (CHAT_ID={})'.format(CHAT_ID))
    entry = conn.fetchone()
    if entry is None:
        conn.execute("INSERT INTO  USERS VALUES (?, ?)", (CHAT_ID, RANK))
        connect.commit()
        conn.close()
    else:
        conn.execute("UPDATE USERS SET RANK=? WHERE CHAT_ID=?;", (RANK, CHAT_ID))
        connect.commit()
        conn.close()
#-------- كشف الرتب -------
def get_rank(CHAT_ID):
    connect = sqlite3.connect('abd.db')
    conn = connect.cursor()
    conn.execute('SELECT RANK FROM USERS WHERE (CHAT_ID={})'.format(CHAT_ID))
    rank = conn.fetchone()
    conn.close()
    if rank is not None:
        return rank[0]
    else:
        return []
@rickthon.on_message(filters.command(["رفع مدير"],prefixes=f"") & filters.group & filters.reply)
async def Knight(client, message):
     if message.reply_to_message:
     	control_rank(message.reply_to_message.from_user.id,"ma")
     	us = message.reply_to_message.from_user.username
     	na = message.reply_to_message.from_user.first_name
     	await message.reply("""**⌯︙المستخدم ↫[{}](t.me/{})
⌯︙تم ترقيته مدير**""".format(na,us),disable_web_page_preview=True)
@rickthon.on_message(filters.command(["رفع اساسي"],prefixes=f"") & filters.user(admin) & filters.group & filters.reply)
async def Knight(client, message):
      if message.reply_to_message:
      	control_rank(message.reply_to_message.from_user.id,"isic")
      	us = message.reply_to_message.from_user.username
      	na = message.reply_to_message.from_user.first_name
      	await message.reply("""**⌯︙المستخدم ↫[{}](t.me/{})
⌯︙تم ترقيته منشى اساسي**""".format(na,us),disable_web_page_preview=True)
@rickthon.on_message(filters.command(["رفع منشى"],prefixes=f"") & filters.user(admin) & filters.group & filters.reply)
async def Knight(client, message):
     if message.reply_to_message:
     	control_rank(message.reply_to_message.from_user.id,"mn")
     	us = message.reply_to_message.from_user.username
     	na = message.reply_to_message.from_user.first_name
     	await message.reply("""**⌯︙المستخدم ↫[{}](t.me/{})
⌯︙تم ترقيته منشى**""".format(na,us),disable_web_page_preview=True)
@rickthon.on_message(filters.command(["رفع ادمن"],prefixes=f"")& filters.user(admin) & filters.group & filters.reply)
async def Knight(client, message):
    if message.reply_to_message:
	    control_rank(message.reply_to_message.from_user.id,"ad")
	    us = message.reply_to_message.from_user.username
	    na = message.reply_to_message.from_user.first_name
	    await message.reply("""**⌯︙المستخدم ↫[{}](t.me/{})
⌯︙تم ترقيته ادمن**""".format(na,us),disable_web_page_preview=True)
@rickthon.on_message(filters.command(["رفع مميز"],prefixes=f"") & filters.user(admin) & filters.group & filters.reply)
async def Knight(client,message):
    if message.reply_to_message:
    	us = message.reply_to_message.from_user.username
    	na = message.reply_to_message.from_user.first_name
    	control_rank(message.reply_to_message.from_user.id, "Knight")
    	await message.reply("""**⌯︙المستخدم ↫[{}](t.me/{})
⌯︙تم ترقيته مميز**""".format(na,us),disable_web_page_preview=True)
@rickthon.on_message(filters.command(["رتبتي"],prefixes=f"") & filters.group)
async def my_rank(client, message):
    if message.from_user.id ==admin:
        await message.reply("رتبتك :  المالك ♕ ", reply_to_message_id=message.id)
    else:
        rank = get_rank(message.from_user.id)
        if rank == "Knight":
        	await message.reply("رتبتك : مميز", reply_to_message_id=message.id)
        elif rank == "ad":
        	await message.reply("رتبتك : الادمن", reply_to_message_id=message.id)
        elif rank == "ma":
        	await message.reply("رتبتك : المدير ", reply_to_message_id=message.id)
        elif rank == "mn":
        	await message.reply("رتبتك : المنشى", reply_to_message_id=message.id)
        elif rank == "isic":
        	await message.reply("رتبتك : المنشى الاساسي", reply_to_message_id=message.id)            	         
        else:
            await message.reply("رتبتك : عضو", reply_to_message_id=message.id)
def delete_rank(CHAT_ID, RANK):
    connect = sqlite3.connect('abd.db')
    conn = connect.cursor()
    conn.execute('DELETE FROM USERS WHERE (CHAT_ID={})'.format(CHAT_ID))
    connect.commit()
    conn.close()
    
@rickthon.on_message(filters.command(["تنزيل مدير"],prefixes=f"") & filters.group & filters.reply)
async def Knight(client, message):
     if message.reply_to_message:
     	delete_rank(message.reply_to_message.from_user.id,"ma")
     	us = message.reply_to_message.from_user.username
     	na = message.reply_to_message.from_user.first_name
     	await message.reply("""**⌯︙المستخدم ↫[{}](t.me/{})
⌯︙تم تنزيل المدير**""".format(na,us),disable_web_page_preview=True)
@rickthon.on_message(filters.command(["تنزيل اساسي"],prefixes=f"") & filters.user(admin) & filters.group & filters.reply)
async def Knight(client, message):
      if message.reply_to_message:
      	delete_rank(message.reply_to_message.from_user.id,"isic")
      	us = message.reply_to_message.from_user.username
      	na = message.reply_to_message.from_user.first_name
      	await message.reply("""**⌯︙المستخدم ↫[{}](t.me/{})
⌯︙تم تنزيل منشى اساسي**""".format(na,us),disable_web_page_preview=True)
@rickthon.on_message(filters.command(["تنزيل منشى"],prefixes=f"") & filters.user(admin) & filters.group & filters.reply)
async def Knight(client, message):
     if message.reply_to_message:
     	delete_rank(message.reply_to_message.from_user.id,"mn")
     	us = message.reply_to_message.from_user.username
     	na = message.reply_to_message.from_user.first_name
     	await message.reply("""**⌯︙المستخدم ↫[{}](t.me/{})
⌯︙تم تنزيل منشى**""".format(na,us),disable_web_page_preview=True)
@rickthon.on_message(filters.command(["تنزيل ادمن"],prefixes=f"")& filters.user(admin) & filters.group & filters.reply)
async def Knight(client, message):
    if message.reply_to_message:
	    delete_rank(message.reply_to_message.from_user.id,"ad")
	    us = message.reply_to_message.from_user.username
	    na = message.reply_to_message.from_user.first_name
	    await message.reply("""**⌯︙المستخدم ↫[{}](t.me/{})
⌯︙تم تنزيل الادمن**""".format(na,us),disable_web_page_preview=True)
@rickthon.on_message(filters.command(["تنزيل مميز"],prefixes=f"") & filters.user(admin) & filters.group & filters.reply)
async def Knight(client,message):
    if message.reply_to_message:
    	us = message.reply_to_message.from_user.username
    	na = message.reply_to_message.from_user.first_name
    	delete_rank(message.reply_to_message.from_user.id, "Knight")
    	await message.reply("""**⌯︙المستخدم ↫[{}](t.me/{})
⌯︙تم تنزيل المميز**""".format(na,us),disable_web_page_previe=True)

def get_rd(text, id):
    chat_id = str(id)
    text = text
    with open("getrdod.txt", "r+") as f:
       x = f.readlines()
       final = f"{chat_id}#{text}"
       for a in x:
         if final in a:
            return int(a.split(f"{final}ZAIDRD")[1].replace("\n",""))
    return False

'''
Programmed by : 🎖️ @DevZaid
   Channel -› • @Y88F8
'''
def add_rd(text, id, rd) -> bool:
    chat_id = str(id)
    with open("getrdod.txt", "a+") as f:
       x = f.readlines()
       for a in x:
         if f"{chat_id}#{text}" in a:
           return False
       f.write(f"{chat_id}#{text}ZAIDRD{rd}\n")
    return True

'''
Programmed by : 🎖️ @DevZaid
   Channel -› • @Y88F8
'''
def del_rd(x):
   word = str(x).replace("\n","")
   with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
   with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if word != line:
              fp.write(line+"\n")
          return


'''
Programmed by : 🎖️ @DevZaid
   Channel -› • @Y88F8
'''
def del_rdod(id) -> bool:
    chat_id = str(id)
    gps = open("getrdod.txt").read()
    if chat_id not in gps:
      return False
    with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
    with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if chat_id not in line:
              fp.write(line+"\n")
          return

'''
Programmed by : 🎖️ @DevZaid
   Channel -› • @Y88F8
'''
def get_rdod(chat_id):
   with open("getrdod.txt", "r+") as f:
       lines = f.readlines()
   text = "• الردود بهذه المجموعة : \n"
   for line in lines:
     if str(chat_id) in line:
       a = line.split("#")[1]
       b = a.split("ZAIDRD")[0]
       text += f"{b}\n"
   if text == "• الردود بهذه المجموعة : \n": return False
   else: return f"**{text}**"
       
async def get_rtba(chat_id: int, user_id: int) -> bool:
    get = await rickthon.get_chat_member(chat_id, user_id)
    if not get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      return False
    else: return True
    

'''
Programmed by : 🎖️ @DevZaid
   Channel -› • @Y88F8
'''
@rickthon.on_message(filters.regex("^اضف رد$") & filters.group)
async def adf_rd(rickthon,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك")
    ask1 = await rickthon.ask(
    message.chat.id, "ارسل كلمة الرد", reply_to_message_id=message.id, filters=filters.text & filters.user(message.from_user.id))
    text = ask1.text
    ask2 = await rickthon.ask(
    message.chat.id, "ارسل جواب الرد", reply_to_message_id=ask1.id, filters=filters.user(message.from_user.id))
    copy = await ask2.copy(LOG)
    rd = copy.id
    a = add_rd(text, message.chat.id, rd)
    if a: return await ask2.reply("تم اضافة الرد بنجاح")
    else: return await ask2.reply("حدث خطأ")

'''
Programmed by : 🎖️ @DevZaid
   Channel -› • @Y88F8
'''
@rickthon.on_message(filters.regex("^مسح رد$") & filters.group)
async def delete_rd(rickthon,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   ask = await rickthon.ask(
     message.chat.id, "ارسل الرد الآن", filters=filters.text & filters.user(message.from_user.id), reply_to_message_id=message.id)
   a = get_rd(ask.text, message.chat.id)
   if not a:
     return await ask.reply("الرد غير موجود")
   x = f"{message.chat.id}#{ask.text}ZAIDRD{a}"
   b = del_rd(x)
   await ask.reply("• تم مسح الرد")
   

'''
Programmed by : 🎖️ @DevZaid
   Channel -› • @Y88F8
'''
@rickthon.on_message(filters.regex("^مسح الردود$") & filters.group)
async def delrdood(rickthon,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   a = del_rdod(message.chat.id)
   print(a)
   if not a : return await message.reply("• تم مسح الردود هنا")
   else: return await message.reply("• لاتوجد ردود هنا")


'''
Programmed by : 🎖️ @DevZaid
   Channel -› • @Y88F8
'''
@rickthon.on_message(filters.regex("^الردود$") & filters.group)
async def get_rdodd(rickthon,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك")
    a = get_rdod(message.chat.id)
    if not a: return await message.reply("• لا توجد ردود هنا")
    else: return await message.reply(a)

'''
Programmed by : 🎖️ @DevZaid
   Channel -› • @Y88F8
'''
@rickthon.on_message(filters.text & filters.group, group=2)
async def gettt_rd(rickthon, message):
   a = get_rd(message.text, message.chat.id)
   if a: return await rickthon.copy_message(message.chat.id, LOG, a, reply_to_message_id=message.id)
   else: return




@rickthon.on_message(filters.regex("^اقتباس$") & filters.group)
@rickthon.on_edited_message(filters.regex("^اقتباس$") & filters.group)
async def game_5(client, message):
   f = "quotes555v"
   t = message.chat.id
   d = randint(2,190)
   await rickthon.copy_message(
      t,
      f,
      d,
      reply_to_message_id=message.id,
      reply_markup=InlineKeyboardMarkup(
      [
      [
      InlineKeyboardButton("Dev", user_id= 5582470474)
      ]
      ]
      )
   )
   

@rickthon.on_message(filters.regex("^افتار انمي$") & filters.group)
@rickthon.on_edited_message(filters.regex("^افتار انمي$") & filters.group)
async def anime(c,m):
    rl = randint(3,201)
    url = f"https://t.me/foravaanime/{rl}"
    user = m.from_user.mention
    await m.reply_photo(url, caption=f"༄ {user}\n༄ تم اختيار افتار لك")     
    
@rickthon.on_message(filters.regex("^افتار ولد$") & filters.group)
@rickthon.on_edited_message(filters.regex("^افتار ولد$") & filters.group)
async def boys(c,m):
    rl = randint(3,446)
    url = f"https://t.me/foravaboys/{rl}"
    user = m.from_user.mention
    await m.reply_photo(url, caption=f"༄ {user}\n༄ تم اختيار افتار لك")  

@rickthon.on_callback_query(filters.regex("cut:"))
async def next_cut(_, query: CallbackQuery):
    id = int(query.data.split(":")[1])
    if not query.from_user.id == id:
      return await query.answer("هذا الأمر لايخصك", show_alert=True)
    else:
      idd = query.from_user.id
      r = randint(2, 141)
      a = await rickthon.get_messages("rancutt", r)
      await query.edit_message_text(
        f"- ‹ {query.from_user.mention} ›\n{a.text}",
        reply_markup=InlineKeyboardMarkup(
          [
          [
          InlineKeyboardButton("التالي", callback_data=f"cut:{idd}")
          ]
          ]
        )
      )
   

@rickthon.on_message(filters.regex("^قفل الشات$"))

async def lockchat(_, message):

    chat_id = message.chat.id

    await rickthon.set_chat_permissions(

    chat_id,

    ChatPermissions(

    can_send_messages=False,

    )

)

    await message.reply_text("ابشر يامُز قفلت الشات")



@rickthon.on_message(filters.regex("^فتح الشات$"))

async def openchat(_, message):

    chat_id = message.chat.id

    await rickthon.set_chat_permissions(

    chat_id,

    ChatPermissions(

    can_send_messages=True,

    can_send_media_messages=True,

    can_send_other_messages=True,

    )

)

    await message.reply_text("ابشر يامُز فتحت الشات")


@rickthon.on_message(filters.new_chat_members)

async def welcome(_,message):

	m = message.from_user.username

	now = datetime.now()

	now = (now.strftime('%I:%M'))

	await message.reply_text(f"""

	- يامرحبا ، نورتنا يا مُز 🤍 .

- معرفك : @{m} .

وقت الدخول : {now} .

""")


@rickthon.on_message(filters.regex("^تثبيت$") & filters.group)

async def pin(_,message):

        stas = (await rickthon.get_chat_member(message.chat.id, message.from_user.id)).status

        auth = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]

        if stas in auth:

        	await message.reply_to_message.pin(message.chat.id, message.from_user.id)

        	await message.reply_text("- تم تثبيت الرسالة")

        else:

            await message.reply("هذا الأمر يخص المشرفين بس .", quote=True)

        

@rickthon.on_message(filters.regex("^تك$") & filters.group)

async def pinn(_,message):

        stas = (await rickthon.get_chat_member(message.chat.id, message.from_user.id)).status

        auth = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]

        if stas in auth:

        	await rickthon.unpin_all_chat_messages(message.chat.id)

        if not message.reply_to_message:

        	return

        	await message.reply_text("- تم الغاء تثبيت جميع الرسائل المثبتة")

        else:

            await message.reply("هذا الأمر يخص المشرفين بس .", quote=True)

@rickthon.on_message(filters.regex("^اطردني$") & filters.group)
async def banrem(_,message):
  user = message.from_user.id
  await rickthon.ban_chat_member(message.chat.id,user)
  await message.reply_text("- تم طردك من المجموعة .")






@rickthon.on_message(filters.regex("^المشرفين$"))
async def adlist(_, message):
    chat_id = message.chat.id
    admin = "- قائمة المشرفين\n— — — — —\n"
    async for admins in rickthon.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
           admin+=f"› {'@'+admins.user.username if admins.user.username else admins.user.mention} - `{admins.user.id}` .\n"
    await message.reply(text=(admin))
    
@rickthon.on_message(filters.regex("^المحظورين$|^المحضورين$"))
async def banlist(_, message):
    chat_id = message.chat.id
    bb = "- قائمة المحظورين\n— — — — —\n"
    async for b in rickthon.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
           bb+=f"› {'@'+b.user.username if b.user.username else b.user.mention} - `{b.user.id}` .\n"
    await message.reply(text=(bb))
    
@rickthon.on_message(filters.regex("^المقيدين$|^المقيديين$"))
async def reslist(_, message):
    chat_id = message.chat.id
    bb = "- قائمة المقيدين\n— — — — —\n"
    async for b in rickthon.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RESTRICTED):
           bb+=f"› {'@'+b.user.username if b.user.username else b.user.mention} - `{b.user.id}` .\n"
    await message.reply(text=(bb))
    
@rickthon.on_message(filters.regex("^البوتات$"))
async def botslist(_, message):
    chat_id = message.chat.id
    bb = "- قائمة البوتات\n— — — — —\n"
    async for b in rickthon.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
           bb+=f"› {'@'+b.user.username if b.user.username else b.user.mention} - `{b.user.id}` .\n"
    await message.reply(text=(bb))
#Commands in *Tag .
@rickthon.on_message(filters.regex("^حظر .*$") & filters.group)
async def ban(_, message):
    User = re.match("حظر @(.*)", message.text).group(1)
    stas = (await rickthon.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth:
    	await message.chat.ban_member(User)
    	await message.reply_text("- تم حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
@rickthon.on_message(filters.regex("^الغاء حظر .*$") & filters.group)
async def unban(_, message):
    User = re.match("الغاء حظر @(.*)", message.text).group(1)
    stas = (await rickthon.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth:
    	await message.chat.unban_member(User)
    	await message.reply_text("- تم الغاء حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
#Commands in *reply .
@rickthon.on_message(filters.regex("^حظر$") & filters.group)
async def ban2(_, message):
    user =message.reply_to_message.from_user.id
    stas = (await rickthon.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth:
    	await rickthon.ban_chat_member(message.chat.id,user)
    	await message.reply_text("- تم حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
@rickthon.on_message(filters.regex("^الغاء حظر$") & filters.group)
async def ban3(_, message):
    user =message.reply_to_message.from_user.id
    stas = (await rickthon.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth:
    	await rickthon.unban_chat_member(message.chat.id,user)
    	await message.reply_text("- تم الغاء حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")

@rickthon.on_message(filters.regex("افتاره"))
async def her(_, message):
     user_id = message.reply_to_message.from_user.id
     d = await rickthon.get_chat(user_id)
     photo = await rickthon.download_media(d.photo.big_file_id)
     bio = d.bio
     if photo:
        await message.reply_photo(photo,caption=bio)
     else:
        await message.reply(bio)
        
@rickthon.on_message(filters.regex("افتاري"))
async def my(_, message):
     user_id = message.from_user.id
     b = await rickthon.get_chat(user_id)
     photo = await rickthon.download_media(b.photo.big_file_id)
     bio = b.bio
     if photo:
        await message.reply_photo(photo,caption=bio)
     else:
        await message.reply(bio)

@rickthon.on_message(filters.regex("^نبذتي$"))
async def Bio(_, message):
    if not message.reply_to_message:
     me = message.from_user.id
     b = await rickthon.get_chat(me)
     bio = b.bio
     await message.reply_text(bio)
	
@rickthon.on_message(filters.regex("^نبذته$"))
async def Bio(_, message):
	if message.reply_to_message:
		user_id = message.reply_to_message.from_user.id
		d = await rickthon.get_chat(user_id)
		bio = d.bio
		await message.reply_text(bio)

@rickthon.on_message(filters.regex("قول"))
async def echo(_, msg):
 text = msg.text.split(None, 1)[1]
 await msg.reply(text)

@rickthon.on_message(filters.command(["المطور",""],prefixes=f""))
def deve(dev,message):
	id = rickthon.get_chat("@a9aa99a")
	
	name = id.first_name
	Id = id.id
	user = id.username
	bio = id.bio
	A1 = InlineKeyboardMarkup([
        [ 
        InlineKeyboardButton(f"{name}",url=f"t.me/{user}")]])
	message.reply("""**𝐍𝐚𝐦𝐞 ➪ {}

𝐔𝐬𝐞𝐫 ➪ @{}

𝐈𝐝 ➪ {}

𝐁𝐢𝐨 ➪ {}**""".format(name,user,Id,bio),reply_markup=A1)
rickthon.run()
idle()
