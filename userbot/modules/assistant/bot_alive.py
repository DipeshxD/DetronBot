from telethon import events

from userbot import ALIVE_NAME, bot

currentversion = "1.0"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DetronBot"
PM_IMG = "https://telegra.ph/file/ecb54ca5afd9c647424a6.mp4"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.7.4` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `{currentversion}`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](https://github.com/xdipesh/DetronBot/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [DetronBot](GitHub.com/xdipesh)\n"
pm_caption += "[Assistant By DetronBot 🇮🇳](https://telegra.ph/file/2f2b8d40e3f2fa4acdc8f.mp4)"


@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
