# COPYRIGHT (C) BY 2021 BY ULTRA X

from telethon import events, Button, custom
import os,re
from ULTRAX import ID
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"restart"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X = [[custom.Button.inline("🔥 RESTART 🔥",data="restart")]] #RESTART
 query = event.text #PROBOYX 
 result = LEGEND.article("LEGEND",text="RESTARTER",buttons=X,link_preview=False)
 await event.answer([result]) #LEGENDX

from telethon import Button, custom, events
import os, re, sys, asyncio
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'restart'))) # PROBOYX
async def restart(event):
  if event.sender_id == bot.me.id or event.sender_id == ID:
    await event.edit("Ya wait....Your Bot is being restarted...\nPlease Wait...")
    await asyncio.sleep(2)
    await event.edit("Restarting the Heroku connection.....")
    await asyncio.sleep(2)
    await event.edit("Yay!! Restarted your bot succesfully..\n✅✅")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()#OP
  else:
    pro = "ρℓєαѕє ∂єρℓσу уσυ σωη υℓтяα χ υѕєявσт"
    await event.answer(pro, alert=True)
