"""
Check all applications for bhoomi.sudha83@gmail.com
"""

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("cashper_backend/.env")

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["cashper_db"]

print("\n" + "="*70)
print("BHOOMI SUDHA APPLICATIONS CHECK")
print("="*70)

# Get user
user = db["users"].find_one({"email": "bhoomi.sudha83@gmail.com"})
if not user:
    print("\n❌ User not found!")
    client.close()
    exit()

user_id = str(user["_id"])
print(f"\n👤 User: {user.get('fullName', 'N/A')}")
print(f"📧 Email: {user['email']}")
print(f"🆔 User ID: {user_id}")

# Check all collections
collections_to_check = [
    ("Personal Loans", "personal_loans"),
    ("Home Loans", "home_loans"),
    ("Business Loans", "business_loans"),
    ("Short Term Loans", "short_term_loans"),
    ("Personal Tax", "tax_planning_applications"),
    ("Business Tax", "business_tax_applications"),
]

print("\n" + "="*70)
print("APPLICATIONS BY SERVICE")
print("="*70)

total_count = 0

for service_name, collection_name in collections_to_check:
    # Try both userId field and email field
    count_by_userId = db[collection_name].count_documents({"userId": user_id})
    count_by_email = db[collection_name].count_documents({
        "$or": [
            {"emailAddress": "bhoomi.sudha83@gmail.com"},
            {"businessEmail": "bhoomi.sudha83@gmail.com"},
            {"email": "bhoomi.sudha83@gmail.com"}
        ]
    })
    
    total_in_collection = db[collection_name].count_documents({})
    
    print(f"\n📊 {service_name} ({collection_name}):")
    print(f"   By userId: {count_by_userId}")
    print(f"   By email: {count_by_email}")
    print(f"   Total in collection: {total_in_collection}")
    
    if count_by_userId > 0:
        apps = list(db[collection_name].find({"userId": user_id}))
        for i, app in enumerate(apps, 1):
            print(f"   {i}. ID: {app['_id']}")
            if 'fullName' in app:
                print(f"      Name: {app.get('fullName')}")
            if 'businessName' in app:
                print(f"      Business: {app.get('businessName')}")
            print(f"      Status: {app.get('status', 'N/A')}")
    
    total_count += count_by_userId

print("\n" + "="*70)
print(f"✅ TOTAL APPLICATIONS: {total_count}")
print("="*70)

client.close()
