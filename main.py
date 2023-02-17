from FormatSignal import Signal
from get_token import getToken, BaseURL
from telethon import TelegramClient, events
from datetime import datetime
import yaml
import sys
import asyncio
import json
import telegram
import json
import requests
import time
import os

with open("./config/config.yml", "r") as ymlfile:
	cfg = yaml.load(ymlfile, Loader=yaml.SafeLoader)
	
api_id = cfg['telethon']['api_id']
api_hash = cfg['telethon']['api_hash']
TELEGRAM_CHAT_ID_Test_bot = cfg['telethon']['TELEGRAM_CHAT_ID_Test_bot']
TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal = cfg['telethon']['TELEGRAM_CHAT_ID_CryptoHawk-Bot-Forward_Signal']
TELEGRAM_CHAT_ID_The_Bull = cfg['telethon']['TELEGRAM_CHAT_ID_The_Bull']
TELEGRAM_CHAT_ID_Rose = cfg['telethon']['TELEGRAM_CHAT_ID_Rose']
TELEGRAM_CHAT_ID_coach = cfg['telethon']['TELEGRAM_CHAT_ID_coach']
TELEGRAM_CHAT_ID_klondike = cfg['telethon']['TELEGRAM_CHAT_ID_klondike']
#client = TelegramClient('hungdv', api_id, api_hash)

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
client = TelegramClient('0xLouis', api_id, api_hash)
@client.on(events.NewMessage)
async def handler(event):
	chat = await event.get_chat()
	chat_id = event.chat_id
	if chat_id == TELEGRAM_CHAT_ID_klondike:
		message = event.message
		#await message.forward_to(TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal)
		if "STOP LOSS".lower() in event.text.lower() and message != message_klondike:
			signal_klondike = Signal(event.text)
			signal_klondike.klondike_signal()
			createCr4Signal(signal_klondike)
			message_klondike = message
	elif chat_id == TELEGRAM_CHAT_ID_coach:
		message = event.message
		#await message.forward_to(TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal)
		if "STOP LOSS".lower() in event.text.lower():
			signal_coach = Signal(event.text)
			signal_coach.coach_signal()
			createCr4Signal(signal_coach)
	elif chat_id == TELEGRAM_CHAT_ID_The_Bull:
		message = event.message
		#await message.forward_to(TELEGRAM_CHAT_ID_CryptoHawk_Bot_Forward_Signal)
		if "STOP LOSS".lower() in event.text.lower():
			signal_theBull = Signal(event.text)
			signal_theBull.theBull_signal()
			createCr4Signal(signal_theBull)
			
client.start()
client.run_until_disconnected()

'''
@client.on(events.NewMessage(chats=TELEGRAM_CHAT_ID_Test_bot))
async def handler(event):
	if "🥎 Open".lower() in event.text.lower() or "🔑 Enter".lower() in event.text.lower():
		signal_klondike = Signal(event.text)
		signal_klondike.klondike_signal()
		createCr4Signal(signal_klondike)
		
	elif "Exchange :".lower() in event.text.lower():
		signal_coach = Signal(event.text)
		signal_coach.coach_signal()
		createCr4Signal(signal_coach)
	elif "BELOW".lower() in event.text.lower():
		signal_theBull = Signal(event.text)
		signal_theBull.theBull_signal()
		createCr4Signal(signal_theBull)
		
# Bắt đầu lắng nghe sự kiện
client.start()
client.run_until_disconnected()
'''


