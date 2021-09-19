from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base_model import Base
import datetime


class Waitlist(Base):
    __tablename__ = "waitlist"

    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey("special_child.id"), nullable=False)
    special_child = relationship("SpecialChild")
    therapist_id = Column(Integer, ForeignKey("therapist.id"), nullable=False)
    therapist = relationship("Therapist")
    created_at = Column(DateTime, default=lambda _: datetime.datetime.utcnow())
    modified_at = Column(DateTime, onupdate=lambda _: datetime.datetime.utcnow())
