from 𝙽𝚄𝙲𝙻𝙴𝙰𝚁 𝚇 𝚂𝙿𝙰𝙼 import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, SUDO_USERS
from 𝙽𝚄𝙲𝙻𝙴𝙰𝚁 𝚇 𝚂𝙿𝙰𝙼 import CMD_HNDLR as hl
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:
        mkl = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = mkl[0]
            Xd = int(bc)
            text = "Leaving....."
            event = await e.reply(text)
            try:
                await event.client(LeaveChannelRequest(Xd))
                await event.edit(" 𝗜 𝗔𝗺 𝗟𝗲𝗮𝘃𝗶𝗻𝗴 𝗧𝗵𝗶𝘀 𝗖𝗵𝗮𝘁 !! ✅")
            except Exception as e:
                await event.edit(str(e))
         
        else:
             bc = e.chat_id
             Xd = int(bc)
             text = "𝗜'𝗺 𝗟𝗲𝗮𝘃𝗶𝗻𝗴 𝗧𝗵𝗶𝘀 𝗚𝗿𝗼𝘂𝗽......"
             if e.is_private:
                  dik = f"You Can't Do This Here !! \n\n {hl}leave <Channel or Chat ID> \n {hl}leave : type in the group, bot will auto leave that group..!"
                  await e.reply(dik)
             else:
                  event = await e.reply(text)
                  try:
                      await event.client(LeaveChannelRequest(Xd))
                  except Exception as e:
                      await event.edit(str(e))
