import sqlalchemy as sq
import enum
from sqlalchemy.sql import text
from sqlalchemy import Date
from database.db_sync import Base, db_session


class PriorityLevel(enum.Enum):
    A = 1
    B = 2
    C = 3


class Status(enum.Enum):
    waiting = 1
    in_progress = 2
    completed = 3


class Tasks(Base):
    __tablename__ = 'tasks'
    id: int = sq.Column(sq.Integer, primary_key=True, autoincrement=True, nullable=False)

    title: str = sq.Column(sq.String)
    description: str = sq.Column(sq.String)
    deadline: Date = sq.Column(Date)
    priority: str = sq.Column(sq.String)
    status: str = sq.Column(sq.String)

    user_id: int = sq.Column(sq.Integer, sq.ForeignKey('users.id'), nullable=False)

    @classmethod
    def insert(cls, title: str, description: str, deadline: Date, priority: str, status: str, user_id: int):
        db_session.execute(
            text(
                """INSERT INTO tasks (title, description, deadline, priority, status, user_id)
                VALUES (:title, :description, :deadline, :priority, :status, :user_id);"""

            ),
            params={
                'title': title,
                'description': description,
                'deadline': deadline,
                'priority': priority,
                'status': status,
                'user_id': user_id
            }
        )

        db_session.commit()

    @classmethod
    def get_tasks_waiting(cls, user_tg_id: int):
        result = db_session.execute(
            text(
                '''SELECT title, description, deadline, priority, status FROM tasks
                 JOIN users ON users.id = tasks.user_id
                 WHERE users.user_id = :user_tg_id and status = 'в ожидании';'''
            ),
            params=
            {
                'user_tg_id': user_tg_id
            }
        )

        return result.fetchall()

    @classmethod
    def get_tasks_in_progress(cls, user_tg_id: int):
        result = db_session.execute(
            text(
                '''SELECT title, description, deadline, priority, status FROM tasks
                 JOIN users ON users.id = tasks.user_id
                 WHERE users.user_id = :user_tg_id and status = 'в процессе';'''
            ),
            params=
            {
                'user_tg_id': user_tg_id
            }
        )

        return result.fetchall()

    @classmethod
    def get_tasks_completed(cls, user_tg_id: int):
        result = db_session.execute(
            text(
                '''SELECT title, description, deadline, priority, status FROM tasks
                 JOIN users ON users.id = tasks.user_id
                 WHERE users.user_id = :user_tg_id and status = 'завершено';'''
            ),
            params=
            {
                'user_tg_id': user_tg_id
            }
        )

        return result.fetchall()

    @classmethod
    def get_all_tasks(cls, user_tg_id: int):
        result = db_session.execute(
            text(
                '''SELECT title, description, deadline, priority, status FROM tasks
                 JOIN users ON users.id = tasks.user_id
                 WHERE users.user_id = :user_tg_id;'''
            ),
            params=
            {
                'user_tg_id': user_tg_id
            }
        )

        return result.fetchall()
