from sqlalchemy import Column, Integer,String
from app.api_v0.database.config.db_connect import Base

class Student(Base):
    __tablename__ ="students"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String)