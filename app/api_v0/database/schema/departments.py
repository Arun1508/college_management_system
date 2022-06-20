from sqlalchemy import Column, Integer, String, INTEGER, Text, BIGINT
from app.api_v0.database.config.db_connect import Base


class Department(Base):
    __tablename__ ="departments"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String)