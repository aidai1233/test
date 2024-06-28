from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


echo_router = Router()


@echo_router.message()
async def echo(message: types.Message):
    words = message.text.split()
    reversed_words = ' '.join(reversed(words))
    await message.answer(reversed_words)