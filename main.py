from FormatSignal import Signal
from get_token import getToken, BaseURL
from telethon import TelegramClient, events
import yaml
import requests
import time
import os

with open("./config/config.yml", "r") as ymlfile:
	cfg = yaml.load(ymlfile, Loader=yaml.SafeLoader)
	
api_id = cfg['telethon']['api_id']
api_hash = cfg['telethon']['api_hash']
TELEGRAM_CHAT_ID_Test_bot = cfg['telethon']['TELEGRAM_CHAT_ID_Test_bot']
TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal = cfg['telethon']['TELEGRAM_CHAT_ID_CryptoHawk-Bot-Forward_Signal']
# TELEGRAM_CHAT_ID_The_Bull = cfg['telethon']['TELEGRAM_CHAT_ID_The_Bull']
# TELEGRAM_CHAT_ID_Rose = cfg['telethon']['TELEGRAM_CHAT_ID_Rose']
# TELEGRAM_CHAT_ID_coach = cfg['telethon']['TELEGRAM_CHAT_ID_coach']
TELEGRAM_CHAT_ID_klondike = cfg['telethon']['TELEGRAM_CHAT_ID_klondike']
TELEGRAM_CHAT_ID_Predictum = cfg['telethon']['TELEGRAM_CHAT_ID_Predictum']
TELEGRAM_CHAT_ID_killers = cfg['telethon']['TELEGRAM_CHAT_ID_killers']
TELEGRAM_CHAT_ID_Bullet = cfg['telethon']['TELEGRAM_CHAT_ID_Bullet']
TELEGRAM_CHAT_ID_Mega = cfg['telethon']['TELEGRAM_CHAT_ID_Mega']
TELEGRAM_CHAT_ID_Yocrypto = cfg['telethon']['TELEGRAM_CHAT_ID_Yocrypto']
TELEGRAM_CHAT_ID_Alts = cfg['telethon']['TELEGRAM_CHAT_ID_Alts']



def getChartURL(syombol):
	return ""
	url = "https://www.tradingview.com/chart/" + ChartToken + "/?symbol=" + syombol
	chrome_path = 'open -a /Applications/Safari.app %s'
	webbrowser.get(chrome_path).open(url)
	time.sleep(5)
	cmd = """
	osascript -e 'tell application "System Events" to keystroke "s" using {option down}'
	"""
	os.system(cmd)

	time.sleep(3)

	cmd = """
	osascript -e 'tell application "System Events" to keystroke "w" using {command down}'
	"""
	os.system(cmd)

	# get clipboard data
	pb = NSPasteboard.generalPasteboard()
	data = pb.stringForType_(NSStringPboardType)
	print(data)

	# This restores the same behavior as before.
	context = ssl._create_unverified_context()
	response = urllib.request.urlopen(url = data, context=context)
	html_response = response.read()
	encoding = response.headers.get_content_charset('utf-8')
	decoded_html = html_response.decode(encoding)
	soup = BS(decoded_html, 'lxml')
	for imgtag in soup.find_all('img'):
		return imgtag['src']


def createCr4Signal(signal):
	coinName = signal.symbol
	endpoint = BaseURL + "/api/v1/currency/search?keyword=" + coinName
	token = getToken()
	headers = {"Authorization": "Bearer " + token}
	response = requests.get(endpoint, headers=headers).json()
	data = response['data']
	coinData = {}
	for coin in data:
		if coin["shortName"] == coinName:
			id = coin["coinId"]
			name = coin["shortName"]
			icon = coin["logo"]
	signalTargets = [{"price": float(validTarget)} for validTarget in signal.targets]
	json_data = {"coin":{"id":id ,"name":name ,"pair": signal.currency , "icon": icon} ,"statistics":{"images":[getChartURL(signal.symbol)]} ,"entryPrice":float(signal.entries), "stopPrice":float(signal.stopLoss), "riskLevel":"MEDIUM", "multiple":1, "form":signal.form, "futureType":signal.futureType.upper(), "type":signal.signalMode, "targets":signalTargets, "leverage":str(signal.leverage), "source":signal.source, "status":signal.status}
	print(json_data)
	
	response = requests.post(BaseURL + '/api/v1/admin/signals', json=json_data, headers=headers).json()
	print(response)
	
message_klondike = ''
message_Predictum = ''
message_killers = ''
message_Bullet = ''
message_Mega = ''
message_Yocrypto = ''
message_Alts = ''
client = TelegramClient('0xLouis', api_id, api_hash)
#client = TelegramClient('hungdv', api_id, api_hash)
@client.on(events.NewMessage)
async def handler(event):
	global message_klondike, message_Predictum, message_killers, message_Bullet, message_Mega, message_Yocrypto, message_Alts
	chat_id = event.chat_id
	# if chat_id == TELEGRAM_CHAT_ID_Test_bot:
	# 	message = event.message
	# 	if "TARGET".lower() in message.text.lower():
	# 		print(message.text)

	if chat_id == TELEGRAM_CHAT_ID_klondike:
		message = event.message
		#await message.forward_to(TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal)
		if "TARGET".lower() in message.text.lower() and message != message_klondike:
			signal_klondike = Signal(event.text)
			signal_klondike.klondike_signal()
			if signal_klondike.check:
				createCr4Signal(signal_klondike)
				message_klondike = message

	elif chat_id == TELEGRAM_CHAT_ID_Predictum:
		message = event.message
		#await message.forward_to(TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal)
		if "TARGET".lower() in message.text.lower() and message != message_Predictum:
			signal_Predictum = Signal(event.text)
			signal_Predictum.predictum_signal()
			if signal_Predictum.check:
				createCr4Signal(signal_Predictum)
				message_Predictum = message

	elif chat_id == TELEGRAM_CHAT_ID_killers:
		message = event.message
		#await message.forward_to(TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal)
		if "TARGET".lower() in message.text.lower() and message != message_killers:
			signal_killers = Signal(event.text)
			signal_killers.killers_signal()
			if signal_killers.check:
				createCr4Signal(signal_killers)
				message_killers = message


	elif chat_id == TELEGRAM_CHAT_ID_Bullet:
		message = event.message
		#await message.forward_to(TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal)
		if "TARGET".lower() in message.text.lower() and message != message_Bullet:
			signal_Bullet = Signal(event.text)
			signal_Bullet.bullet_signal()
			if signal_Bullet.check:
				createCr4Signal(signal_Bullet)
				message_Bullet = message


	elif chat_id == TELEGRAM_CHAT_ID_Mega:
		message = event.message
		#await message.forward_to(TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal)
		if "TARGET".lower() in message.text.lower() and message != message_Mega:
			signal_Mega = Signal(event.text)
			signal_Mega.mega_signal()
			if signal_Mega.check:
				createCr4Signal(signal_Mega)
				message_Mega = message

	elif chat_id == TELEGRAM_CHAT_ID_Yocrypto:
		message = event.message
		#await message.forward_to(TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal)
		if "TARGET".lower() in message.text.lower() and message != message_Yocrypto:
			signal_Yocrypto = Signal(event.text)
			signal_Yocrypto.yocrypto_signal()
			if signal_Yocrypto.check:
				createCr4Signal(signal_Yocrypto)
				message_Yocrypto = message

	elif chat_id == TELEGRAM_CHAT_ID_Alts:
		message = event.message
		#await message.forward_to(TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal)
		if "TARGET".lower() in message.text.lower() and message != message_Alts:
			signal_Alts = Signal(event.text)
			signal_Alts.alts_signal()
			if signal_Alts.check:
				createCr4Signal(signal_Alts)
				message_Alts = message
			
client.start()
client.run_until_disconnected()




