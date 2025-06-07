from pydantic import BaseModel ,Field
from typing import List,Dict

from datetime import datetime


class Address(BaseModel):
    street:str
    city:str
    state:str
    zip_code:str

class User(BaseModel):
    name:str
    email:str
    address:Address
    created_at:datetime=Field(default_factory=datetime.now)
    tags:List[str]=[]

#create a user instance
user = User(name="John Doe", email="john.doe@example.com", address=Address(street="123 Main St", city="Anytown", state="CA", zip_code="12345"),tags=["python","pydantic"])

#serialize to json
json_data = user.model_dump_json()
print(json_data)

#serialize to yaml


