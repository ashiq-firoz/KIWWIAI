from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import FastAPI, Depends, File, UploadFile, Body, Query,Form
from core.initializer import initialise_express
from core.pages import generate_page,create_content
from core.routes import add_route

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login/")
async def create_item(item: str):
    print(item)
    return item

@app.post("/framework")
async def select_framework(framework : str,no : int):
    print(framework)
    if framework == "express":
        print(no)
        if initialise_express("user1"):
            return {"status":True}
        else:
            return {"status":False}
    return {"status":False}

@app.post("/pages")
async def add_pages(page_data:str,page_name:str):
    print(page_data)
    try:
        o1 = generate_page(page_data)
        o2 = create_content(page_data,page_name,"user1")
        o3 = add_route(page_name,page_data,"user1")
        
        if not o1 and not o2 and not o3:
            return {"status":False}
        else:
            return {"status":True}
    except Exception as e:
        print(e)
        return False


