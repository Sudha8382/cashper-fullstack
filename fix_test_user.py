"""
Fix test user password field
"""
from pymongo import MongoClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cashper_backend'))

from app.config import mongo_url, mongo_db
from bson import ObjectId

# Connect to MongoDB
client = MongoClient(mongo_url)
db = client[mongo_db]

TEST_EMAIL = "testuser@cashper.com"

user = db.users.find_one({"email": TEST_EMAIL.lower()})

if user:
    # Update with correct fields
    password_hash = user.get('password')
    
    db.users.update_one(
        {"_id": user["_id"]},
        {"$set": {
            "fullName": "Test User",
            "hashedPassword": password_hash,
            "isActive": True,
            "isEmailVerified": True,
            "isPhoneVerified": True
        }}
    )
    print(f"✅ Updated user with correct fields")
    
    # Verify
    updated_user = db.users.find_one({"_id": user["_id"]})
    print(f"   hashedPassword: {'EXISTS' if updated_user.get('hashedPassword') else 'MISSING'}")
    print(f"   isActive: {updated_user.get('isActive')}")
else:
    print(f"❌ User not found")
