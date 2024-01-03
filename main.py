from config import Config
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# تعيين توكن البوت الخاص بك
TOKEN = Config.TG_BOT_TOKEN
# تعيين معرف القناة المصدر
SOURCE_CHANNEL = '@aeon'
# تعيين معرف القناة الهدف
TARGET_CHANNEL = '@PBOOB'

# تكوين السجل للحصول على سجل الأحداث
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

# وظيفة التعامل مع أمر /start
def start(update: Update, context):
    update.message.reply_text('مرحبًا! أنا بوت نقل المنشورات من قناة لأخرى.')

# وظيفة التعامل مع الرسائل النصية
def text_message(update: Update, context):
    # فقط نقل الرسالة إلى القناة الهدف
    context.bot.forward_message(chat_id=TARGET_CHANNEL,
                                from_chat_id=update.message.chat_id,
                                message_id=update.message.message_id)

# وظيفة التعامل مع الصور والفيديو والملفات
def media_message(update: Update, context):
    # فقط نقل الملف إلى القناة الهدف
    context.bot.forward_message(chat_id=TARGET_CHANNEL,
                                from_chat_id=update.message.chat_id,
                                message_id=update.message.message_id)

# وظيفة التشغيل الرئيسية
def main():
    # إعداد واجهة برمجة التطبيقات (API) للبوت
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # إضافة معالج الأوامر
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # إضافة معالج الرسائل النصية
    text_handler = MessageHandler(Filters.text & ~Filters.command, text_message)
    dispatcher.add_handler(text_handler)

    # إضافة معالج الرسائل المتعددة الوسائط
    media_handler = MessageHandler(Filters.photo | Filters.video | Filters.document, media_message)
    dispatcher.add_handler(media_handler)

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
