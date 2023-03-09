# meta banner: https://te.legra.ph/file/8d17459bce508ab404cd4.jpg
#meta developer: @GoormHikka, @modwini
import random
from datetime import timedelta
import asyncio
import time
from telethon import events

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class FarmMonacoMod(loader.Module):
    """Модуль для автоматического фарминга, для запуска по очереди введите такие команды:<.b>, <p>, <l>, <t> команды обезательно нужно вводить в лс @MonacoGamebot!"""

    strings = {"name": "Farm"}
    
    async def bcmd(self, message):
        while True:
            await message.respond("Ежедневный бонус")
            await asyncio.sleep(1200)
         
    async def pcmd(self, message):
        while True:
            await message.respond("Бизнес снять")
            await asyncio.sleep(1920) 
            
    async def lcmd(self, message):
        while True:
            await message.respond("Город снять")
            await asyncio.sleep(1220)
            
    async def tcmd(self, message):
        while True:
            await message.respond("Работать")
            await asyncio.sleep(1440)  