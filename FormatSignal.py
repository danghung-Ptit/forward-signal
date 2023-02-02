import requests
import re

class Signal:
    # constructor
    def __init__(self, signal):
        self.signal = signal
        self.is_valid = True
        self.entry = 0
        self.entries = []
        self.targets = []
        self.currency = ""
        self.stopLoss = ""
        self.symbol = ''
        self.leverage = 10
        self.multiple = "1"
        self.isBinance = True
        self.form = "FUTURE"
        self.futureType = ""
        self.futureTypeIcon = ""
        self.source = None
        self.status = 3 #1 open, 2 close 3 setup
        self.signalId = ""
        self.signalMode = "SCALP"
    def get_symbol(self):
        return self.symbol

    def get_entry(self):
        return self.entries

    def get_stop_loss(self):
        return self.stopLoss

    def get_targets(self):
        return self.targets

    # translates class attributes into json format.
    def to_json(self):
        signal_json = {}
        signal_json['symbol'] = self.symbol
        signal_json['entry'] = self.entries
        signal_json['targets'] = self.targets
        signal_json['stop_loss'] = self.stop_loss
        return signal_json

    def canCreate(self):
        return len(self.symbol) > 0 and len(self.entries) > 0 and len(self.stopLoss) > 0 and len(self.targets) > 0 and self.isBinance == True and self.form == "future"
    def canClose(self):
        return self.isBinance == True



    def woles_signal(self):
        filtered_signal = self.signal
        sefl.source = 9
        otherExchanges = ["ftx", "coinbase", "kucoin", "kraken", "bitfinex", "huobi", "bybit"]

        if "binance" not in filtered_signal.lower():
            for exchange in otherExchanges:
                if exchange in filtered_signal:
                    self.isBinance = False

        self.targets = re.findall(r"TARGET \d+ : (\d+)", filtered_signal)
        self.stopLoss = re.findall(r"STOP LOSS : (\d+)", filtered_signal)[0].strip()
        self.leverage = re.findall(r"LEVERAGE:\s+(\d+)", filtered_signal)[0].strip()
        self.symbol, self.currency = re.findall(r"#(\w+)/(\w+)", filtered_signal)[0]
        self.futureType = re.findall(r"#(\w+)", filtered_signal)[1].upper()

        buy_price_range = re.findall(r"BUY :([\d\$\-]+)\$", filtered_signal)[0].strip()
        buy_prices = [int(price.strip().split("$")[0]) for price in buy_price_range.split("-")]
        self.entries = sum(buy_prices) / len(buy_prices)
        
        
    def klondike_signal(sefl):
        text = sefl.signal
        sefl.source = 12
        otherExchanges = ["ftx", "coinbase", "kucoin", "kraken", "bitfinex", "huobi", "bybit"]
        
        if "binance" not in text.lower():
            for exchange in otherExchanges:
                if exchange in text:
                    self.isBinance = False
                    
            
        
        # Get the name of the coin
        coin_info = re.findall(r"\((.*)\)", text)
        if coin_info:
            coin = coin_info[0].split("/")[0].strip().upper()
        else:
            coin = None
            
        # Get the currency
        currency_info = re.findall(r"\((.*)\)", text)
        if currency_info:
            currency = coin_info[0].split("/")[1].strip().upper()
            if "US" in currency:
                currency = "USDT"
            elif "BU" in currency:
                currency = "BUSD"
        else:
            currency = None
            
        # Get the targets
        targets_info = re.findall("the price \$([\d\.]+)", text)
        if targets_info:
            targets = [float(target) for target in targets_info]
        else:
            targets = []
            
        # Get the stop loss
        stop_loss_info = re.search("STOP LOSS: \$([\d\.]+)", text)
        if stop_loss_info is not None:
            stop_loss = float(stop_loss_info.group(1))
        else:
            stop_loss = None
            
        # Get the average buy price
        
            
        # Get the average buy price
        buy_price_range = re.findall(r"price between \$([\d]+)\- \$([\d.]+)", text)
        if buy_price_range:
            buy_prices = [int(price) for price in buy_price_range[0]]
            average_buy_price = sum(buy_prices) / len(buy_prices)
        else:
            entry = re.search("price between \$([\d\.]+) - \$([\d\.]+)", text)
            if entry is not None:
                average_buy_price = (float(entry.group(1)) + float(entry.group(2))) / 2
            else:
                average_buy_price = None
        # Print the results
        print("Coin:", coin)
        print("Currency:", currency)
        print("Targets:", targets)
        print("Stop Loss:", stop_loss)
        print("Average Buy Price:", average_buy_price)
        
        #Get the futureType
    
        if average_buy_price > stop_loss:
            sefl.futureType = "LONG"
        elif average_buy_price < stop_loss:
            sefl.futureType = "SHORT"
        sefl.symbol = coin
        sefl.currency = currency
        sefl.targets = targets
        sefl.stopLoss = stop_loss
        sefl.entries = average_buy_price
        
        
        
    def coach_signal(sefl):
        text = sefl.signal
        sefl.source = 13
        
        otherExchanges = ["ftx", "coinbase", "kucoin", "kraken", "bitfinex", "huobi", "bybit"]
        
        if "binance" not in text.lower():
            for exchange in otherExchanges:
                if exchange in text:
                    self.isBinance = False
                    
        #Get the name of the coin
        
        coin_info = re.findall(r"#(\w+)", text)
        if coin_info:
            coin = coin_info[0].strip().upper()
        else:
            coin = None
            
        #Get the buy price
            
        buy_price_info = re.findall(r"Buy : (\d+.\d+)", text)
        if buy_price_info:
            buy_price = float(buy_price_info[0])
        else:
            buy_price_info = re.findall(r"Entry : (\d+.\d+)", text)
            if buy_price_info:
                buy_price = float(buy_price_info[0])
            else:
                buy_price = None
            
        #Get the targets
            
        targets_info = re.findall(r"Targets : (\d+.\d+)", text)
        if targets_info:
            targets = [float(price) for price in targets_info]
        else:
            targets = []
            
        #Get the stop loss
            
        stop_loss_info = re.findall(r"Stop Loss : (\d+.\d+)", text)
        if stop_loss_info:
            stop_loss = float(stop_loss_info[0])
        else:
            stop_loss = None
            
        #Get the exchange
            
        exchange_info = re.findall(r"Exchange : #(\w+)", text)
        if exchange_info:
            exchange = exchange_info[0].strip().lower()
        else:
            exchange = None
            
        #Get the futureType
            
        if buy_price > stop_loss:
            sefl.futureType = "LONG"
            sefl.form = "SPOT"
        elif buy_price < stop_loss:
            sefl.futureType = "SHORT"
            sefl.form = "FUTURE"
        
        print("Coin:", coin)
        print("Buy price:", buy_price)
        print("Targets:", targets)
        print("Stop loss:", stop_loss)
        print("Exchange:", exchange)
        
        #Get the futureType
        
        if buy_price > stop_loss:
            sefl.futureType = "LONG"
        elif buy_price < stop_loss:
            sefl.futureType = "SHORT"
        sefl.symbol = coin
        sefl.currency = "USDT"
        sefl.targets = targets
        sefl.stopLoss = stop_loss
        sefl.entries = buy_price
        
        
    def theBull_signal(sefl):
        text = sefl.signal
        sefl.source = 11
        otherExchanges = ["ftx", "coinbase", "kucoin", "kraken", "bitfinex", "huobi", "bybit"]
        
        if "binance" not in text.lower():
            for exchange in otherExchanges:
                if exchange in text:
                    self.isBinance = False
                    
                    
        #Get the name of the coin
                    
        coin_info = re.findall(r"([A-Z]+)/", text)
        if coin_info:
            coin = coin_info[0].strip().upper()
        else:
            coin = None
            
        #Get the currency
            
        currency_info = re.findall(r"/([A-Z]+)\s", text)
        if currency_info:
            currency = currency_info[0].strip().upper()
        else:
            currency = None
            
        #Get the targets
            
        targets_info = re.findall(r"\s(\d+.\d+)", text)
        if targets_info:
            targets = [float(price) for price in targets_info]
        else:
            targets = []
            
        #Get the stop loss
            
        stop_loss_info = re.findall(r"BELOW (\d+.\d+)", text)
        if stop_loss_info:
            stop_loss = float(stop_loss_info[0])
        else:
            stop_loss = None
            
        #Get the average buy price
        entry = re.search("ENTRY\s+([\d\.]+)\s+-\s+([\d\.]+)", text)
        if entry:
            average_buy_price = (float(entry.group(1)) + float(entry.group(2))) / 2
        else:
            average_buy_price = None
            
        #Get the futureType
        if average_buy_price:
            if average_buy_price > stop_loss:
                sefl.futureType = "LONG"
            elif average_buy_price < stop_loss:
                sefl.futureType = "SHORT"
            
        print("Coin:", coin)
        print("Currency:", currency)
        print("Targets:", targets)
        print("Stop Loss:", stop_loss)
        print("Average Buy Price:", average_buy_price)
        
        
        #Get the futureType
        
        if average_buy_price > stop_loss:
            sefl.futureType = "LONG"
        elif average_buy_price < stop_loss:
            sefl.futureType = "SHORT"
        sefl.symbol = coin
        sefl.currency = currency
        sefl.targets = targets
        sefl.stopLoss = stop_loss
        sefl.entries = average_buy_price




        

klondike = """#SIGNAL (BTC/USD)

🥎 Open LONG for the price between $22786- $22917 with 1% of your deposit with cross leverage.

🍒 Targets:

1) Close the position at the price $2296.9
2) Close the position at the price $22992
3) Close the position at the price $23026
4) Close the position at the price $23083
5) Close the position at the price $23152
6) Close the position at the price $23243
7) Close the position at the price $23358

❌ STOP LOSS: $22671"""


klondike2 = """
#SIGNAL (APT/USDT) 

📛 Risk of the signal: 8/10 

🔑 Enter SHORT at price between $16.9 - $17.5 with 10x leverage on Binance Futures

🉐 Targets:

1️⃣ Close the order at the price $158
2️⃣ Close the order at the price $15.1
3️⃣ Close the order at the price $14.3
4️⃣ Close the order at the price $13.1
5️⃣ Close the order at the price $12.2

❗️STOP LOSS: $181
"""


#signal_klondike = Signal(klondike)
#signal_klondike.klondike_signal()
#print("-----------------------------")

coach = """#RIF

Buy : 0.0521 $

Targets : 0.0539 - 0.0570 - 0.0600 -

0.0630 - 0.0680 $

Stop Loss : 0.0500 $

Exchange : #Binance"""

#signal_coach = Signal(coach)
#signal_coach.coach_signal()
#print("-----------------------------")

theBull = """CHR/USDT

ENTRY 0.1580 - 0.1590

TARGETS 0.1777 - 0.1937 - 0.2052 - 0.2317 - 0.2531 - 0.2745 - 0.3050 - 0.3438

STOP LOSS ON DAILY CLOSE BELOW 0.1375"""

#signal_theBull = Signal(theBull)
#signal_theBull.theBull_signal()

'''
-1001284332848:Drvkich The bull exclusive
-1001429238571:Drvkich Rose premium signal
-1001401152082:Drvkich klondike vip
-1001157822084:Drvkich CCC.io Crypto coins premium leaks
-1001415616482:Drvkich trading crypto coach vip

source 9: Wolves
source 10: Ozel
source 11: The bull
source 12: klondike
source 13: coach
source 14: Rose
'''