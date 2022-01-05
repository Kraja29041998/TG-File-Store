from pyrogram import Client, filters
from utils import temp
from pyrogram.types import Message
from plugins.database.access_db import db
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *
async def banned_users(_, client, message: Message):
    return (
        message.from_user is not None or not message.sender_chat
    ) and message.from_user.id in temp.BANNED_USERS

banned_user = filters.create(banned_users)


@Client.on_message(filters.private & banned_user & filters.incoming)
async def ban_reply(bot, message):
    ban = await db.get_ban_status(message.from_user.id)
    await message.reply(f'Sorry Bro, You Are Banned To Use Me. \nBan Reason : {ban["ban_reason"]} \n Ban Duration : {ban["ban_duration"]} \n Ban Time : {ban["banned_on"]}\n\n If You Think This is Mistake. Contact To :- @DKBOTZ')
