from typing import List

import uvicorn
from fastapi import FastAPI

from app.api_v0.database.config.db_connect import Base, engine, async_session
from app.api_v0.database.schema.students import Student
from app.api_v0.database.controller.students import StudentDAL
from app.api_v0.database.schema.departments import Department
from app.api_v0.database.schema.student_department import StudentDepartment

app = FastAPI()

@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)




@app.post("/students/")
async def create_book(name: str):
    async with async_session() as session:
        async with session.begin():
            student_dal = StudentDAL(session)
            return await student_dal.create_student(name)



@app.get("/students/")
async def get_all_books() -> List[Student]:
    async with async_session() as session:
        async with session.begin():
            student_dal = StudentDAL(session)
            return await student_dal.get_all_student()

if __name__ == '__main__':
    uvicorn.run("app.main:app", port=1111, host='127.0.0.1')
