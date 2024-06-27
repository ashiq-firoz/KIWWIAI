from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import FastAPI, Depends, File, UploadFile, Body, Query,Form
from core.initializer import initialise_express
from core.pages import generate_page,create_content,get_page
from core.routes import add_route
from fastapi.middleware.cors import CORSMiddleware

import scheme

app = FastAPI()

origins = [
    "http://localhost:3000",  # Add the URL of your Next.js app here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Api Status": "ok 200"}


@app.post("/login/",tags=["Authenthication Routes"])
async def create_item(item: str):
    print(item)
    return item

@app.post("/backendframework", tags=["Operations"])
async def select_framework(framework:scheme.BackendFrameworks):
    """
    Api to initialize a repo with Respective Backend FrameWork
    """
    if framework == scheme.BackendFrameworks.EXPRESS:
        id = initialise_express("user")
        if id!=False:
            return {"status":True,"repoID":id}
        else:
            return {"status":False}
    return {"status":False}

@app.post("/createpage", tags=["Operations"])
async def add_page(page_description:str,page_name:str,repoID : str):
    """
    API to create pages based on the description given
    """
    try:
        o1 = generate_page(page_description,repoID)
        o2 = create_content(page_description,page_name,"user",repoID)
        o3 = add_route(page_name,page_description,"user")
        
        if not o1 and not o2 and not o3: #if any of the above process fails
            return {"status":False}
        else:
            return {"status":True}
    except Exception as e:
        print(e)
        return False


@app.post("/viewpage", tags=["Operations"])
async def view_page(page_name:str):
    """API to view page in realtime"""
    print(page_name)
    return {"url":get_page(page_name)}

