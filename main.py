import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN
from components.users.models import Users

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id

    if len(Users.select(user_id)) == 0:
        Users.insert(message.from_user.id, message.from_user.username)

    await message.answer(f"Привет, {message.from_user.first_name}, я помогу тебе быть более продуктивным")


@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.reply('Мой функционал:\n'
                        '/tasks_waiting')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
