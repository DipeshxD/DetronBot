import platform
import sys
from telethon import version
from userbot import (HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HELP, BOTLOG, BOTLOG_CHATID, DetronBot_NAME, ALIVE_NAME, YOUR_SHORT_NAME)
from userbot.events import DetronBot, rekcah05 
import os
DetronBot = os.environ.get("ALIVE_PIC","https://telegra.ph/file/ecb54ca5afd9c647424a6.mp4")

import asyncio
from telethon import events
import heroku3
FULL_SUDO = os.environ.get("FULL_SUDO", None)
from var import Var
rksu = Var.SUDO_USERS
from datetime import datetime
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, DetronBot_NAME, DetronBot_MSG, ORI_MSG, ALIVE_S_MESSAGE, ALIVE_E_MESSAGE, ALIVE_S_MSG, ALIVE_E_MSG
client2 = client3 = None
try:
  from userbot import bot, client2 , client3
except:
	pass

SPAM_PROTECT = os.environ.get("SPAM_PROTECT", None)
DetronBot_NNAME = str(DetronBot_NAME) if DetronBot_NAME else str(DetronBot_MSG)
ALIVE_S_MMSG = str(ALIVE_S_MESSAGE) if ALIVE_S_MESSAGE else str(ALIVE_S_MSG)
ALIVE_E_MMSG = str(ALIVE_E_MESSAGE) if ALIVE_E_MESSAGE else str(ALIVE_E_MSG)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else YOUR_SHORT_NAME
START_TIME = datetime.now()
client = bot
S2_NAME = os.environ.get("S2_NAME", DetronBot_NNAME)
S3_NAME = os.environ.get("S3_NAME", DetronBot_NNAME)
S2_USER = os.environ.get("S2_USER", DEFAULTUSER)
S3_USER = os.environ.get("S3_USER", DEFAULTUSER)

v = "2.0.0"

if rksu:
 if FULL_SUDO:
    sudork = 'Full access'
 else:
    sudork = 'Normal access'
else:
	sudork = 'NotSet'


if SPAM_PROTECT:
	ss = "True"
else:
	ss = "False"

try:
   Heroku = heroku3.from_key(HEROKU_API_KEY)                         
   app = Heroku.app(HEROKU_APP_NAME)
   herokurk = 'connected'
except:
	herokurk = '[Failed to connect](https://telegra.ph/RkPavi-06-09-6)'
	pass


if BOTLOG_CHATID:
	logrk = 'connected'
else:
	logrk = '[Failed to connect](https://telegra.ph/RkPavi-06-09-3)'


@client.on(events.NewMessage(outgoing=True, pattern='!DetronBot'))
async def alive(alive):
    text=(""
                    f"**{ALIVE_S_MMSG}**\n\n"                     
                    f" °  `{DetronBot_NNAME}`: **{v}**\n"
                    f" °  `User:` ** {DEFAULTUSER} **\n"
                    f" °  `Telethon`: ** {version.__version__} **\n"
                    f" °  `Python` : ** {platform.python_version()} **\n"                                                                                     
                    f" °  `Os:` ** Kali GNU/Linux Rolling x86_64   **\n"                                       
                    f" °  `Heroku:` ** {herokurk} **\n"
                    f" °  `LogChat:` ** {logrk} **\n"
                    f" °  `Sudo:` ** {sudork} **\n"           
                    f" °  `SpamProtect:` ** {ss} **\n"       
                    f" °  `Uptime:` ** {str(datetime.now() - START_TIME).split('.')[0]} **\n\n"                                   
                    f"**{ALIVE_E_MMSG}**")
    await alive.client.send_file(alive.chat_id, shivam,caption=text, force_document=False)
    await alive.delete()
if client2:
 @client2.on(events.NewMessage(outgoing=True, pattern='!DetronBot'))
 async def alive(alive):
    text=(""
                    f"**{ALIVE_S_MMSG}**\n\n"                     
                    f" °  `{S2_NAME}`: **{v}**\n"
                    f" °  `User:` ** {S2_USER} **\n"
                    f" °  `Telethon`: ** {version.__version__} **\n"
                    f" °  `Python` : ** {platform.python_version()} **\n"                                                                                     
                    f" °  `Os:` ** Kali GNU/Linux Rolling x86_64   **\n"                                       
                    f" °  `Heroku:` ** {herokurk} **\n"
                    f" °  `LogChat:` ** {logrk} **\n"
                    f" °  `Sudo:` ** {sudork} **\n"           
                    f" °  `SpamProtect:` ** {ss} **\n"       
                    f" °  `Uptime:` ** {str(datetime.now() - START_TIME).split('.')[0]} **\n\n"                                   
                    f"**{ALIVE_E_MMSG}**")
    await alive.client.send_file(alive.chat_id, shivam,caption=text, force_document=False)
    await alive.delete()
if client3:
 @client3.on(events.NewMessage(outgoing=True, pattern='!DetronBot'))
 async def alive(alive):
    text=(""
                    f"**{ALIVE_S_MMSG}**\n\n"                     
                    f" °  `{S3_NAME}`: **{v}**\n"
                    f" °  `User:` ** {S3_USER} **\n"
                    f" °  `Telethon`: ** {version.__version__} **\n"
                    f" °  `Python` : ** {platform.python_version()} **\n"                                                                                     
                    f" °  `Os:` ** Kali GNU/Linux Rolling x86_64   **\n"                                       
                    f" °  `Heroku:` ** {herokurk} **\n"
                    f" °  `LogChat:` ** {logrk} **\n"
                    f" °  `Sudo:` ** {sudork} **\n"           
                    f" °  `SpamProtect:` ** {ss} **\n"       
                    f" °  `Uptime:` ** {str(datetime.now() - START_TIME).split('.')[0]} **\n\n"                                   
                    f"**{ALIVE_E_MMSG}**")
    await alive.client.send_file(alive.chat_id, shivam,caption=text, force_document=False)
    await alive.delete()

@DetronBot05(outgoing=True, pattern="^\.alive$")
@DetronBot05(outgoing=True, pattern="^\!alive$")
async def alive(alive):
    text=("Iam On type` !DetronBot `or` !help `for more info....")
    await alive.client.send_file(alive.chat_id, shivam,caption=text, force_document=False)
    await alive.delete()





@bot.on(rekcah05(pattern=f"sudo$", allow_sudo=True))
@bot.on(rekcah05(pattern=f"DetronBot$", allow_sudo=True))
async def alive(alive):
    text=(""
                    f"**{ALIVE_S_MMSG}**\n\n"                     
                    f" °  `{DetronBot_NNAME}`: **{v}**\n"
                    f" °  `Sudo Id:` ** {rksu} **\n"
                    f" °  `Telethon`: ** {version.__version__} **\n"
                    f" °  `Python` : ** {platform.python_version()} **\n"                                                                                     
                    f" °  `Os:` ** Kali GNU/Linux Rolling x86_64   **\n"                                       
                    f" °  `Heroku:` ** {herokurk} **\n"
                    f" °  `LogChat:` ** {logrk} **\n"
                    f" °  `Sudo:` ** {sudork} **\n"
                    f" °  `SpamProtect:` ** {ss} **\n"                    
                    f" °  `Uptime:` ** {str(datetime.now() - START_TIME).split('.')[0]} **\n\n"                                   
                    f"**{ALIVE_E_MMSG}**")
    await alive.client.send_file(alive.chat_id, shivam,caption=text, force_document=False)
    await alive.delete()
