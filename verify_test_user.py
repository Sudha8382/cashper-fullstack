"""
Quick script to verify test user and try direct login
"""
from pymongo import MongoClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cashper_backend'))

from app.config import mongo_url, mongo_db
from app.utils.security import verify_password

# Connect to MongoDB
client = MongoClient(mongo_url)
db = client[mongo_db]

TEST_EMAIL = "testuser@cashper.com"
TEST_PASSWORD = "Test@123"

user = db.users.find_one({"email": TEST_EMAIL.lower()})

if user:
    print(f"✅ User found: {user['email']}")
    print(f"   User ID: {user['_id']}")
    print(f"   Name: {user.get('name', 'N/A')}")
    print(f"   Password hash exists: {bool(user.get('password'))}")
    
    # Verify password
    is_valid = verify_password(TEST_PASSWORD, user.get('password', ''))
    print(f"   Password verification: {'✅ VALID' if is_valid else '❌ INVALID'}")
else:
    print(f"❌ User not found: {TEST_EMAIL}")
