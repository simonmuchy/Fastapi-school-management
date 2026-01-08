from sqlalchemy import Column, Integer, String, Boolean, DateTime
from ..database import Base
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False, unique=True)
    id_number = Column(Integer, nullable=False, unique=True)
    addmission_year = Column(Integer, nullable=False)
    class_id = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        nullable=False
    )
    