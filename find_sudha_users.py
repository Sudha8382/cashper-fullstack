from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("cashper_backend/.env")
client = MongoClient(os.getenv("MONGO_URI"))
db = client["cashper_db"]

users = list(db["users"].find({"email": {"$regex": "sudha", "$options": "i"}}, {"email": 1, "fullName": 1, "_id": 1}))
print(f"\nFound {len(users)} users with 'sudha' in email:")
for u in users:
    print(f"  • {u.get('fullName', 'N/A')} - {u['email']} (ID: {u['_id']})")

client.close()
