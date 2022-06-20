from sqlalchemy import Column, ForeignKey, Integer, String, INTEGER, Text, BIGINT
from app.api_v0.database.config.db_connect import Base


class StudentDepartment(Base):
    __tablename__ ="student_department"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    stud_id = Column(Integer, ForeignKey('students.id'))
    dep_id = Column(Integer, ForeignKey('departments.id'))
