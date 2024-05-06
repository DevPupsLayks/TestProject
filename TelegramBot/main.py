import asyncio
from telegram import Bot

async def send_message():
    TOKEN = '7162762804:AAFpHcd57Ns6KjyEWnAwWTqsIM3eSLjsq9k'
    bot = Bot(TOKEN)
    chat_id = 797676862  # Numeric chat ID
    await bot.send_message(chat_id=chat_id, text='Hello World!')

asyncio.run(send_message())
