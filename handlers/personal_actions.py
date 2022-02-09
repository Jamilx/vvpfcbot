from aiogram import types
from dispatcher import dp
from bot import BotDB
from random import randint as rd
from keyboard import kb_1, kb_week, kb_week_see, s_add,see_add,kb_okay
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMClient(StatesGroup):
	dest= State()
	day = State()
	item = State()
	item_z = State()
	item1 = State()
	item1_z = State()
	item2 = State()
	item2_z = State()
	item3 = State()
	item3_z = State()
	item4 = State()
	item4_z = State()
	ojs = State()





class FSMSee(StatesGroup):
	dest= State()
	days = State()


'''#############-Проверка всех команд-#############'''
@dp.message_handler(commands="start")
async def start(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id, first_name, last_name, username)

    await message.bot.send_message(message.from_user.id, '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓'+'\n'+"     Привіт 👋 \
	\n \n    Створи та переглядай розклад,\n      коли завгодно за допомоги\n      спеціальної клавіатури, яка зявляється\n      замість основної  🗂️\n\n\n\n     РЕКОМЕНДАЦІЇ:\n     Використовувати розмір тексту = 12\n     для його нормального відображення"+'\n'+'┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛', reply_markup =kb_1)

'''@dp.message_handler(commands="test")
async def start(message: types.Message):

	day = "понеділок"
	item = "Понеділок"
	item1= "Понеділок"
	item2= "Понеділок"
	item3= "Понеділок"
	item4= "Понеділок"
	item_z= "Понеділок"
	item1_z= "Понеділок"
	item2_z= "Понеділок"
	item3_z= "Понеділок"
	item4_z= "Понеділок"
	BotDB.add_all_info(message.from_user.id, day, item, item1, item2, item3, item4,item_z,item1_z,item2_z,item3_z,item4_z)
'''
#Назад
@dp.message_handler(commands="Назад")
async def back(message: types.Message):
    await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛',reply_markup =kb_1)
'''#Зміни
@dp.message_handler(commands="Зміни")
async def create(message: types.Message):
	await message.reply('Виберіть день')
'''



@dp.message_handler(commands="Розклад", state = None)
async def rozklad(message: types.Message, state: FSMContext):
	await message.answer('┏━━━━━━━━┓\n'+'█   Виберіть    '+'\n┗━━━━━━━━┛', reply_markup = see_add)
	await FSMClient.dest.set()


@dp.message_handler(state = FSMClient.dest)
async def dest(message: types.Message,  state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	if message.text =="Редагувати розклад":
		await FSMClient.day.set()
		await message.answer('┏━━━━━━━━┓\n'+'█   Виберіть    '+'\n┗━━━━━━━━┛', reply_markup =kb_week)
	if message.text =="Переглянути розклад":
		await FSMSee.days.set()
		await message.answer('┏━━━━━━━━┓\n'+'█   Виберіть    '+'\n┗━━━━━━━━┛', reply_markup = kb_week)

@dp.message_handler(state = FSMSee.days)
async def dest(message: types.Message,  state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		user_id_recs = message.from_user.id
		day = message.text
		ent = BotDB.see_schud(user_id_recs, day)
		if ent == False:
			await message.answer('Немає розкладу на '+ day, reply_markup = kb_1)
			await state.finish()
		else:
			await message.answer(ent, reply_markup = kb_1)
			await state.finish()


"""########## Створення розкладу ##########"""
@dp.message_handler(state = FSMClient.day)
async def start(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['day'] = message.text
		await FSMClient.next()
		await message.answer('┏━━━━━━━━━━━━━━━━┅┅┅┉┉\n┃ Введіть чисельник 1️⃣ пари\n┗━━━━━━━━━━━━━━━━┅┅┅┉┉', reply_markup = s_add)


@dp.message_handler(state = FSMClient.item)
async def oneK(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['item'] = message.text
		await FSMClient.next()
		await message.answer('┏━━━━━━━━━━━━━━━━┅┅┅┉┉\n┃ Введіть знаменник 1️⃣ пари\n┗━━━━━━━━━━━━━━━━┅┅┅┉┉', reply_markup = s_add)

@dp.message_handler(state = FSMClient.item_z)
async def oneK_z(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['item_z'] = message.text
		await FSMClient.next()
		await message.answer('┏━━━━━━━━━━━━━━━━┅┅┅┉┉\n┃Введіть чисельник 2️⃣ пари\n┗━━━━━━━━━━━━━━━━┅┅┅┉┉', reply_markup = s_add)


@dp.message_handler(state = FSMClient.item1)
async def twoK(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['item1'] = message.text
		await FSMClient.next()
		await message.answer('┏━━━━━━━━━━━━━━━━┅┅┅┉┉\n┃Введіть знаменник 2️⃣ пари\n┗━━━━━━━━━━━━━━━━┅┅┅┉┉', reply_markup = s_add)

@dp.message_handler(state = FSMClient.item1_z)
async def oneK(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('Головне меню', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['item1_z'] = message.text
		await FSMClient.next()
		await message.answer('┏━━━━━━━━━━━━━━━━┅┅┅┉┉\n┃Введіть чисельник 3️⃣ пари\n┗━━━━━━━━━━━━━━━━┅┅┅┉┉', reply_markup = s_add)

@dp.message_handler(state = FSMClient.item2)
async def three_k(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['item2'] = message.text
		await FSMClient.next()
		await message.answer('┏━━━━━━━━━━━━━━━━┅┅┅┉┉\n┃Введіть знаменик 3️⃣ пари\n┗━━━━━━━━━━━━━━━━┅┅┅┉┉', reply_markup = s_add)

@dp.message_handler(state = FSMClient.item2_z)
async def oneK(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['item2_z'] = message.text
		await FSMClient.next()
		await message.answer('┏━━━━━━━━━━━━━━━━┅┅┅┉┉\n┃Введіть чисельник 4️⃣ пари\n┗━━━━━━━━━━━━━━━━┅┅┅┉┉', reply_markup = s_add)

@dp.message_handler(state = FSMClient.item3)
async def twoK(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['item3'] = message.text
		await FSMClient.next()
		await message.answer('┏━━━━━━━━━━━━━━━━┅┅┅┉┉\n┃Введіть знаменник 4️⃣ пари\n┗━━━━━━━━━━━━━━━━┅┅┅┉┉', reply_markup = s_add)

@dp.message_handler(state = FSMClient.item3_z)
async def oneK(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['item3_z'] = message.text
		await FSMClient.next()
		await message.answer('┏━━━━━━━━━━━━━━━━┅┅┅┉┉\n┃Введіть чисельник 5️⃣ пари\n┗━━━━━━━━━━━━━━━━┅┅┅┉┉', reply_markup = s_add)

@dp.message_handler(state = FSMClient.item4)
async def oneK(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['item4'] = message.text
		await FSMClient.next()
		await message.answer('┏━━━━━━━━━━━━━━━━┅┅┅┉┉\n┃Введіть знаменник 5️⃣ пари\n┗━━━━━━━━━━━━━━━━┅┅┅┉┉', reply_markup = s_add)

@dp.message_handler(state = FSMClient.item4_z)
async def twoK(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	else:
		async with state.proxy() as data:
			data['item4_z'] = message.text
		await FSMClient.next()
		await message.answer("┏━━━━━━━━━━━━\n┃ Пітвердження    ✅\n┗━━━━━━━━━━━━", reply_markup =kb_okay)

@dp.message_handler(state = FSMClient.ojs)
async def okays(message: types.Message, state: FSMContext):
	if message.text =="Назад":
		await state.finish()
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛', reply_markup =kb_1)
	if message.text == "Готово":
		async with state.proxy() as data:
			BotDB.cheking(message.from_user.id, data['day'], data['item'], data['item1'], data['item2'], data['item3'], data['item4'],\
																  data['item_z'], data['item1_z'], data['item2_z'], data['item3_z'], data['item4_z'])
			await message.answer('Розклад на '+ data['day'] +' додано)', reply_markup=kb_1)
			await state.finish()

"""#######################################"""

'''
─ ━ │ ┃ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋
┌ ┍ ┎ ┏ ┐ ┑ ┒ ┓
└ ┕ ┖ ┗ ┘ ┙ ┚ ┛
├ ┝ ┞ ┟ ┠ ┡ ┢ ┣ ┤ ┥ ┦ ┧ ┨ ┩ ┪ ┫
 ┬ ┭ ┮ ┯ ┰ ┱ ┲ ┳
 ┴ ┵ ┶ ┷ ┸ ┹ ┺ ┻
 ┼ ┽ ┾ ┿ ╀ ╁ ╂ ╃ ╄ ╅ ╆ ╇ ╈ ╉ ╊ ╋
 ╌ ╍ ╎ ╏ ═ ║
 ╒ ╓ ╔ ╕ ╖ ╗
 ╘ ╙ ╚ ╛ ╜ ╝
 ╞ ╟ ╠ ╡ ╢ ╣
 ╤ ╥ ╦
 ╧ ╨ ╩
 ╪ ╫ ╬
 ╭ ╮
 ╯ ╰
 ╱ ╲ ╳ ╴ ╵ ╶ ╷ ╸ ╹ ╺ ╻ ╼ ╽ ╾ ╿
 ▀ ▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▉ ▊ ▋ ▌ ▍ ▎ ▏ ▐ ░ ▒ ▓ ▔ ▕ 𝌴
'''






'''#############-Проверка всех сообщений-#############'''
@dp.message_handler()
async def all_message(message: types.Message):
	if message.text =="Назад":
		await message.answer('┏━━━━━━━━┓\n'+'█ Головне меню'+'\n┗━━━━━━━━┛',reply_markup =kb_1)
	else:
		if message.text == message.text:
			await message.answer("шо ти пишеш? -_-")


