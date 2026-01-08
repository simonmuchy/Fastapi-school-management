from sqlalchemy import Column, Integer, String
from ..database import Base

class User(Base):
    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    teacher_id = Column(String, nullable=False, unique=True)
    