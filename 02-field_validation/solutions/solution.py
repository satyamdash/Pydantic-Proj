from pydantic import BaseModel, Field
from typing import Optional,List,Dict

# TODO: Create Employee model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General')
# - salary: float (must be >= 10000) 

class Employee(BaseModel):
    id:int
    name: str=Field(... ,min_length=3,max_length=100,description="Emplyee name",example="John Doe")
    department: Optional[str] = Field(default='General')
    salary :float=Field(...,ge=10000)

input_data={ "id":1, "name":"Johv", "department":"IT", "salary":10000}
Employee(**input_data)
