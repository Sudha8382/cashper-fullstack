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
    
    print("=== USER STATUS CHECK ===\n")
    
    # Get all users with status fields
    users = list(db['users'].find({}, {'fullName': 1, 'isActive': 1, 'isSuspended': 1}))
    
    print(f"Total users in database: {len(users)}\n")
    
    if users:
        print("Sample users:")
        for i, user in enumerate(users[:3]):
            print(f"  {i+1}. {user.get('fullName', 'N/A')}")
            print(f"     isActive: {user.get('isActive', 'NOT SET')}")
            print(f"     isSuspended: {user.get('isSuspended', 'NOT SET')}")
        print()
    
    # Count various statuses
    total = db['users'].count_documents({})
    
    # Count based on database values
    has_isActive_true = db['users'].count_documents({'isActive': True})
    has_isActive_false = db['users'].count_documents({'isActive': False})
    has_isActive_missing = db['users'].count_documents({'isActive': {'$exists': False}})
    
    has_isSuspended_true = db['users'].count_documents({'isSuspended': True})
    has_isSuspended_false = db['users'].count_documents({'isSuspended': False})
    has_isSuspended_missing = db['users'].count_documents({'isSuspended': {'$exists': False}})
    
    print("=== FIELD DISTRIBUTION ===")
    print(f"\nisActive field:")
    print(f"  True: {has_isActive_true}")
    print(f"  False: {has_isActive_false}")
    print(f"  Missing: {has_isActive_missing}")
    
    print(f"\nisSuspended field:")
    print(f"  True: {has_isSuspended_true}")
    print(f"  False: {has_isSuspended_false}")
    print(f"  Missing: {has_isSuspended_missing}")
    
    print(f"\n=== CALCULATED STATS (UPDATED LOGIC) ===")
    # Updated logic: Active = isActive=True AND (isSuspended missing OR False)
    active = db['users'].count_documents({"isActive": True, "$or": [{"isSuspended": {"$exists": False}}, {"isSuspended": False}]})
    # Inactive = isActive=False AND (isSuspended missing OR False) - exclude suspended
    inactive = db['users'].count_documents({"isActive": False, "$or": [{"isSuspended": {"$exists": False}}, {"isSuspended": False}]})
    suspended = db['users'].count_documents({'isSuspended': True})
    
    print(f"Active (isActive=True AND isSuspended not set/False): {active}")
    print(f"Inactive (isActive=False AND isSuspended not set/False): {inactive}")
    print(f"Suspended (isSuspended=True): {suspended}")
    print(f"Total: {total}")
    
    client.close()
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
