import os
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, status, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from pymongo.mongo_client import MongoClient
from starlette.middleware.sessions import SessionMiddleware

import scheme
from core.initializer import initialise_express
from core.pages import generate_page, create_content, get_page
from core.routes import add_route
from DB.db import create_user, get_user, get_repos,add_repo,update_user_count
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

# Session setup
class SessionData(BaseModel):
    loggedin: bool = False
    user_id: Union[str, None] = None
    repo_count: int = 0

# Replace 'your-secret-key' with a strong, randomly generated secret key
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# MongoDB setup (assuming MongoClient is correctly configured)


def get_session_data(request: Request) -> SessionData:
    cookie_data = request.cookies.get("session_data")
    if cookie_data:
        return SessionData.parse_raw(cookie_data)
    return SessionData()


@app.get("/")
def read_root(sessiondata :SessionData = Depends(get_session_data)):
    return {"Api Status": "ok 200"}

@app.post("/signup/", tags=["Authentication Routes"])
async def signup(username: str, password: str):
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
async def login(username: str, password: str, response: Response):
    """
    API endpoint for user login
    """
    user = get_user(username)
    
    if not user or user["password"] != password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    session_data = SessionData(loggedin=True, user_id=str(user["_id"]), repo_count=user["count"])

    response.set_cookie(
        key="session_data",
        value=session_data.json(),
        httponly=True,
        max_age=1800,  # 30 minutes
        samesite="lax"
    )

    return {"status": True, "message": "Login successful", "id": user["_id"], "repoCount": user["count"], "password": user["password"]}


@app.post("/backendframework", tags=["Operations"])
async def select_framework(framework: scheme.BackendFrameworks,response: Response, session_data: SessionData = Depends(get_session_data)):
    """
    API to initialize a repo with respective Backend Framework
    """
    if not session_data.loggedin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    userId = session_data.user_id
    repocount = session_data.repo_count
    print(session_data)
    if framework == scheme.BackendFrameworks.EXPRESS and userId:
        res = initialise_express(userId + str(repocount))
        if res:
            session_data.repo_count += 1
            add_repo(str(repocount),userId)
            update_user_count(session_data.user_id,session_data.repo_count)

            # Update the session cookie with the new session data
            response.set_cookie(
                key="session_data",
                value=session_data.json(),
                httponly=True,
                max_age=1800,  # 30 minutes
                samesite="lax"
            )

            return {"status": True, "repoID": str(repocount)}
    return {"status": False}

@app.post("/getRepos",tags=["Operations"])
async def get_repo_list(session_data: SessionData = Depends(get_session_data)):
    """
    API to get a list of created repos for authorised user
    """
    if not session_data.loggedin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    userId = session_data.user_id
    res = get_repos(userId)
    
    return {"status": True, "repo_ID_list": res}

@app.post("/createpage", tags=["Operations"])
async def add_page(page_description: str, page_name: str, repoID: str, session_data: SessionData = Depends(get_session_data)):
    """
    API to create pages based on the description given
    """
    if not session_data.loggedin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    
    try:
        o1 = generate_page(page_description, repoID,session_data.user_id)
        o2 = create_content(page_description, page_name, session_data.user_id, repoID)
        o3 = add_route(page_name, page_description, session_data.user_id,repoID)

        if not o1 or not o2 or not o3:  # if any of the above process fails
            return {"status": False}
        else:
            return {"status": True}
    except Exception as e:
        print(e)
        return {"status": False}

@app.post("/viewpage", tags=["Operations"])
async def view_page(page_name: str,repoID:str, session_data: SessionData = Depends(get_session_data)):
    """
    API to view page in real-time
    """
    if not session_data.loggedin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    print(page_name)
    return {"url": get_page(page_name,repoID,session_data.user_id)}
