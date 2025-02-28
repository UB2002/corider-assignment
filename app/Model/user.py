from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from bson import ObjectId


class User(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(ObjectId()))
    name : str = Field(..., min_length=3, max_length=50)
    email : EmailStr
    password : str = Field(..., min_length=8, max_length=50)

    class Config:
        arbitrary_types_allowed = True
        json_encoders={
            ObjectId: str
        }