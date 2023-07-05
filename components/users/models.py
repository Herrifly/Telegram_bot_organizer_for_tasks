import sqlalchemy as sq
from sqlalchemy.sql import text
from sqlalchemy import Date
from datetime import datetime
from database.db_sync import Base, db_session


class Users(Base):
    __tablename__ = 'users'
    id: int = sq.Column(sq.Integer, primary_key=True, autoincrement=True, nullable=False)

    user_id: int = sq.Column(sq.Integer, nullable=False)
    username: str = sq.Column(sq.String)
    date_registration: Date = sq.Column(Date)

    @classmethod
    def insert(cls, user_id: int, username: str):
        db_session.execute(
            text(
                """INSERT INTO users (user_id, username, date_registration)
                VALUES (:user_id, :username, :date_registration);"""

            ),
            params={
                'user_id': user_id,
                'username': username,
                'date_registration': datetime.now().date()
            }
        )

        db_session.commit()

    @classmethod
    def select(cls, user_id: int):
        result = db_session.execute(
            text(
                """SELECT user_id FROM users WHERE user_id = :user_id"""
            ),
            params={
                'user_id': user_id
            }
        )

        db_session.commit()

        return result.fetchall()

    @classmethod
    def get_id_by_user_id(cls, user_id: int):
        result = db_session.execute(
            text(
                '''SELECT id from users WHERE user_id = :user_id;'''
            ),
            params=
            {
                'user_id': user_id
            }
        )
        return result.fetchone().id
