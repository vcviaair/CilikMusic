# © KenendyXMusic
# Adjustment for yukki by Fariz <XBOT-MUSIC>
# Thanks Ken 💙
# Ported by Fariz

from os import path
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import Message
from time import time
from datetime import datetime
from CilikMusic import app
from pytgcalls import __version__ as pytover

from CilikMusic.config import (
    GROUP,
    CHANNEL,
)
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


CILIK_IMG = "https://telegra.ph/file/f6ad2607939dc82d7190c.jpg"


@app.on_message(filters.command(["alive", "alive@Tg_Vc_00_Bot"]))
async def alive(client, message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await client.send_photo(message.chat.id,
        photo=f"{CILIK_IMG}",
        caption=f"""**Hallo {message.from_user.mention()}.** \n
✪ **I'm Working Properly** \n
✪ **Uptime : `{uptime}`** \n
✪ **Pyrogram Version : `{pyrover}`** \n
✪ **PyTgCalls Version: `{pytover.__version__}`** \n
✪ **Using New Version** \n
**Thanks For Using Me 🔥**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"t.me/{GROUP}"
                    ),
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇs", url=f"t.me/{CHANNEL}"
                    )
                ]
            ]
        )
    )
