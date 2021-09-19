from sqlalchemy import Column, Integer, String, DateTime
from .base_model import Base
import datetime


class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    message = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=lambda _: datetime.datetime.utcnow())
    modified_at = Column(DateTime, onupdate=lambda _: datetime.datetime.utcnow())
