from Bestie_Robot import pbot
from pyrogram import filters
from pyrogram.types import Message

@pbot.on_message(filters.command("whois", prefixes=["/", ".", "?", "-"]))
async def whois(_, m: Message):
    if m.reply_to_message:
        await pbot.send_message(m.reply_to_message.date)
        return
    if not m.reply_to_message:
        await pbot.send_message(m.date)
        return
