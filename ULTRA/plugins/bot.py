
# make by @LEGENDX22
# inline alive
# modify by proboy22
import asyncio
import os
from LEGENDX import BOT, PHOTO, VERSION, ALIVE_USERNAME, ALIVE_BOT_USERNAME
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom
from ULTRA.utils import admin_cmd
from ULTRA import ALIVE_NAME
from ULTRA import bot as ultra
from telethon import Button, custom
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = ultra.uid
from ULTRA.utils import admin_cmd
from PIL import Image
import requests
from io import BytesIO
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"
ALIVE_PHOTTO = PHOTO

pro_text=(f"**{BOT} ιѕ ση ƒιяє**\n\n🔥 αвσυт му ѕуѕтєм 🔥\n\n➥ **Tᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** : 1.19.5\n➥ **Sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** : [UʟᴛʀᴀX Sᴜᴘᴘᴏʀᴛ](https://t.me/UltraXOT)\n➥ **Lɪᴄᴇɴꜱᴇ** : [UʟᴛʀᴀX](https://github.com/ULTRA-OP)\n➥ **Cᴏᴘʏʀɪɢʜᴛ ʙʏ** : [UʟᴛʀᴀX Usᴇʀʙᴏᴛ](https://github.com/ULTRA-OP/ULTRA-X)\n\n➥ **Mʏ ᴍᴀsᴛᴇʀ** : [{DEFAULTUSER}](tg://user?id={ok})\n")
TG_BOT_USER_NAME_BF_HER = os.environ.get("ALIVE_PHOTTO", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await ultra.get_me()
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Rᴇᴘᴏ", "https://github.com/ULTRA-OP/ULTRA-X"),
                    Button.url("Dᴇᴘʟᴏʏ", "https://heroku.com/deploy?template=https://github.com/ULTRA-OP/ULTRA-X/blob/master")],
                    [Button.url("Sᴛʀɪɴɢ", "https://repl.it/ULTRA-OP/ULTRA-X#main.py"),
                    Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/ULTRAXOT")
                ]
                    [Button.url("Master", "https://t.me/{ALIVE_USERNAME})
                    Button.url("Assistant", "https://t.me/{ALIVE_BOT_USERNAME})  
                ]
            ]
            buttons += [[custom.Button.inline("Hᴇʟᴘ", data="helpme"), custom.Button.inline("Rᴇsᴛᴀʀᴛ", data='restart')]]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="υℓтяα χ",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="υℓтяα χ",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)



from ULTRA import bot 


@bot.on(admin_cmd(outgoing=True, pattern="alive"))
async def repo(event):
    if event.fwd_from:
        return
    ULTRAX = Var.TG_BOT_USER_NAME_BF_HER
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(ULTRAX, "alive")
    await response[0].click(event.chat_id)
    await event.delete()
