import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN
from components.users.models import Users
from components.tasks.models import Tasks

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

    await message.answer(f"Привет, {message.from_user.first_name}, я помогу тебе быть более продуктивным\n"
                         f"Чтобы добавить задачу напиши ее в формате:\n"
                         f"Название;Описание;Дедлайн;Приоритет;Статус\n\n"
                         f"Пример: Сделать сайт;Интернет магазин WB, по заказу школы;2023-07-03(год-месяц-день);A(A-высокий,B-средний,C-низкий)")


@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.reply('Могу тебе показать твои:\n'
                        '/tasks_waiting  - задачи в ожидании\n'
                        '/tasks_in_progress - задачи в процессе выполнения\n'
                        '/tasks_completed - выполненные задачи\n'
                        '/all_tasks - все задачи\n'
                        'всего лишь кликни на нужный вариант')


@dp.message(Command('tasks_waiting'))
async def cmd_tasks_waiting(message: types.Message):
    tasks = Tasks.get_tasks_waiting(message.from_user.id)
    if len(tasks) != 0:
        result = ['Название ', ' Описание ', ' Дедлайн ', ' Приоритет ', ' Статус ']
        for i in tasks:
            result.append(f'{i.title}  {i.description}  {i.deadline}  {i.priority}  {i.status}')

        result = '\n'.join(result)
    else:
        result = "Таких задачек нет"
    await message.answer(result)


@dp.message(Command('tasks_in_progress'))
async def cmd_tasks_in_progress(message: types.Message):
    tasks = Tasks.get_tasks_in_progress(message.from_user.id)
    await message.answer("В разработке ...")


@dp.message(Command('tasks_completed'))
async def cmd_tasks_completed(message: types.Message):
    tasks = Tasks.get_tasks_completed(message.from_user.id)
    await message.answer("В разработке ...")


@dp.message(Command('all_tasks'))
async def cmd_all_tasks(message: types.Message):
    tasks = Tasks.get_all_tasks(message.from_user.id)
    await message.answer("В разработке ...")
