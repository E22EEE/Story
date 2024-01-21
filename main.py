from config import Config

from telebot import (TeleBot,types)
from random import (choice,randint)
from names import get_first_name,get_full_name,get_last_name
from gzip import decompress
from time import sleep
from os import path,system
import websocket,concurrent.futures,ssl,json


ppp88 = TeleBot("6449900091:AAEA64nljWvoIQyCC_O4N-dxVbquuP9_iPE")

@ppp88.message_handler(commands=['start'])
def Start(message):
    
    control = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( Start )',callback_data='StartSafum'))
    control.add(types.InlineKeyboardButton('( Devloper )',url='zeezzz.t.me'),types.InlineKeyboardButton('( Channel )',url='uciuu.t.me'))
    control.add(types.InlineKeyboardButton('( Bot InstruCtions )',callback_data='help'))
    ppp88.reply_to(message,f'''
↯︙Hi ( {message.chat.first_name} ) .
↯︙I Can Create Infinite s Accounts .
''',reply_markup=control)

@ppp88.callback_query_handler(func=lambda call:True)
def CallingButtons(call):
    executor=concurrent.futures.ThreadPoolExecutor(max_workers=90)
    if call.data=='StartSafum':
        with open('StartSafum.txt','a') as a:
            pass
        d = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('[ Loading .. ]',callback_data='h'))
        d.add(types.InlineKeyboardButton('( 🔺 Stop 🔺 )',callback_data='Stop'))
        ppp88.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='↯︙Plz , Wait ...\n↯︙Creating Account ...',reply_markup=d);sleep(2)
        
        
        def StartSafum(call):
            
                
                Created,Failed,Error=0,0,0
                user=str(choice([get_first_name().lower(),get_full_name().replace(' ','').lower(),get_last_name().lower()]))+str(''.join(choice('1234567790') for ppp88 in range(int(randint(2,3)))))+str(choice('qwertyuioplkjhgfdsazxcvbnm')[0])+str(''.join(choice('qwertyuioplkjhgfdsazxcvbnm1234567890') for i in range(int(randint(6,13)))))
                headers = {"app": "com.safeum.android",
            	    "host": None,
            	    "remoteIp": "51.79.208.190",
            	    "remotePort": str(8080),
            	    "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195","time": "2023-04-30 12:13:32",
            	    "url": "wss://51.79.208.190/Auth"}
                data0={"action":"Register","subaction":"Desktop","locale":"en_GB","gmt":"+02","password":{"m1x":"503c73d12b354f86ff9706b2114704380876f59f1444133e62ca27b5ee8127cc","m1y":"6387ae32b7087257452ae27fc8a925ddd6ba31d955639838249c02b3de175dfc","m2":"219d1d9b049550f26a6c7b7914a44da1b5c931eff8692dbfe3127eeb1a922fcf","iv":"e38cb9e83aef6ceb60a7a71493317903","message":"0d99759f972c527722a18a74b3e0b3c6060fe1be3ad53581a7692ff67b7bb651a18cde40552972d6d0b1482e119abde6203f5ab4985940da19bb998bb73f523806ed67cc6c9dbd310fd59fedee420f32"},"magicword":{"m1x":"04eb364e4ef79f31f3e95df2a956e9c72ddc7b8ed4bf965f4cea42739dbe8a4a","m1y":"ef1608faa151cb7989b0ba7f57b39822d7b282511a77c4d7a33afe8165bdc1ab","m2":"4b4d1468bfaf01a82c574ea71c44052d3ecb7c2866a2ced102d0a1a55901c94b","iv":"b31d0165dde6b3d204263d6ea4b96789","message":"8c6ec7ce0b9108d882bb076be6e49fe2"},"magicwordhint":"0000","login":str(user),"devicename":"Xiaomi Redmi Note 8 Pro","softwareversion":"1.1.0.1380","nickname":"hvtctchnjvfxfx","os":"AND","deviceuid":"c72d110c1ae40d50","devicepushuid":"*dxT6B6Solm0:APA91bHqL8wxzlyKHckKxMDz66HmUqmxCPAVKBDrs8KcxCAjwdpxIPTCfRmeEw8Jks_q13vOSFsOVjCVhb-CkkKmTUsaiS7YOYHQS_pbH1g6P4N-jlnRzySQwGvqMP1gxRVksHiOXKKP","osversion":"and_11.0.0","id":"1734805704"}
                if path.exists('StartSafum.txt') == True: 
                    ws=websocket.create_connection("wss://51.79.208.190/Auth", header=headers, sslopt={"cert_reqs": ssl.CERT_NONE})
                    ws.send(json.dumps(data0))
                    result=ws.recv()
                    decoded_data = decompress(result)
                    
                    if '"comment":"Exists"' in str(decoded_data):
                        
                        Failed+=1
                        
                    elif '"status":"Success"' in str(decoded_data):
                        
                        ppp88.send_message(call.message.chat.id,f'{user}')
                        Created+=1
                                         
                    else:
                        
                        Error+=1             
                    
        while 1:
            for i in range(10):
                if path.exists('StartSafum.txt') == False:
                    ppp88.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
↯︙Bot has been Stoped 🔺 
↯︙I will Send Accounts ..
''',reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( Back )',callback_data='Back')))
                    executor.shutdown(wait=True)
                    system('rm -rf StartSafum.txt')
                    
                    break
                    
                else:
                        
                        executor.submit(StartSafum,call)    
    elif call.data == 'Back':
        control = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( Start )',callback_data='StartSafum'))
        control.add(types.InlineKeyboardButton('( Devloper )',url='zeezzz.t.me'),types.InlineKeyboardButton('( Channel )',url='uciuu.t.me'))
        control.add(types.InlineKeyboardButton('( Bot InstruCtions )',callback_data='help'))
        ppp88.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
↯︙Hi ( {call.message.chat.first_name} ) .
↯︙I Can Create Infinite s Accounts .
''',reply_markup=control)
            
    elif call.data == 'help':
        ppp88.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''

''',reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('( Link App )',url='https://play.google.com/store/apps/details?id=com.azacodes.dubaivpn'),types.InlineKeyboardButton('( Back )',callback_data='Back')))
                        
    elif call.data == 'Stop':
            system('rm -rf StartSafum.txt')
            

ppp88.infinity_polling()
