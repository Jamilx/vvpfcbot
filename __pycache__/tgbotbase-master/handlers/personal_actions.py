from distutils import command
from aiogram import types
from dispatcher import dp
import config
import re
from bot import BotDB

@dp.message_handler()
async def start(message: types.Message):
    if(not BotDB.user_exits(message.from_user.id)):
        BotDB.add_user(message.from_user.id)

    await message.bot.send_message(message.from_user.id, 'Привет \n я бот який зберигає у соби розклад')

@dp.message_handler()
async def add_schedules(message: types.Message):
    cmd_variants = ('/add_schedule', '/add_s', '!add_schedule', '!add_s')
    await message.answer('Введить день')
    week_day = message.text
    await message.answer('Введить назву предмету')
    item = message.text

    BotDB.add_schedule(message.from_user.id, week_day, item)

    await message.reply('До розкладу на ' + week_day + 'було занесено предмет ' + item)


@dp.message_handler()
async def schedules(message: types.Message):
    cmd_variants = ('/schedule', '/s', '!schedule', '!s')
#shudel_s = BotDB.get_schedule(message.from_user.id, week_day, item)
    
