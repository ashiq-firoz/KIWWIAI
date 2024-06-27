import os
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, status, Form, Body, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pymongo.mongo_client import MongoClient

import scheme
from core.initializer import initialise_express
from core.pages import generate_page, create_content, get_page
from core.routes import add_route
from DB.db import create_user, get_user
from DB.dbmodels import User

app = FastAPI()

# CORS setup
origins = [
    "http://localhost:3000",  # Replace with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB setup (assuming MongoClient is correctly configured)

@app.get("/")
def read_root():
    return {"Api Status": "ok 200"}

@app.post("/signup/", tags=["Authentication Routes"])
async def signup(username:str,password : str):
    """
    API endpoint for user signup
    """
    user = User(username=username, password=password)
    result = create_user(user.username, user.password)
    if result:
        return {"status": True, "message": "User created successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User creation failed")

@app.post("/login/", tags=["Authentication Routes"])
async def login(username:str,password : str,response:Response):
    """
    API endpoint for user login
    """
    user = get_user(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    # Example: Create access token here if needed

    return {"status": True, "message": "Login successful","id":user["_id"],"repoCount":user["count"],"password":user["password"]}

@app.post("/backendframework", tags=["Operations"])
async def select_framework(framework: scheme.BackendFrameworks, userId: str,repocount: str):
    """
    API to initialize a repo with respective Backend Framework
    """
    
    if framework == scheme.BackendFrameworks.EXPRESS and userId:
        id = initialise_express(userId+repocount)
        if id:
            return {"status": True, "repoID": id}
    return {"status": False}

@app.post("/createpage", tags=["Operations"])
async def add_page(page_description: str, page_name: str, repoID: str):
    """
    API to create pages based on the description given
    """
    try:
        o1 = generate_page(page_description, repoID)
        o2 = create_content(page_description, page_name, "user", repoID)
        o3 = add_route(page_name, page_description, "user")

        if not o1 or not o2 or not o3:  # if any of the above process fails
            return {"status": False}
        else:
            return {"status": True}
    except Exception as e:
        print(e)
        return {"status": False}

@app.post("/viewpage", tags=["Operations"])
async def view_page(page_name: str):
    """
    API to view page in realtime
    """
    print(page_name)
    return {"url": get_page(page_name)}
