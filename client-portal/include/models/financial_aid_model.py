from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base_model import Base
import datetime


class FinancialAid(Base):
    __tablename__ = "financial_aid"

    id = Column(Integer, primary_key=True)
    family_id = Column(Integer, ForeignKey("family.id"), nullable=False)
    family = relationship("Family")

    family_income = Column(Integer, nullable=False)
    expenses = Column(Integer, nullable=False)
    eligible_for_aid = Column(Boolean, nullable=True)
    created_at = Column(DateTime, default=lambda _: datetime.datetime.utcnow())
    modified_at = Column(DateTime, onupdate=lambda _: datetime.datetime.utcnow())
