import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError
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
        db.users.insert_one({"username": username, "password": password})
        return True
    except Exception as e:
        print(e)
        return False

def get_user(username: str) -> dict:
    try:
        user = db.users.find_one({"username": username})
        return user
    except PyMongoError as e:
        # Log the exception for debugging or error reporting
        print(f"Error retrieving user '{username}': {e}")
        return None