import os
from flask import current_app, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from config import DB_NAME, DB_PORT, DB_USER, DB_PASS, DB_HOST


def init_db():
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    session_class = sessionmaker(bind=engine)
    return session_class()


db_session = init_db()
