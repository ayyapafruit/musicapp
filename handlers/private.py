from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAx0CQ2C8OgACPTFhF8RphRAh0XC4OYaBee8ONWCrGAACGQ0AAuJm8UsXOff5HjA9DiAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [DONVIP](https://t.me/SENSIBLEGUY).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    
                  [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/ENGLISH_HINDI_CHATTINGG"
                    
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/MUSICPLAYER2022_BOT?startgroup=true"
                       
                ]    
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
               
            ]
        )
   )


