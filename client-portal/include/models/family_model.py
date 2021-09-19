from sqlalchemy import Column, Integer, String, DateTime
from .base_model import Base
import datetime


class Family(Base):
    __tablename__ = "family"

    id = Column(Integer, primary_key=True)
    father_name = Column(String(100), nullable=False)
    mother_name = Column(String(100), nullable=False)
    father_occupation = Column(String(50), nullable=False)
    mother_occupation = Column(String(50), nullable=False)
    father_contact_num = Column(String(15), nullable=False)
    mother_contact_num = Column(String(15), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, default=lambda _: datetime.datetime.utcnow())
    modified_at = Column(DateTime, onupdate=lambda _: datetime.datetime.utcnow())
