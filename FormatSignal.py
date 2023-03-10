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
        self.check = False
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




    def klondike_signal(sefl):
        text = sefl.signal
        sefl.source = 12

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



        # Get the future type
        if average_buy_price is not None and stop_loss is not None:
            if average_buy_price > stop_loss:
                futureType = "LONG"
            elif average_buy_price < stop_loss:
                futureType = "SHORT"
        else:
            futureType = None


        sefl.futureType = futureType
        sefl.symbol = coin
        sefl.currency = currency
        sefl.targets = targets
        sefl.stopLoss = stop_loss
        sefl.entries = average_buy_price

        if coin is not None and futureType is not None and targets is not None and stop_loss is not None and average_buy_price is not None:
            sefl.check = True
            print("True")

        print("klondike_signal")
        print("Coin:", coin)
        print("Currency:", currency)
        print("Targets:", targets)
        print("Stop Loss:", stop_loss)
        print("Average Buy Price:", average_buy_price)
        print(futureType)



    def predictum_signal(self):
        self.source = 9
        text = self.signal
        if 'spot' in text.lower():
            self.form = "SPOT"

         #Get the name of the coin

        coin_info = re.findall(r"\#(.*)/", text)
        if coin_info:
            coin = coin_info[0].strip().upper()
        else:
            coin = None
        # Get the currency
        currency_info = re.findall(r"\#.*\/(.*)", text)
        if currency_info:
            currency = currency_info[0].strip().upper()
        else:
            currency = None

        # Get the average buy price
        buy_price_info = re.search(r"Entry Point - (\d+.\d+)", text)
        if buy_price_info:
            average_buy_price = float(buy_price_info.group(1))
        else:
            average_buy_price = None

        # Get the targets
        targets_info = re.findall(r"Targets: ([\d+.\s-]+)", text)
        if targets_info:
            targets = [float(target) for target in targets_info[0].split("-")]
        else:
            targets = []

        # Get the stop loss
        stop_loss_info = re.findall(r"Stop Loss - (\d+.\d+)", text)
        if stop_loss_info:
            stop_loss = float(stop_loss_info[0])
        else:
            stop_loss = None

        # Get the future type
        if average_buy_price is not None and stop_loss is not None:
            if average_buy_price > stop_loss:
                futureType = "LONG"
            elif average_buy_price < stop_loss:
                futureType = "SHORT"
        else:
            futureType = None


        self.futureType = futureType
        self.symbol = coin
        self.currency = currency
        self.targets = targets
        self.stopLoss = stop_loss
        self.entries = average_buy_price

        if coin is not None and futureType is not None and targets is not None and stop_loss is not None and average_buy_price is not None:
            self.check = True
            print("True")

        print("predictum_signal")
        print("Coin:", coin)
        print("Currency:", currency)
        print("Targets:", targets)
        print("Stop Loss:", stop_loss)
        print("Average Buy Price:", average_buy_price)
        print(futureType)


    def yocrypto_signal(self):
        self.source = 10
        text = self.signal
        if 'spot' in text.lower():
            self.form = "SPOT"


        # Get the name of the coin
        coin_info = re.findall(r"\#(.*)\s", text)
        if coin_info:
            coin = coin_info[0].strip().upper()
            if coin.endswith("USDT") or coin.endswith("BUSD"):
                coin = coin[:-4]
        else:
            coin = None

         # Get the currency
        currency_info = re.findall(r"\#(.*)\s", text)
        if currency_info:
            currency = currency_info[0].strip().upper()[-4:]
        else:
            currency = None

        # Get the average buy price
        buy_price_info = re.findall(r"Entry: ([\d+.\-]+)", text)
        if buy_price_info:
            buy_prices = [float(price) for price in buy_price_info[0].split("-")]
            average_buy_price = sum(buy_prices) / len(buy_prices)
        else:
            average_buy_price = None

        # Get the targets
        targets_info = re.findall(r"Targets: ([\d+.\s-]+)", text)
        if targets_info:
            targets = [float(target) for target in targets_info[0].split("-")]
        else:
            targets = []

        # Get the stop loss
        stop_loss_info = re.findall(r"Stop-loss\s*-\s*([\d+.\-]+)", text)
        if stop_loss_info:
            stop_loss = float(stop_loss_info[0])
        else:
            stop_loss = None


        # Get the future type
        if average_buy_price is not None and stop_loss is not None:
            if average_buy_price > stop_loss:
                futureType = "LONG"
            elif average_buy_price < stop_loss:
                futureType = "SHORT"
        else:
            futureType = None


        self.futureType = futureType
        self.symbol = coin
        self.currency = currency
        self.targets = targets
        self.stopLoss = stop_loss
        self.entries = average_buy_price

        if coin is not None and futureType is not None and targets is not None and stop_loss is not None and average_buy_price is not None:
            self.check = True
            print("True")

        print("yocrypto_signal")
        print("Coin:", coin)
        print("Currency:", currency)
        print("Targets:", targets)
        print("Stop Loss:", stop_loss)
        print("Average Buy Price:", average_buy_price)
        print(futureType)


    def bullet_signal(self):
        self.source = 14
        text = self.signal
        if 'spot' in text.lower():
            self.form = "SPOT"

        # Get the coin name and direction
        coin_info = re.findall(r"COIN: \$?(.*)\/.*\nDirection:\s*(\w+)", text)
        if coin_info:
            coin, direction = coin_info[0]
            coin = coin.strip().upper()
        else:
            coin, direction = None, None

        currency_info = re.findall(r"\/([A-Za-z]+)", text)
        if currency_info:
            currency = currency_info[0].strip().upper()
        else:
            currency = None


        # Get the exchange
        exchange_info = re.findall(r"Exchange:\s*(.*)", text)
        if exchange_info:
            exchange = exchange_info[0].strip()
        else:
            exchange = None

        # Get the leverage
        leverage_info = re.findall(r"Leverage:\s*(.*)", text)
        if leverage_info:
            leverage = leverage_info[0].strip()
        else:
            leverage = None

        # Get the entry prices
        buy_price_info = re.findall(r"ENTRY:\s*([\d+.\s-]+)", text)
        if buy_price_info:
            buy_prices = [float(price) for price in buy_price_info[0].split("-")]
            average_buy_price = round(sum(buy_prices) / len(buy_prices), 5)
        else:
            average_buy_price = None

        # Get the targets
        targets_info = re.findall(r"TARGETS:\s*([\d+.\s-]+)", text)
        if targets_info:
            targets = [float(target) for target in targets_info[0].split("-")]
        else:
            targets = []

        # Get the stop loss
        stop_loss_info = re.findall(r"SL:\s*([\d+.]+)", text)
        if stop_loss_info:
            stop_loss = float(stop_loss_info[0])
        else:
            stop_loss = None

        # Get the future type
        if average_buy_price is not None and stop_loss is not None:
            if average_buy_price > stop_loss:
                futureType = "LONG"
            elif average_buy_price < stop_loss:
                futureType = "SHORT"
        else:
            futureType = None


        self.futureType = futureType
        self.symbol = coin
        self.currency = currency
        self.targets = targets
        self.stopLoss = stop_loss
        self.entries = average_buy_price

        if coin is not None and futureType is not None and targets is not None and stop_loss is not None and average_buy_price is not None:
            self.check = True
            print("True")

        print("bullet_signal")
        print("Coin:", coin)
        print("Currency:", currency)
        print("Targets:", targets)
        print("Stop Loss:", stop_loss)
        print("Average Buy Price:", average_buy_price)
        print(futureType)


    def mega_signal(self):
        text = self.signal

        self.source = 11
        text = self.signal
        if 'spot' in text.lower():
            self.form = "SPOT"

       # Tìm kiếm tên của đồng tiền
        coin_info = re.findall(r"\#?([\w\d]+)[/\s]+[\w\d]+\s", text)
        if coin_info:
            coin = coin_info[0].strip().upper()
        else:
            coin = None

        currency = re.search(r"/(\w+)\s", text).group(1)


       # Lấy danh sách các giá trị mục tiêu trong phần Entry Targets
        entry_targets = re.findall(r"Entry Targets:\n(?:\d+\)\s)?([\d\.]+)\n(?:\d+\)\s)?([\d\.]+)", text)
        if entry_targets:
            entry_targets = [float(x) for x in entry_targets[0]]
            average_buy_price = round(sum(entry_targets) / len(entry_targets), 5)
        else:
            average_buy_price = None

        # Lấy các giá trị trong phần Take-Profit Targets
        take_profit_targets = re.findall(r"Take-Profit Targets:\n([\d\.\)\s%-]+)", text)
        take_profit_targets = re.findall(r"([\d\.]+)\s*-", take_profit_targets[0])
        targets = [float(x) for x in take_profit_targets]

        # Lấy các giá trị trong phần Stop Targets
        stop_targets = re.findall(r"Stop Targets:\n\d\)\s*([\d\.]+)", text)
        stop_loss = [float(x) for x in stop_targets][0]

         # Get the future type
        if average_buy_price is not None and stop_loss is not None:
            if average_buy_price > stop_loss:
                futureType = "LONG"
            elif average_buy_price < stop_loss:
                futureType = "SHORT"
        else:
            futureType = None


        self.futureType = futureType
        self.symbol = coin
        self.currency = currency
        self.targets = targets
        self.stopLoss = stop_loss
        self.entries = average_buy_price

        if coin is not None and futureType is not None and targets is not None and stop_loss is not None and average_buy_price is not None:
            self.check = True
            print("True")
        print("mega_signal")
        print("Coin:", coin)
        print("Currency:", currency)
        print("Targets:", targets)
        print("Stop Loss:", stop_loss)
        print("Average Buy Price:", average_buy_price)
        print(futureType)


    def killers_signal(self):
        self.source = 13
        text = self.signal
        if 'spot' in text.lower():
            self.form = "SPOT"


        # Get the name of the coin
        coin_info = re.findall(r"\$([a-zA-Z]+)/[a-zA-Z]+", text)
        if coin_info:
            coin = coin_info[0].strip().upper()
        else:
            coin = None

        # Get the currency
        currency_info = re.findall(r"/([a-zA-Z]+)", text)
        if currency_info:
            currency = currency_info[0].strip().upper()
        else:
            currency = None

        # Get the direction
        direction_info = re.findall(r"Direction: ([a-zA-Z]+)", text)
        if direction_info:
            direction = direction_info[0].strip().upper()
        else:
            direction = None

        # Get the entry prices
        entry_price_info = re.findall(r"ENTRY: ([\d+.\-\s]+)", text)
        if entry_price_info:
            entry_prices = [float(price) for price in entry_price_info[0].split("-")]
            average_buy_price = round(sum(entry_prices) / len(entry_prices), 5)
        else:
            average_buy_price = []

        # Get the targets
        targets_info = re.findall(r"TARGETS: ([\d+.\s-]+)", text)
        if targets_info:
            targets = [float(target) for target in targets_info[0].split("-")]
        else:
            targets = []

        # Get the stop loss
        stop_loss_info = re.findall(r"STOP LOSS: ([\d+.\-]+)", text)
        if stop_loss_info:
            stop_loss = float(stop_loss_info[0])
        else:
            stop_loss = None




        # Get the future type
        if average_buy_price is not None and stop_loss is not None:
            if average_buy_price > stop_loss:
                futureType = "LONG"
            elif average_buy_price < stop_loss:
                futureType = "SHORT"
        else:
            futureType = None


        self.futureType = futureType
        self.symbol = coin
        self.currency = currency
        self.targets = targets
        self.stopLoss = stop_loss
        self.entries = average_buy_price

        if coin is not None and futureType is not None and targets is not None and stop_loss is not None and average_buy_price is not None:
            self.check = True
            print("True")
        print("killers_signal")
        print("Coin:", coin)
        print("Currency:", currency)
        print("Targets:", targets)
        print("Stop Loss:", stop_loss)
        print("Average Buy Price:", average_buy_price)
        print(futureType)

    def alts_signal(self):
        self.source = 15
        text = self.signal
        if 'spot' in text.lower():
            self.form = "SPOT"

        # Get the name of the coin
        coin_info = re.findall(r"\bCoin:\s*([\w/]+)\s*", text)
        if coin_info:
            coin = coin_info[0].strip().split("/")[0].upper()
        else:
            coin = None

        # Get the currency
        currency_info = re.findall(r"/(\w+)\s", text)
        if currency_info:
            currency = currency_info[0].upper()
        else:
            currency = None

        # Get the average buy price
        buy_price_info = re.findall(r"Entry:\s*([\d.\s-]+)", text)
        if buy_price_info:
            buy_prices = [float(price) for price in buy_price_info[0].split("-")]
            average_buy_price = sum(buy_prices) / len(buy_prices)
        else:
            average_buy_price = None

        # Get the targets
        targets_info = re.findall(r"Target:\s*([\d.\s-]+)", text)
        if targets_info:
            targets = [float(target) for target in targets_info[0].split("-")]
        else:
            targets = []

        # Get the stop loss
        stop_loss_info = re.findall(r"Stoploss:\s*([\d.\-]+)", text)
        if stop_loss_info:
            stop_loss = float(stop_loss_info[0])
        else:
            stop_loss = None



        # Get the future type
        if average_buy_price is not None and stop_loss is not None:
            if average_buy_price > stop_loss:
                futureType = "LONG"
            elif average_buy_price < stop_loss:
                futureType = "SHORT"
        else:
            futureType = None


        self.futureType = futureType
        self.symbol = coin
        self.currency = currency
        self.targets = targets
        self.stopLoss = stop_loss
        self.entries = average_buy_price

        if coin is not None and futureType is not None and targets is not None and stop_loss is not None and average_buy_price is not None:
            self.check = True
            print("True")

        print("alts_signal")
        print("Coin:", coin)
        print("Currency:", currency)
        print("Targets:", targets)
        print("Stop Loss:", stop_loss)
        print("Average Buy Price:", average_buy_price)
        print(futureType)



    def gg_signal(self):
        text = self.signal

        self.source = 17
        text = self.signal
        if 'spot' in text.lower():
            self.form = "SPOT"

       # Tìm kiếm tên của đồng tiền
        coin_info = re.findall(r"\#?([\w\d]+)[/\s]+[\w\d]+\s", text)
        if coin_info:
            coin = coin_info[0].strip().upper()
        else:
            coin = None
            print("No coin name information found.")

        currency = coin
        if currency:
            if "USD" in currency:
                currency = "USDT"
            elif "BUS" in currency:
                currency = "BUSD"
        else:
            currency = None

        coin = coin.replace(currency, "")



       # Lấy danh sách các giá trị mục tiêu trong phần Entry Targets
        buy_price_info = re.findall(r"Entry Zone:\s*([\d.\s-]+)", text)
        if buy_price_info:
            buy_prices = [float(price) for price in buy_price_info[0].split("-")]
            average_buy_price = sum(buy_prices) / len(buy_prices)
        else:
            average_buy_price = None

        # Lấy các giá trị trong phần Take-Profit Targets
        target_info = re.findall(r"Target \d+:\s*([\d.]+)", text)
        if target_info:
            targets = [float(target) for target in target_info]
        else:
            target_info = re.findall(r"Target(\d+)\s*:?\s*([\d\.]+)", gg)
            if target_info:
                targets = [float(target[1]) for target in target_info]
            else:
                targets = []


        # Lấy các giá trị trong phần Stop Targets
        stop_loss_info = re.findall(r"Stop-Loss:\s*([\d.]+)", text)
        if stop_loss_info:
            stop_loss = float(stop_loss_info[0])
        else:
            stop_loss = None

         # Get the future type
        if average_buy_price is not None and stop_loss is not None:
            if average_buy_price > stop_loss:
                futureType = "LONG"
            elif average_buy_price < stop_loss:
                futureType = "SHORT"
        else:
            futureType = None


        self.futureType = futureType
        self.symbol = coin
        self.currency = currency
        self.targets = targets
        self.stopLoss = stop_loss
        self.entries = average_buy_price
        self.leverage = 20

        if coin is not None and futureType is not None and targets is not None and stop_loss is not None and average_buy_price is not None:
            self.check = True
            print("True")
        print("gg_signal")
        print("Coin:", coin)
        print("Currency:", currency)
        print("Targets:", targets)
        print("Stop Loss:", stop_loss)
        print("Average Buy Price:", average_buy_price)
        print(futureType)




klondike = """
#SIGNAL (BTC/USD)

🥎 Open SHORT for the price between $22022- $22147 with 1% of your deposit with cross leverage.

🍒 Targets:

1) Close the position at the price $21971
2) Close the position at the price $21949
3) Close the position at the price $21916
4) Close the position at the price $21861
5) Close the position at the price $21795
6) Close the position at the price $21706
7) Close the position at the price $21596

❌ STOP LOSS: $22257
"""


#
# signal = Signal(klondike)
# signal.klondike_signal()
# print("-----------------------------")
#
#
# predictum = """
# Breakout ( Sell ) #AGIX/USDT
#
# Entry Point - 3970
#
# Targets: 3954 - 3938 - 3922 - 3890 - 3810
#
# Leverage - 10x
#
# Stop Loss - 4210
# """
#
#
#
# signal = Signal(predictum)
# signal.predictum_signal()
# print("-----------------------------")
#



yocrypto = """
Long #THETAUSDT 

Bybit USDT, Binance

Entry: 1.24-1.258

LEVERAGE: 2x

Targets: 1.40-1.50-1.60-1.80-2.04

Stop-loss - 1.1225
"""


# signal = Signal(yocrypto)
# signal.yocrypto_signal()
# print("-----------------------------")



bullet = """
COIN: $DOGE/USDT
Direction: Long
Exchange: Binance Futures
Leverage: 3x

ENTRY: 0.0695 - 0.0785 - 0.0872

TARGETS: 0.0895 - 0.092 - 0.095 - 0.098 - 0.102 - 0.106 - 0.111 - 0.116 - 0.122 - 0.129 - 0.137 - 0.150 - 0.165 - 0.190 - 0.235 - 0.300

SL: 0.063
➖➖➖➖➖
Bitcoin Bullets® Trading
"""


# signal = Signal(bullet)
# signal.bullet_signal()
# print("-----------------------------")

mega = """
⚡⚡ #BNB/USDT ⚡⚡
Exchanges: ByBit USDT, Binance Futures
Signal Type: Regular (Long)
Leverage: Cross (5.0X)

Entry Targets:
1) 287
2) 285

Take-Profit Targets:
1) 288.5 - 25.0%
2) 291 - 25.0%
3) 294 - 25.0%
4) 299 - 25.0%

Stop Targets:
1) 283

Trailing Configuration:
Stop: Moving 2 Target -
  Trigger: Target (2)
"""


# signal = Signal(mega)
# signal.mega_signal()
# print("-----------------------------")


killers = """
SPOT

COIN: $XTZ/USDT
Direction: SHORT

ENTRY: 1.18 - 1.207 - 1.235

TARGETS: 1.17 - 1.16 - 1.145 - 1.13 - 1.11 - 1.08 - 1.03 - 0.95 - 0.87 - 0.78

STOP LOSS: 1.29
"""


# signal = Signal(killers)
# signal.killers_signal()
# print("-----------------------------")


alts = """
Coin: DYDX/USDT LONG
LEVERAGE:2x
Entry: 2.403 - 2.911
Target: 2.990 - 3.116 - 3.673 - 4.2
Stoploss: 2.264
"""

#
# signal = Signal(alts)
# signal.alts_signal()
# print("-----------------------------")


#
# gg = """📩 #LTCUSDT 30m | Mid-Term
# 📈 Short Entry Zone:91-93
# 🎯Accuracy of this strategy - 82.00%
#
#
# - ⏳ -  Signal details:
#
#
#
# Target1 :90.636
# Target2 : 90.09
# Target3 : 89.544
# Target4 : 88.816
# Target5:87.36
# Target6:77.532
# _____
# Leverage : 20x
# ❌Stop-Loss: 102.486
# 💡After reaching the first target you can put the rest of the position to breakeven"""
#
#
# signal = Signal(gg)
# signal.gg_signal()
# print("-----------------------------")
#




'''
source 9: Wolves -> Predictum
source 10: Ozel -> Yocrypto
source 11: The bull -> Mega
source 12: klondike
source 13: coach -> Killers
source 14: Rose -> Bullet
source 15: Alts
source 17: gg
'''