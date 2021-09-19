from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base_model import Base
import datetime


class SpecialChild(Base):
    __tablename__ = "special_child"

    id = Column(Integer, primary_key=True)
    family_id = Column(Integer, ForeignKey("family.id"), nullable=False)
    family = relationship("Family")

    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=lambda _: datetime.datetime.utcnow())
    modified_at = Column(DateTime, onupdate=lambda _: datetime.datetime.utcnow())
