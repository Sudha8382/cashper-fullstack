"""
Check user password field name
"""
from pymongo import MongoClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cashper_backend'))

from app.config import mongo_url, mongo_db

# Connect to MongoDB
client = MongoClient(mongo_url)
db = client[mongo_db]

TEST_EMAIL = "testuser@cashper.com"

user = db.users.find_one({"email": TEST_EMAIL.lower()})

if user:
    print(f"User fields:")
    for key in user.keys():
        if key == 'password' or key == 'hashedPassword':
            print(f"   {key}: {'EXISTS' if user[key] else 'NONE'}")
        elif key != '_id':
            print(f"   {key}: {user[key]}")
