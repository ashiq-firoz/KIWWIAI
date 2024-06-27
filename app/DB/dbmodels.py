from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Repo(BaseModel):
    userid : str
    name: str
    id:str