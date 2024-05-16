import logging
import sqlite3

from aiogram import *
from aiogram.types import *
from aiogram.exceptions import *
from aiogram.filters import *

from datetime import datetime

rootList = [] # enter here your telegram id
botToken = '' # enter here your bot token
codename = 'hotspring' # project's codename, don't keep in mind about that
version = '0.1' # current core verison

# everything to keep bot polling stable and correct
logger = logging.getLogger(__name__)
bot = Bot(token=botToken, parse_mode="HTML")
dp = Dispatcher()
StartTime = datetime.now()
aioVersion = __version__

# not done yet but WIP
def isIgnoring(msg: Message):
        with sqlite3.connect("config.db") as UserDB:
            UserBDCursor = UserDB.cursor()
            if UserBDCursor.execute("SELECT chatid FROM ignorechat WHERE chatid = ?", (msg.chat.id,)).fetchone() == None and UserBDCursor.execute("SELECT userid FROM ignoreuser WHERE userid = ?", (msg.from_user.id,)).fetchone() == None:
                return True

# method of starting bot
def main():
    with sqlite3.connect("config.db") as config:
        cfgdb = config.cursor()
        cfgdb.execute("""CREATE TABLE IF NOT EXISTS main(chatid INTEGER, ship TEXT, lang TEXT)""")
        cfgdb.execute("""CREATE TABLE IF NOT EXISTS shiplist(chatid INTEGER, userid INTEGER, username TEXT)""")
        cfgdb.execute("""CREATE TABLE IF NOT EXISTS ignoreuser(userid INTEGER)""")
        cfgdb.execute("""CREATE TABLE IF NOT EXISTS ignorechat(chatid INTEGER)""")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp.run_polling(bot, allowed_updates=dp.resolve_used_update_types())


# useful methods for your chatbots
class mt:
        async def isUserAnAdmin(msg = None):
            user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
            if user.status in ["administrator", "creator"]:
                return True


        async def isUserRoot(msg = None):
            if msg.from_user.id in rootList:
                return True
            

        async def isBotPromoted(msg = None):
            botStatus = await bot.get_chat_member(msg.chat.id, bot.id)
            print(botStatus.status)
            if botStatus.status in ["administrator", "creator"]:
                return True  


        def isdbActive(msg = None):
            pass # WIP


        def isPrivate(msg = None):
            if msg.chat.type == 'private':
                return True


        def isBotActive(msg = None):
            pass # WIP


        def rootLock(msg = None):
            pass # WIP