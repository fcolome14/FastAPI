from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
class ProductBase(BaseModel):
    name: str
    price: int
    # user: UserOut

class ProductUpdate(ProductBase):
    published: bool
    
class ProductCreate(ProductBase):
    pass

class UserCreate(UserBase):
    pass
    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserVerified(UserOut):
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None