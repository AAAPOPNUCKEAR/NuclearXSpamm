from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from .. import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, ALIVE_PIC, OWNER_ID
from SemxXSpam.plugins.help import *


MIG_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/91d82bf74b7a75468f5ef.jpg"

Ryan_Button = [
        [
        Button.url("✨ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ✨", "https://t.me/NucLeaR_xD")
        ],
        [
        Button.inline("⚡ 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 ⚡", data="help_back")
        ]
        ]
               
RyanX_Button = [
        [
        Button.url("✨ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ✨", "https://t.me/NucLeaR_xD"),
        Button.url("✨ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ✨", "https://t.me/AUKAATMEINRAHO")
        ],
        [
        Button.url("🔥 𝗥𝗘𝗣𝗢 🔥", "https://github.com/ERR0rMK/SEMXxBOTFATHER")
        ]
        ]
        
        
#USERS 


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RyanBot = await event.client.get_me()
       bot_name = RyanBot.first_name
       bot_id = RyanBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRyan = event.chat_id
       firstname = replied_user.user.first_name
       userid = replied_user.user.id
       ownermsg = f"**Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\n Click Below Buttons For Help. 🌚**"
       usermsg = f"**Hello !! [{firstname}](tg://user?id={userid})\nNice To Meet You, Well I Am [{bot_name}](tg://user?id={bot_id}), A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From The Button Given Below.** \n\n**Powered By : [𝙎𝙚𝙢𝙭𝙓𝙎𝙥𝙖𝙢](https://t.me/rudra_hun_vaii)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheRyan,
                  MIG_IMG,
                  caption=ownermsg, 
                  buttons=Ryan_Button)
       else:
            await event.client.send_file(TheRyan,
                  MIG_IMG,
                  caption=usermsg, 
                  buttons=RyanX_Button)
                

