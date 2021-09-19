from sqlalchemy import Column, Integer, String, DateTime
from .base_model import Base
import datetime


class Donor(Base):
    __tablename__ = "donor"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_num = Column(String(15), nullable=False)
    created_at = Column(DateTime, default=lambda _: datetime.datetime.utcnow())
    modified_at = Column(DateTime, onupdate=lambda _: datetime.datetime.utcnow())
