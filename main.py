from telethon import TelegramClient, sync

# брать с сайта телеграмма https://my.telegram.org/auth
api_id = ''
api_hash = ''
client = TelegramClient('mirror', api_id, api_hash)

client.start()

#id чата из которого надо скачать аватарки
participants = client.get_participants(-1111111111111, aggressive=False)
for p in participants:
    client.download_profile_photo(p.id)
