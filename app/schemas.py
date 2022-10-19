
from datetime import datetime
from operator import le
from pydantic import BaseModel, EmailStr , conint
from typing import Optional
from app.models import *
from pydantic.types import conlist



class UserCreate(BaseModel):
    email: EmailStr           # Check for proper email syntex 
    password : str

    class Config:
        orm_mode = True  # original 
 
class UserOut(BaseModel):  # Select BaseMolel is we select UserCreate then password field also get inhertited by default 
    id: int
    email: EmailStr
    created_at: datetime

    
    class Config:
        orm_mode = True  
    
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    class Config:
        orm_mode = True  

 
 
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
           
class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut  
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post : Post
    votes : int
    class Config:
            orm_mode = True

    

#  auth.py Token schemas
 
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
# Schemes for voting 

class Vote(BaseModel):
    post_id : int
    dir: conint(le=1)

    