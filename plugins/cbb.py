#This repo is developed by @aaru_2075, don't you fucking dare to remove credit. [Ask @aaru_2075 before reselling it]
#For Paid bot or support contact on @Manga_Campus_Chat

from pyrogram import __version__

import config
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""<b><blockquote expandable>╭───────────⍟
├➽ Oᴡɴᴇʀ : <a href='tg://user?id={6180759790}'>𝗚𝗣𝗚</a>
├➽ Aɴɪᴍᴇ Iɴᴅᴇx: <a href=https://t.me/Anime_Mortals>Aɴɪᴍᴇ Mᴏʀᴛᴀʟs</a> 
├➽ Fɪɴɪsʜᴇᴅ Aɴɪᴍᴇ: <a href=https://t.me/Anime_Awakeners>Aɴɪᴍᴇ Aᴡᴀᴋᴇɴᴇʀs</a> 
├➽ Oɴɢᴏɪɴɢ Aɴɪᴍᴇ: <a href=https://t.me/Ongoing_Mortals>Oɴɢᴏɪɴɢ Mᴏʀᴛᴀʟ</a> 
├➽ Mᴀɴʜᴡᴀ / Mᴀɴɢᴀ: <a href=https://t.me/Manhwa_Mortals>Mᴀɴʜᴡᴀ Mᴏʀᴛᴀʟs</a> 
├➽ Nᴇᴛᴡᴏʀᴋ: <a href=https://t.me/The_Awakeners>Tʜᴇ Aᴡᴀᴋᴇɴᴇʀs</a> 
├➽ Rᴇǫ/Cʜᴀᴛ: <a href=https://t.me/Mortals_Realm>Mᴏʀᴛᴀʟs Rᴇᴀʟᴍ</a>
╰───────────────⍟ </b></blockquote>
➽ Dᴇᴠᴇʟᴏᴩᴇʀ : <a href='tg://user?id={5543390445}'>Aaru</a>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝙲𝚕𝚘𝚜𝚎", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
