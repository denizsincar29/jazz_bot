from ShazamAPI import Shazam
from random import randint
from datetime import datetime
import telebot,json
import jazz
conf=None
with open("bot.json",encoding="UTF-8") as f:conf=json.loads(f.read())
bot = telebot.TeleBot(conf["token"])

def words(ms,*args):
	for i in args:
		if not i in ms:return False
	return True

def randjazz():
	jz=jazz.a[randint(0,len(a))]
	return "we picked a jazz standard!\n"+jz[0]+"\ncategory: "+jz[1]+"\npriority: "+jz[2]

def shazamchik(msg):
	if msg.content_type=="text" and (msg.text=="cancel" or msg.text=="exit"):
		return
	elif msg.content_type=="voice":
		file_info = bot.get_file(message.voice.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		filename=getuser(message.from_user.id)+datetime.now().strftime("%B %d %Y, %H:%M:%S")
		with open(filename,"wb") as f:f.write(downloaded_file)
		shazam=Shazam


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	adminids=conf["admins"].values()
	admin=(message.from_user.id in adminids)
	if message.text.startswith("//") and not admin:
		bot.send_message(message.from_user.id, "sorry. you're not admin! probably you will be an admin in your next life! have a very nice day!")
		return
	if words(message.text,"random","jazz"):
		bot.send_message(message.from_user.id,randjazz())
	elif words(message.text,"shazam") or words(message.text,"what","song"):
		bot.register_next_step_handler(message,shazamchik)


@bot.message_handler(content_types=['voice'])
def get_voice_messages(message):
	file_info = bot.get_file(message.voice.file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	with open(getuser(message.from_user.id)+datetime.now().strftime("%B %d %Y, %H:%M:%S"),"wb") as f:f.write(downloaded_file)


bot.infinity_polling()
