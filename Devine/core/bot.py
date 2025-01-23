
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from ..logging import LOGGER


class Devine(Client):
    def __init__(self):
        LOGGER(__name__).info("Devine Music Starting...")
        super().__init__(
            name="Devine",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = f"{self.me.first_name} {(self.me.last_name or '')}"
        self.username = self.me.username
        self.mention = self.me.mention

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ᴄʀᴇᴀᴛᴏʀ", user_id=config.OWNER_ID)
            ],
            [
                InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url="https://t.me/hxh_network"),
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/zenitsu_bot_support"),
            ]
        ])

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<b>{self.mention} ɪs ᴀʟɪᴠᴇ <a href='https://i.ibb.co/XFyfNRC/photo-2024-12-14-04-11-48-7448115436119392264.jpg' target='_blank'>✨</a></b>\n\n"
                         f"<b>• ʙᴏᴛ ᴠᴇʀsɪᴏɴ :</b> <code>𝟸.𝟷 ʀx</code>\n"
                         f"<b>• ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :</b> <code>𝟹.𝟷𝟶.𝟷𝟷</code>\n"
                         f"<b>• ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :</b> <code>𝟸.𝟶.𝟷𝟶𝟼</code>"
                ),
                reply_markup=keyboard
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log channel. Make sure that you have added your bot to your log group/channel."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason: {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            exit()
        LOGGER(__name__).info(f"Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
