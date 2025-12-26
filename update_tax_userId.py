"""
Update existing Tax Planning applications with userId
पुराने applications में userId add करेंगे
"""

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("cashper_backend/.env")

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["cashper_db"]

print("\n" + "="*70)
print("UPDATING TAX PLANNING APPLICATIONS WITH userId")
print("="*70)

# Get users
users = list(db["users"].find(
    {"email": {"$in": ["bhoomi.sudha83@gmail.com", "kumuyadav249@gmail.com"]}},
    {"_id": 1, "email": 1}
))

user_map = {user["email"]: str(user["_id"]) for user in users}
print(f"\n📋 Found {len(users)} users:")
for email, userId in user_map.items():
    print(f"  • {email} → {userId}")

# Update Personal Tax Applications
print("\n" + "="*70)
print("PERSONAL TAX APPLICATIONS")
print("="*70)

personal_apps = list(db["tax_planning_applications"].find({"userId": None}))
print(f"\nApplications without userId: {len(personal_apps)}")

if personal_apps:
    print("\nUpdating based on email address:")
    updated_count = 0
    for app in personal_apps:
        email = app.get("emailAddress", "").lower()
        if email in user_map:
            result = db["tax_planning_applications"].update_one(
                {"_id": app["_id"]},
                {"$set": {"userId": user_map[email]}}
            )
            if result.modified_count > 0:
                updated_count += 1
                print(f"  ✅ Updated: {app.get('fullName')} ({email})")
    
    print(f"\n✅ Updated {updated_count} Personal Tax applications")
else:
    print("  ℹ️  All Personal Tax applications already have userId")

# Update Business Tax Applications
print("\n" + "="*70)
print("BUSINESS TAX APPLICATIONS")
print("="*70)

business_apps = list(db["business_tax_applications"].find({"userId": None}))
print(f"\nApplications without userId: {len(business_apps)}")

if business_apps:
    print("\nUpdating based on email address:")
    updated_count = 0
    for app in business_apps:
        email = app.get("businessEmail", "").lower()
        if email in user_map:
            result = db["business_tax_applications"].update_one(
                {"_id": app["_id"]},
                {"$set": {"userId": user_map[email]}}
            )
            if result.modified_count > 0:
                updated_count += 1
                print(f"  ✅ Updated: {app.get('businessName')} ({email})")
    
    print(f"\n✅ Updated {updated_count} Business Tax applications")
else:
    print("  ℹ️  All Business Tax applications already have userId")

# Verification
print("\n" + "="*70)
print("VERIFICATION")
print("="*70)

personal_total = db["tax_planning_applications"].count_documents({})
personal_with_userId = db["tax_planning_applications"].count_documents({"userId": {"$ne": None}})
print(f"\n📊 Personal Tax:")
print(f"  Total: {personal_total}")
print(f"  With userId: {personal_with_userId}")
print(f"  Without userId: {personal_total - personal_with_userId}")

business_total = db["business_tax_applications"].count_documents({})
business_with_userId = db["business_tax_applications"].count_documents({"userId": {"$ne": None}})
print(f"\n📊 Business Tax:")
print(f"  Total: {business_total}")
print(f"  With userId: {business_with_userId}")
print(f"  Without userId: {business_total - business_with_userId}")

print("\n" + "="*70)
print("✅ UPDATE COMPLETE")
print("="*70)

client.close()
