import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Devine import LOGGER, app, userbot
from Devine.core.call import devine
from Devine.misc import sudo
from Devine.plugins import ALL_MODULES
from Devine.utils.database import get_banned_users, get_gbanned
from config import filter


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("assistant variables is empty")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            filter.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            filter.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Devine.plugins" + all_module)
    LOGGER("Devine.plugins").info("plugins loaded.")
    await userbot.start()
    await devine.start()
    try:
        await devine.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Devine").error(
            "trun on vc of log channel"
        )
        exit()
    except:
        pass
    await devine.decorators()
    LOGGER("Devine").info(
        "Powered by @hxh_network"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Devine").info("stopping bot....")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
