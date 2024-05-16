import pythonping
import platform

from corelib.core import *

from aiogram import *
from aiogram.types import *
from aiogram.exceptions import *
from aiogram.filters import *

# write ur code here

@dp.message(Command(commands=['example']))
async def exampleCommand(msg: Message):
    await msg.reply(f"Hello {msg.from_user.full_name}! This is an example command!")


@dp.message(Command(commands=["status"]))
async def status(msg: Message) -> None:
    if await mt.isUserRoot(msg):
        await msg.reply(
            f"Core build:<code> {version}</code>" +
            f"\nCodename:<code> {codename}</code>" +
            f"\nUptime:<code> {str(datetime.now() - StartTime)}</code>" +
            f"\nChat id:<code> {str(msg.chat.id)}</code>" +
            f"\nUser id:<code> {str(msg.from_user.id)}</code>" +
            f"\nTelegram latency:<code> {str(pythonping.ping('api.telegram.org').rtt_avg_ms)}</code>" +
            f"\nLanguage:<code> Python {platform.python_version()}</code>" +
            f"\nLib:<code> aiogram {aioVersion}</code>" +
            f"\nRunning system:<code> {platform.system()} {platform.release()}</code>" +
            f"\n@byterunners, 2024")

        
if __name__ == '__main__': # DO NOT DELETE OR BOT WONT START
    main()