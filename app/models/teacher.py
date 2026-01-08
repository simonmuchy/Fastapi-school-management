from sqlalchemy import Column, Integer, String, Boolean
from ..database import Base


class User(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False, unique=True)
    subject = Column(String, nullable=False, unique=True)
    class_id = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)