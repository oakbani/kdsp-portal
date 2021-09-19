import datetime
from sqlalchemy import Column, DateTime, Integer, Unicode

from .base_model import Base
import enum


class RoleTypes(enum.Enum):
    admin = "admin"
    user = "user"
    guest = "guest"
    family = "family"
    donor = "donor"


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(50), nullable=False, unique=True)
    created_at = Column(DateTime, default=lambda _: datetime.datetime.utcnow())
    modified_at = Column(DateTime, onupdate=lambda _: datetime.datetime.utcnow())

    def __repr__(self):
        return "<Role (id=%s)(title=%s)>" % (self.id, self.title)
