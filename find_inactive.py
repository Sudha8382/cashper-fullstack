#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, 'cashper_backend')
os.chdir('cashper_backend')

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("MONGO_URL", "mongodb+srv://kumuyadav249_db_user:O0zb3rZlZXArZiSg@cluster0.mnzwn7m.mongodb.net/")
DATABASE_NAME = os.getenv("MONGO_DB", "cashper_db")

try:
    client = MongoClient(DATABASE_URL)
    db = client[DATABASE_NAME]
    
    # Find inactive users
    inactive_users = list(db['users'].find({'isActive': False}, {'_id': 1, 'fullName': 1, 'email': 1, 'isActive': 1, 'isSuspended': 1}))
    
    print(f"Inactive users (isActive=False): {len(inactive_users)}")
    if inactive_users:
        for user in inactive_users:
            print(f"\n  User ID: {user['_id']}")
            print(f"  Name: {user.get('fullName', 'N/A')}")
            print(f"  Email: {user.get('email', 'N/A')}")
            print(f"  isActive: {user.get('isActive')}")
            print(f"  isSuspended: {user.get('isSuspended', 'NOT SET')}")
    
    client.close()
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
