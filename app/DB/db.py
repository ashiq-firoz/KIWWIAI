import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId

# MongoDB connection
uri = os.getenv("MONGO_URL")

try:
    client = MongoClient(uri, server_api=ServerApi('1'))
    print("Database connection Success")
except Exception as err:
    print(f'Database connection failed, err: {err}')

db = client.KIWIDB

def create_user(username: str, password: str) -> bool:
    try:
        if db.users.find_one({"username": username}):
            return False
        db.users.insert_one({"username": username, "password": password,"count":0})
        return True
    except Exception as e:
        print(e)
        return False

def get_user(username: str) -> dict:
    try:
        user = db.users.find_one({"username": username})
        user["_id"] = str(user["_id"])
        return user
    except PyMongoError as e:
        # Log the exception for debugging or error reporting
        print(f"Error retrieving user '{username}': {e}")
        return None

def update_user_count(userID:str,new_count:int)->bool:
    try:
        print(new_count)
        db.users.update_one({"_id":ObjectId(userID)},{"$set":{"count":new_count}})
        return True
    except Exception as err:
        print(err)
        return False

def add_repo(repoID:str,user:str) -> bool:
    try:
        if db.repos.find_one({"repoID": repoID,"user":user}):
            return False
        
        db.repos.insert_one({"user":user,"repoID":repoID})
    except Exception as err:
        print(err)
        return False
    return True

def get_repos(user:str):
    try:
        repos = db.repos.find({"user":user},{'_id': 0})  

        # Extract list of repoId from the repositories
        repo_ids = [repo['repoID'] for repo in list(repos)]
        return repo_ids
    except Exception as err:
        print(err)
        return None