import discord  # install 'discord.py-self', not 'discord'
from aiogram import Bot, Dispatcher, executor
import asyncio

discord_token = 'DISCORD_TOKEN'  # your discord account token
telegram_token = 'TELEGRAM_TOKEN'  # your telegram bot token

telegram_chat = 'TELEGRAM_CHAT_ID'  # there are bots on telegram to find out the id of the chat or channel

list_of_channels = {
    959554738804883536  # channel IDs that need to be forwarded, write yours!
}


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on!')

    async def on_message(self, message):
        if message.channel.id in list_of_channels:
            await bot.send_message(chat_id=telegram_chat, text=message.content)

    bot = Bot(token=telegram_token)
    dp = Dispatcher(bot)


bot = Bot(token=telegram_token)
client = MyClient()

# The cycle of two bots at the same time
loop = asyncio.get_event_loop()
task1 = loop.create_task(client.start(discord_token))
task2 = loop.create_task(executor.start_polling(client.dp, skip_updates=True))
gathered = asyncio.gather(task1, task2, loop=loop)
loop.run_until_complete(gathered)
