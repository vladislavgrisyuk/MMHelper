from typing import Any
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.message_entity import MessageEntity
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from talent import talentS
import helper

storage = MemoryStorage()

token = '5014356260:AAExs4--9I4IcNkawOxwrf6fM3xFaidGRiU'


bot = Bot(token)
dp = Dispatcher(bot, storage=storage)


class TalentState(StatesGroup):
    level = State()
    potential = State()
    baseStrength = State()
    spiritPercent = State()
    wiseLevel = State()
    auraPercent = State()
    teaStrength = State()
    itemStrength = State()
    soulmatesStrength = State()  # Strength of the soulames splitted by ','
    soulmatesPercent = State()  # Percent bonus of the soulames splitted by ','


async def executeAnswer(self, value, shouldCheck=True) -> bool:
    try:
        async with self.proxy() as data:
            if helper.isNumberCorrect(value) or not shouldCheck:
                data[str(await dp.get_current().current_state().get_state()).split(':')[1]] = value
                return True
            else:
                return False
    except ValueError:
        print(ValueError)
        return False


@dp.message_handler(commands=['reset'])
async def begin(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, '<i>Возвар в главное меню</i>', parse_mode='HTML')
    await state.finish()


@dp.message_handler(commands=['start2'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id, '<i>asd</i>', parse_mode='HTML')
    bot.set_my_commands()


@dp.message_handler(commands=['calc'], state=None)
async def beginCalculate(message: types.Message, state: FSMContext):
    try:
        await message.answer('Начало подсчета...')
        await TalentState.level.set()
        await message.answer('Введите уровень умельца: ')
    except ValueError:
        print(ValueError)


@dp.message_handler(state=TalentState.level)
async def beginCalculate(message: types.Message, state: FSMContext):
    try:
        if not message.text.isnumeric() and await executeAnswer(state, message.text):
            await bot.send_message(message.chat.id, 'Уровень должен быть целым числом')
            return

        await TalentState.next()
        await message.answer('Введите характер умельца: (Пример - 112): ')
    except ValueError:
        print(ValueError)


@dp.message_handler(state=TalentState.potential)
async def beginCalculate(message: types.Message, state: FSMContext):
    try:
        if not message.text.isnumeric() and await executeAnswer(state, message.text):
            await bot.send_message(message.chat.id, 'Характер должен быть целым числом')
            return

        await TalentState.next()
        await message.answer('Введите базовую силу умельца (Пример - 6490999): ')
    except ValueError:
        print(ValueError)


@dp.message_handler(state=TalentState.baseStrength)
async def beginCalculate(message: types.Message, state: FSMContext):
    try:
        if not message.text.isnumeric() and await executeAnswer(state, message.text):
            await bot.send_message(message.chat.id, 'Базовая сила должна быть целым числом')
            return

        await executeAnswer(state, message.text)
        await TalentState.next()
        await message.answer('Введите процент духа (Пример - 608.8): ')
    except ValueError:
        print(ValueError)


@dp.message_handler(state=TalentState.spiritPercent)
async def beginCalculate(message: types.Message, state: FSMContext):
    try:
        if not helper.isFloat(message.text.strip()) and await executeAnswer(state, message.text.replace('%', '').replace(',', '.')):
            await bot.send_message(message.chat.id, 'Процент духа должен быть числом с плавающей точкой (Пример - 608.8)')
            return

        await TalentState.next()
        await message.answer('Введите уровень мудрости (Пример - 2): ')
    except ValueError:
        print(ValueError)


@dp.message_handler(state=TalentState.wiseLevel)
async def beginCalculate(message: types.Message, state: FSMContext):
    try:
        if not message.text.isnumeric() and await executeAnswer(state, message.text.replace('%', '').replace(',', '.')):
            await bot.send_message(message.chat.id, 'Уровень мудрости должен быть целым числом (Пример - 2)')
            return

        await TalentState.next()
        await message.answer('Введите процент ауры богемы (Пример - 15): ')
    except ValueError:
        print(ValueError)


@dp.message_handler(state=TalentState.auraPercent)
async def beginCalculate(message: types.Message, state: FSMContext):
    try:
        if not message.text.isnumeric() and await executeAnswer(state, message.text.replace('%', '').replace(',', '.')):
            await bot.send_message(message.chat.id, 'Процент ауры богемы быть целым числом (Пример - 2)')
            return

        await TalentState.next()
        await message.answer('Введите силу от чайного магазина (Пример - 42704): ')
    except ValueError:
        print(ValueError)


@dp.message_handler(state=TalentState.teaStrength)
async def beginCalculate(message: types.Message, state: FSMContext):
    try:
        if not message.text.isnumeric() and await executeAnswer(state, message.text.replace('%', '').replace(',', '.')):
            await bot.send_message(message.chat.id, 'Сила от чая должна быть целым числом (Пример - 42704)')
            return

        await TalentState.next()
        await message.answer('Введите силу от предметов (Пример - 125000): ')
    except ValueError:
        print(ValueError)


@dp.message_handler(state=TalentState.itemStrength)
async def beginCalculate(message: types.Message, state: FSMContext):
    try:
        if not message.text.isnumeric() and await executeAnswer(state, message.text.replace('%', '').replace(',', '.')):
            await bot.send_message(message.chat.id, 'Сила от предметов должна быть целым числом (Пример - 4875000)')
            return

        await TalentState.next()
        await message.answer('Введите чистую силу от пассий через запятую (Пример - 125000, 65000, 1300): ')
    except ValueError:
        print(ValueError)


@dp.message_handler(state=TalentState.soulmatesStrength)
async def beginCalculate(message: types.Message, state: FSMContext):
    # if not message.text.isnumeric():
    #     await bot.send_message(message.chat.id, 'Сила от пассий должна быть целым числом через запятую (Пример - 8540884)')
    #     return
    try:
        await executeAnswer(state, message.text.replace('%', ''))
        await TalentState.next()
        await message.answer('Введите процентную силу от пассий через запятую (Пример - 12.5, 37, 5.5): ')
    except ValueError:
        print(ValueError)


@dp.message_handler(state=TalentState.soulmatesPercent)
async def beginCalculate(message: types.Message, state: FSMContext):
    # if not message.text.isnumeric():
    #     await bot.send_message(message.chat.id, 'Процент пассий должен быть или целым, или числом с плавающей точкой через запятую (Пример 37, 35.3)')
    #     return
    try:
        cMes = message.text.replace('%', '')

        for val in cMes.split(','):
            if not helper.isFloat(val.strip()) and helper.isNumberCorrect(val):
                await bot.send_message(message.chat.id, 'Процент пассий должен быть или целым числом, или числом с точкой (Пример - 38.4, 4, 4.5)')
                return

        await executeAnswer(state, cMes, False)
        await bot.send_message(message.chat.id, await state.get_data())
        await state.finish()
        talent = talentS(await state.get_data())
        talent.calculateStrength()
    except ValueError:
        print(ValueError)


async def on_startup(dispatcher):
    commands = [
        {
            "command": "start",
            "description": "Start using bot"
        },
        {
            "command": "help",
            "description": "Display help"
        },
        {
            "command": "calc",
            "description": "Посчитать силу умельца"
        }
    ]
    await bot.set_my_commands(commands)


executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
