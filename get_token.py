
import requests
import json


# Prod
#TELEGRAM_BOT_TOKEN = "5733025778:AAHT67_fnrH5ZR4VQ1k22_3FhmdPQGmkjdU"
#TELEGRAM_CHAT_ID = '-1001831725991'
#BaseURL = "https://api.coinr4.com"
#Email = "admin@gmail.com"
#Password = "123456aA@"
#AnonId = "fOISj31S9kaNvOahpKMol12q0wx2"
#ChartToken = "twz9VSjX"


# Dev
BaseURL = "https://test-api.coinr4.com"
Email = "admin@gmail.com"
Password = "123456Aa@"
AnonId = "JDcwPjLCk5egpORnGgcFpHEDeHS2"
ChartToken = "sZ6ZWleN"



def getToken():
	url = BaseURL + "/api/v1/auth/login"

	payload = json.dumps({
	  "email": Email,
	  "password": Password,
	  "anonId": AnonId
	})
	headers = {
	  'accept': 'application/json, text/plain, */*',
	  'content-type': 'application/json'
	}

	print(BaseURL)

	response = requests.request("POST", url, headers=headers, data=payload)
	print(response)
	data = response.json()
	data = data['data']
	return data["accessToken"]

