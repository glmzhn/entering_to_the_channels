from pyrogram import Client
import asyncio
import os
import random

filepath = os.path.abspath(__file__)
channels = filepath.replace('\\main.py', '\\channels')
proxy_dir = filepath.replace("\\main.py", "\\proxy")
sessions_dir = os.path.join(os.path.dirname(filepath), 'sessions')

with open(f'{proxy_dir}/' + 'proxy.txt', 'r') as fl:
    proxy_list = fl.read().split('\n')

with open(f'{channels}/' + 'channels.txt', 'r') as fl:
    channels_list = fl.readlines()

cur_proxy = random.choice(proxy_list)

sessions = []

for files in os.listdir(sessions_dir):
    if files.endswith(".session"):
        files = files.split('.')
        sessions.append(files[0])

app = Client(sessions[0], workdir=sessions_dir)


async def join_channels():
    for channel_url in channels_list:
        try:
            chat = await app.join_chat(channel_url)
            print(f"Succesfully entered to the channel: {chat.title}")
        except Exception as e:
            print(f"Got an error while entering to the channel: {channel_url}")
            print(e)
            continue

        await asyncio.sleep(30)

if __name__ == "__main__":
    app.start()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(join_channels())
    app.stop()
