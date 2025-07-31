#This repo is developed by @aaru_2075, don't you fucking dare to remove credit. [Ask @aaru_2075 before reselling it]
#For Paid bot or support contact on @Manga_Campus_Chat

import os
import logging
from dotenv import load_dotenv
load_dotenv()
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN") or os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")


OWNER_ID = int(os.environ.get("OWNER_ID", "6180759790"))
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))    #DB channel

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))  #F-sub-1
# Secondary force-subscription channel (set 0 to disable)
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "")) #F-sub-2

REQUEST_CHANNEL_1 = int(os.environ.get("REQUEST_CHANNEL_1", ""))   #Req-sub-1

REQUEST_CHANNEL_2 = int(os.environ.get("REQUEST_CHANNEL_2", "")) #Req-sub-2



START_PIC = os.environ.get("START_PIC", "")
FORCE_PIC = os.environ.get("FORCE_PIC", "")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "")) # auto delete in seconds


PORT = os.environ.get("PORT", "8040")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6180759790]
    for x in (os.environ.get("ADMINS", "6180759790 5543390445").split()): #put admin ids like this 6180759790 6975428639 7827086839 [don't put any comma]
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")



CUSTOM_CAPTION = os.environ.get("", None) #<blockquote><b>𝗡𝗘𝗧𝗪𝗢𝗥𝗞: @The_Awakeners</b></blockquote>

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "<blockquote>❌𝗗𝗼𝗻'𝘁 𝘀𝗲𝗻𝗱 𝗺𝗲 𝗱𝗶𝗿𝗲𝗰𝘁 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗶𝗻 𝗱𝗺, 𝗱𝗼 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝗮 𝗱𝗲𝗮𝘁𝗵 𝘄𝗶𝘀𝗵?</blockquote>"

START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote><b><blockquote>Moshi Moshi Senpai {mention}</blockquote></b>\n<b>I'm Black Scythe a Filestore bot of @Anime_Mortals</b></blockquote>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ Sᴇɴᴘᴀɪ {mention}\n\n<b>Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟs Tᴏ Gᴇᴛ Fɪʟᴇs</b>")




ADMINS.append(OWNER_ID)
ADMINS.append(6180759790)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   #8104175594:AAE--rOpvYm00jmxIkBkUcFGd0Lk5z-wpG4

class Txt(object):
    about = f"""<b>😈 My Name :</b> <a href='https://t.me/Blackscythe_bot'>Black Scythe 😈</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>😈 Bot Made By :</b> @Aaru_2075"""

#This repo is developed by @aaru_2075, don't you fucking dare to remove credit. [Ask @aaru_2075 before reselling it]
#For Paid bot or support contact on @Manga_Campus_Chat
    
