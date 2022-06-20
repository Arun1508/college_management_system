from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.api_v0.database.schema.students import Student


class StudentDAL():

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_student(self, name: str):
        self.db_session.add(Student(name=name))
        await self.db_session.flush()

    async def get_all_student(self):
        students = await self.db_session.execute(select(Student).order_by(Student.id))
        return students.scalars().all()
    