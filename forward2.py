from telethon import TelegramClient, events
api_id1 = 26860497
api_hash1 = '977d3200525322dcd121eb41e1059cfe'
api_id2 = 21047114
api_hash2 = 'd492ac1c69cd5019fab7251591865440'
# Tạo client
client1 = TelegramClient('AHung', api_id1, api_hash1)
client2 = TelegramClient('CTrangKem', api_id2, api_hash2)

# Channel muốn forward tin nhắn từ đó
#-1001630951114:YRK TRADING PREMIUM
#-1001397467226:Rich Kids Margin
channel1 = -1001397467226
channel2 = -1001630951114


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

client1.start()
client2.start()

client1.run_until_disconnected()
client2.run_until_disconnected()
