"""
Script to add admin role to a user
"""
from pymongo import MongoClient
from app.config import mongo_url

# Connect to MongoDB
client = MongoClient(mongo_url)
db = client.cashper_db

# Update user to admin
email = "admin@cashper.com"
result = db.users.update_one(
    {"email": email},
    {"$set": {"role": "admin"}}
)

if result.modified_count > 0:
    print(f"✅ Successfully added admin role to {email}")
else:
    user = db.users.find_one({"email": email})
    if user:
        if user.get("role") == "admin":
            print(f"ℹ️  User {email} already has admin role")
        else:
            print(f"⚠️  User {email} found but role not updated")
    else:
        print(f"❌ User {email} not found")

client.close()
