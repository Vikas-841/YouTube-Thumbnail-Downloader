# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
import requests
from pyrogram import Client, filters


Bot = Client(
    "YouTube-Thumbnail-Downloader",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@Bot.on_message(filters.private & filters.text)
async def send_thumbnail(bot, update):
    if ("youtube.com" in update.text) and ("/" in update.text) and ("=" in update.text):
        id = update.text.split("=", -1)[1]
    elif ("youtu.be" in update.text) and ("/" in update.text):
        id = update.text.split("/", -1)[1]
    else:
        id = update.text
    try:
        thumbnail = "https://i.ytimg.com/vi/" + id + "maxresdefault.jpg"
        await update.reply_photo(thumbnail)
    except Exception as error:
        await update.reply_text(error)

Bot.run()
