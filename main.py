from config import Config
import logging
from telegram.ext import Updater, MessageHandler, Filters

# تكوين سجل السجلات (logs)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# تكوين توكن البوت الخاص بك
bot_token = Config.TG_BOT_TOKEN

# تكوين قناة الوجهة التي ترغب في نشر المنشورات فيها
destination_channel_id = '@aeo_n'

# دالة للتعامل مع المنشورات الواردة
def handle_post(update, context):
    message = update.effective_message
    chat_id = message.chat_id
    
    # التحقق من أن المنشور قادم من القناة المطلوبة
    if message.forward_from_chat and message.forward_from_chat.username == 'PBOOB':
        # إعادة نشر المنشور في القناة المقصودة
        message.forward(destination_channel_id)
    
    # تحديث حالة البوت بعد معالجة المنشور
    context.bot.send_message(chat_id=chat_id, text='تم نشر المنشور بنجاح!')

# تهيئة واجهة التحديث والتعامل مع المنشورات الواردة
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
post_handler = MessageHandler(Filters.text & (~Filters.command), handle_post)
dispatcher.add_handler(post_handler)

# بدء تشغيل البوت
updater.start_polling()
