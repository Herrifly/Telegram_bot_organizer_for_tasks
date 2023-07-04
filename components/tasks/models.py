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
    priority: enum.Enum = sq.Column(sq.Enum(PriorityLevel))
    status: enum.Enum = sq.Column(sq.Enum(Status))

    user_id: int = sq.Column(sq.Integer, sq.ForeignKey('users.id'))
    @classmethod
    def insert(cls, title: str, description: str, deadline: Date, priority: PriorityLevel, status: Status):
        db_session.execute(
            text(
                """INSERT INTO tasks (title, description, deadline, priority, status)
                VALUES (:title, :description, :deadline, :priority, :status);"""

            ),
            params={
                'title': title,
                'description': description,
                'deadline': deadline,
                'priority': priority.name,
                'status': status.name
            }
        )

        db_session.commit()
