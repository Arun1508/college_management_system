from pydantic import BaseModel

class StudentModel(BaseModel):
    id: int
    name:str
