from pydantic import BaseModel

class User(BaseModel):
    id : int 
    names:str
    email:str
    password:str