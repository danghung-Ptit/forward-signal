from telethon import TelegramClient, events
api_id1 = 26860497
api_hash1 = '977d3200525322dcd121eb41e1059cfe'
api_id2 = 21047114
api_hash2 = 'd492ac1c69cd5019fab7251591865440'
api_id3=28206423
api_hash3 = '61a64a5d9e5dbedaba7c55b02b29c101'


# Tạo client
client1 = TelegramClient('AHung', api_id1, api_hash1)
client2 = TelegramClient('CTrangKem', api_id2, api_hash2)
client3 = TelegramClient('0xLouis', api_id3, api_hash3)

# Channel muốn forward tin nhắn từ đó
#-1001630951114:YRK TRADING PREMIUM
#-1001397467226:Rich Kids Margin
channel1 = -1001397467226
channel2 = -1001630951114

group_signal = {
    -1001686591807: "Drvkich Predictūm ( indictum )",
    -1001298366223: "Drvkich Wolves VIP",
    -1001150314411: "Drvkich Binance killers vip",
    -1001520813141: "Drvkich Fed® Russian Vip Channel",
    -1001197765997: "Drvkich Bullet vip Cornix 🐦",
    -1001563558761: "Drvkich Mega Crypto Vip",
    -1001196334161: "Yocrypto ( @cryptoleakss)",
    -1001210266512: "Drvkich Kim crypto",
    -1001663586985: "Alts signals",
    -1001429238571: "Drvkich Rose premium signal",
    -1001401152082: "Drvkich klondike vip",
    -1001157822084: "Drvkich CCC.io Crypto coins premium leaks",
    -1001415616482: "Drvkich trading crypto coach vip"
}

# Group muốn forward tin nhắn đến
destination_group = -856447389

# Function called when a new message is received on channel A
@client1.on(events.NewMessage(chats=channel1))
async def handler_A(event):
    message = event.message
    await message.forward_to(destination_group)

# Function called when a new message is received on channel B
@client2.on(events.NewMessage(chats=channel2))
async def handler_B(event):
    message = event.message
    await message.forward_to(destination_group)
    
@client3.on(events.NewMessage)
async def handler_C(event):
    chat_id = event.chat_id
    if chat_id in list(group_signal.keys()):
        message = event.message
        await message.forward_to(destination_group)

client1.start()
client2.start()
client3.start()

client1.run_until_disconnected()
client2.run_until_disconnected()
client3.run_until_disconnected()
