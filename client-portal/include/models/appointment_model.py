from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base_model import Base
import datetime


class Appointment(Base):
    __tablename__ = "appointment"

    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey("special_child.id"), nullable=False)
    special_child = relationship("SpecialChild")
    therapist_id = Column(Integer, ForeignKey("therapist.id"), nullable=False)
    therapist = relationship("Therapist")
    appointment_datetime = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=lambda _: datetime.datetime.utcnow())
    modified_at = Column(DateTime, onupdate=lambda _: datetime.datetime.utcnow())
