import email
from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title : str
    blog : str
    creator_id :int

class User(BaseModel):
    name : str
    email : str
    password : str

class UserView(BaseModel):
    name : str
    email : str
    class Config():
        orm_mode = True


class UserBlog(BaseModel):
    title : str
    blog : str
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name : str
    email : str
    blogs : List[UserBlog] = []
    class Config():
        orm_mode = True

class ViewUser(BaseModel):
    name : str
    email : str
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title : str
    blog : str
    creator : ViewUser

    class Config():
        orm_mode = True