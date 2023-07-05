import datetime
from components.tasks.models import Tasks
from components.users.models import Users

set_priority = {'A', 'B', 'C', 'А', 'В', 'С'}
set_status = {'в ожидании', 'в процессе', 'завершено'}


def check_data(task, user_id):
    if task[3] not in set_priority:
        return "Неверный формат приоритета, допускаются A,B,C"
    elif task[4] not in set_status:
        return "Неверный формат статуса, допускаются (в ожидании, в процессе, завершено)"
    elif len(task[2].split('-')) != 3:
        return "Неверный формат даты, допускается (год-месяц-день)"
    else:
        Tasks.insert(task[0], task[1], task[2], task[3], task[4],
                     Users.get_id_by_user_id(user_id))
        return 'Задача успешно добавлена!'


def print_tasks(tasks):
    if len(tasks) != 0:
        result = []
        j = 1
        for i in tasks:
            result.append(f'Задача {j}:\n{i.title}\n{i.description}\n{i.deadline}\n{i.priority}\n{i.status}')
            j += 1

        result = '\n'.join(result)
    else:
        result = "Таких задачек нет"
    return result
