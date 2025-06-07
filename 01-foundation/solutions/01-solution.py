from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool

input_data={ "id":1, "name":"Laptop", "price":1000, "in_stock":True}

product = Product(**input_data)   

print(product)