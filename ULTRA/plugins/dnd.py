# by madboy482 ... @Warning_MadBoy_is_Here
"""Syntax: .dnd REASON"""
import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types

from ULTRA import CMD_HELP
from ULTRA.utils import admin_cmd

global USER_DND  # pylint:disable=E0602
global dnd_time  # pylint:disable=E0602
global last_dnd_message  # pylint:disable=E0602
global dnd_start
global dnd_end
USER_DND = {}
dnd_time = None
last_dnd_message = {}
dnd_start = {}


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_dnd(event):
    global USER_DND  # pylint:disable=E0602
    global dnd_time  # pylint:disable=E0602
    global last_dnd_message  # pylint:disable=E0602
    global dnd_start
    global dnd_end
    back_alive = datetime.now()
    dnd_end = back_alive.replace(microsecond=0)
    if dnd_start != {}:
        total_dnd_time = str((dnd_end - dnd_start))
    current_message = event.message.message
    if ".dnd" not in current_message and "yes" in USER_DND:  # pylint:disable=E0602
        shite = await borg.send_message(
            event.chat_id,
                + "😶__Bᴀᴄᴋ Aʟɪᴠᴇ!__\n**Nᴏ ʟᴏɴɢᴇʀ AғK.**\n\n**Wᴀs AғK ғᴏʀ:** "
                + total_dnd_time
                + ".",
        )
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "#ᗩᖴKᖴᗩᒪՏᗴ \nSet dnd mode to False\n"
                + "😶__Bᴀᴄᴋ Aʟɪᴠᴇ!__\n**Nᴏ ʟᴏɴɢᴇʀ AғK.**\n\n**Wᴀs AғK ғᴏʀ:** "
                + total_dnd_time
                + ".",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PRIVATE_GROUP_BOT_API_ID` "
                + "for the proper functioning of dnd functionality "
                + "Ask In @UltraXchaT Chat grp to get help..\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        await asyncio.sleep(5)
        await shite.delete()
        USER_DND = {}  # pylint:disable=E0602
        dnd_time = None  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_dnd(event):
    if event.fwd_from:
        return
    global USER_DND  # pylint:disable=E0602
    global dnd_time  # pylint:disable=E0602
    global last_dnd_message  # pylint:disable=E0602
    global dnd_start
    global dnd_end
    back_alivee = datetime.now()
    dnd_end = back_alivee.replace(microsecond=0)
    if dnd_start != {}:
        total_dnd_time = str((dnd_end - dnd_start))
    current_message_text = event.message.message.lower()
    if "dnd" in current_message_text:
        # ULTRA's should not reply to other ULTRA's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_DND and not (await event.get_sender()).bot:  # pylint:disable=E0602
        #   if dnd_time:  # pylint:disable=E0602
        #      now = datetime.datetime.now()
        #     datime_since_dnd = now - dnd_time  # pylint:disable=E0602
        #    time = float(datime_since_dnd.seconds)
        #   days = time // (24 * 3600)
        #  time = time % (24 * 3600)
        # hours = time // 3600
        # time %= 3600
        #            minutes = time // 60
        #           time %= 60
        #          seconds = time
        #         if days == 1:
        #            dnd_since = "**Yesterday**"
        #       elif days > 1:
        #          if days > 6:
        #             date = now + \
        #                datetime.timedelta(
        #                   days=-days, hours=-hours, minutes=-minutes)
        #          dnd_since = date.strftime("%A, %Y %B %m, %H:%I")
        #     else:
        #        wday = now + datetime.timedelta(days=-days)
        #       dnd_since = wday.strftime('%A')
        #            elif hours > 1:
        #               dnd_since = f"`{int(hours)}h{int(minutes)}m` **ago**"
        #          elif minutes > 0:
        #             dnd_since = f"`{int(minutes)}m{int(seconds)}s` **ago**"
        #        else:
        #           dnd_since = f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = (
            f"**ᕼᗴY!! Mʏ Mᴀsᴛᴇʀ ɪs ᴄᴜʀʀᴇɴᴛʟʏ Oғғʟɪɴᴇ... Sɪɴᴄᴇ Wʜᴇɴ?**\n\n**Fᴏʀ** `{total_dnd_time}`\n"
            + f"\n\n__Hᴇ ʟᴇғᴛ ᴀ ʀᴇᴀsᴏɴ ʙᴛᴡ🧐__ :-\n{reason}"
            if reason
            else f"**ᕼᗴY!!**\n__I'ᴍ ᴄᴜʀʀᴇɴᴛʟʏ ᴜɴᴀᴠᴀɪʟᴀʙʟᴇ. Sɪɴᴄᴇ ᴡʜᴇɴ ʏᴏᴜ ᴀsᴋ?\n\nFᴏʀ `{total_dnd_time}` .__\n\nWʜᴇɴ I'ʟʟ ʙᴇ ʙᴀᴄᴋ? __Wʜᴇɴᴇᴠᴇʀ I ғᴇᴇʟ ʟɪᴋᴇ ᴄᴏᴍɪɴɢ ʙᴀᴄᴋ__🤧🚶🚶  "
        )
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_dnd_message:  # pylint:disable=E0602
            await last_dnd_message[event.chat_id].delete()  # pylint:disable=E0602
        last_dnd_message[event.chat_id] = msg  # pylint:disable=E0602


@borg.on(admin_cmd(pattern=r"dnd ?(.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    global USER_DND  # pylint:disable=E0602
    global dnd_time  # pylint:disable=E0602
    global last_dnd_message  # pylint:disable=E0602
    global dnd_start
    global dnd_end
    global reason
    USER_DND = {}
    dnd_time = None
    last_dnd_message = {}
    dnd_end = {}
    start_1 = datetime.now()
    dnd_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    if not USER_DND:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            dnd_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_DND = f"Yes: {reason}"  # pylint:disable=E0602
        if reason:
            await borg.send_message(
                event.chat_id, f"__**I sʜᴀʟʟ ʙᴇ ɢᴏɪɴɢ AғK Bᴇᴄᴜᴢ**__ ~ `{reason}`"
            )
        else:
            await borg.send_message(event.chat_id, f"**I'ᴍ ɢᴏɪɴɢ AғK!**")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                f"#ᗩᖴKTᖇᑌᗴ\nSet dnd mode to True.\nReason is `{reason}`",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


CMD_HELP.update(
    {
        "dnd": "__**PLUGIN NAME :** dnd__\
\n\n ** CMD ** `.dnd` [Optional Reason]\
\n**USAGE  :  **Sets you as afk.\nReplies to anyone who tags/PM's \
you telling them that you are afk(reason) and to not disturb you.\n\n__Switches off dnd when you type back anything, anywhere.__\
"
    }
)
