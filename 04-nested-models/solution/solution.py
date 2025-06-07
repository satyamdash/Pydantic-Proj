from pydantic import BaseModel #type: ignore
from typing import List

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons


class Lesson(BaseModel):
    name:str
    content:str

class Module(BaseModel):
    name:str
    lessons:List[Lesson]

class Course(BaseModel):
    name:str
    modules:List[Module]



input_data={ "name":"Python Basics", "modules":[{"name":"Introduction to Python", "lessons":[{"name":"What is Python?", "content":"Python is a versatile programming language..."}]}]}
