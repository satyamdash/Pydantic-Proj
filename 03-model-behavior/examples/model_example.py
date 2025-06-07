from pydantic import BaseModel ,field_validator,model_validator,computed_field

class User(BaseModel):
    username:str

    @field_validator('username')
    def username_validator(cls,v):
        if len(v)<3:
            raise ValueError("Username must be at least 3 characters long")
        return v
    
    @model_validator(mode='after')
    def validate_username(self):
        if self.username.lower() == 'admin':
            raise ValueError("Username cannot be 'admin'")
        return self
    
class signupdata(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode='after')
    def validate_password(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
    
class Product(BaseModel):
    price:float
    quantity:int


    @computed_field
    @property

    def total_price(self)->float:
        return self.price * self.quantity