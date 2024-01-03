from config import Config
from pyrogram import Client, filters

app = Client('my_acount',
	     api_id=Config.APP_ID,
	     api_hash=Config.API_HASH,)

"""***---******---******---******---******---******---******---******---******---******---***"""

id = 6549245259
ch = -1001198143769
yes = ["no"]
"""***---******---******---******---******---******---******---******---******---******---***"""
#هنا اوامر التفعيل والتعطيل#
"""***---******---******---******---******---******---******---******---******---******---***"""
@app.on_message(filters.command(["تعطيل","عطل"],prefixes=f""))
async def yas(yess,message):
	if "no" in yes:
		await app.send_message(message.chat.id,"معطل")
	else:
		yes[0] = "no"
		await app.send_message(message.chat.id,"تم التعطيل")
@app.on_message(filters.command(["تفعيل","فعل"],prefixes=f""))
async def No(NO,message):
	if "yes" in yes:
		await app.send_message(message.chat.id,"مفعل")
	else:
		yes[0] = "yes"
		await app.send_message(message.chat.id,"تم التفعيل")
"""***---******---******---******---******---******---******---******---******---******---***"""	#هنا اخذ المنشورات#
"""***---******---******---******---******---******---******---******---******---******---***"""	
@app.on_message(filters.chat(int(ch)) & filters.all)
async def handle_messages(client, message):
	if "yes" in yes:
		if message.text:
			if "@aeo_n" in message.text:
				msg =message.text.replace("@aeo_n","@iqrels")
				ci = await app.get_chat(message.chat.id)
				msg = message.text
				title = ci.title
				username = ci.username
				await app.send_message(id,f"""رسالة جديدة من قناة : {title}
يوزر القناة : @{username}
الرسالة : {msg}""")
			else:
				ci = await app.get_chat(message.chat.id)
				msg = message.text
				title = ci.title
				username = ci.username
				await app.send_message(id,f"""رسالة جديدة من قناة : {title}
يوزر القناة : @{username}
الرسالة : {msg}""")
		if message.video:
			if "@aeo_n" in message.caption:
				msg = message.caption.replace("@aeo_n","@iqrels")
				file = message.video.file_id
				await app.send_video(id,video=message.video.file_id,caption=msg)
			else:
				file = message.video.file_id
				await app.send_video(id,video=file,caption=msg)
		if message.photo:
			if "@aeo_n" in message.caption:
				msg = message.caption.replace("@aeo_n","@iqrels")
				file = message.photo.file_id
				await app.send_photo(id,photo=file,caption=msg)
			else:
				msg = message.caption
				file = message.photo.file_id
				await app.send_photo(id,photo=file,caption=msg)
"""***---******---******---******---******---******---******---******---******---******---***"""	
print("run the bot")
app.run()
