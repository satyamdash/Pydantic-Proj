from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class UserSignup(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    age: int = Field(..., gt=0, lt=120)
    password: str = Field(...)


class Settings(BaseModel):
    app_name: str = "Fast-API app"
    admin_email: str = "admin@example.com"
    admin_password: str = Field(..., min_length=8)

    class Config:
        json_schema_extra = {
            "example": {
                "app_name": "Fast-API app",
                "admin_email": "admin@example.com",
                "admin_password": "adminpassword123"
            }
        }

def get_app_settings():
    # In a real application, these would come from environment variables
    return Settings(
        app_name="Fast-API app",
        admin_email="admin@example.com",
        admin_password="adminpassword123"  # This should be loaded from environment variables
    )

# def get_settings_2(settings: Settings = Depends(get_app_settings)):
#     return {"app_name": settings.app_name, "admin_email": settings.admin_email}

@app.post("/signup")
def signup(user: UserSignup):
    # In a real application, you would:
    # 1. Hash the password
    # 2. Store user in database
    # 3. Send verification email
    user_dict = user.model_dump()
    user_dict.pop("password")  # Remove password from response
    return {"message": "User created successfully", "user": user_dict}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/settings")
def get_settings_route():
    return get_app_settings()
