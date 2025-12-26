"""
Update existing tax applications without userId
"""

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("cashper_backend/.env")

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["cashper_db"]

print("\n" + "="*70)
print("UPDATING TAX APPLICATIONS WITHOUT userId")
print("="*70)

# Get user by email
user = db["users"].find_one({"email": "sudha@gmail.com"})
if not user:
    print("\n❌ User not found!")
    client.close()
    exit()

user_id = str(user["_id"])
print(f"\n👤 User: {user.get('fullName', 'N/A')} ({user['email']})")
print(f"🆔 User ID: {user_id}")

# Update Personal Tax Applications
print("\n" + "="*70)
print("PERSONAL TAX APPLICATIONS")
print("="*70)

personal_apps_null = list(db["tax_planning_applications"].find({"userId": None}))
print(f"\nFound {len(personal_apps_null)} applications without userId")

if personal_apps_null:
    updated = 0
    for app in personal_apps_null:
        email = app.get("emailAddress", "").lower()
        
        # Check if email matches any registered user
        matching_user = db["users"].find_one({"email": email})
        
        if matching_user:
            result = db["tax_planning_applications"].update_one(
                {"_id": app["_id"]},
                {"$set": {"userId": str(matching_user["_id"])}}
            )
            if result.modified_count > 0:
                updated += 1
                print(f"  ✅ Updated: {app.get('fullName')} ({email})")
                print(f"     Assigned to userId: {str(matching_user['_id'])}")
        else:
            print(f"  ⚠️  No user found for: {app.get('fullName')} ({email})")
    
    print(f"\n✅ Updated {updated} Personal Tax applications")
else:
    print("  ℹ️  No applications to update")

# Update Business Tax Applications
print("\n" + "="*70)
print("BUSINESS TAX APPLICATIONS")
print("="*70)

business_apps_null = list(db["business_tax_applications"].find({"userId": None}))
print(f"\nFound {len(business_apps_null)} applications without userId")

if business_apps_null:
    updated = 0
    for app in business_apps_null:
        email = app.get("businessEmail", "").lower()
        
        # Check if email matches any registered user
        matching_user = db["users"].find_one({"email": email})
        
        if matching_user:
            result = db["business_tax_applications"].update_one(
                {"_id": app["_id"]},
                {"$set": {"userId": str(matching_user["_id"])}}
            )
            if result.modified_count > 0:
                updated += 1
                print(f"  ✅ Updated: {app.get('businessName')} ({email})")
                print(f"     Assigned to userId: {str(matching_user['_id'])}")
        else:
            print(f"  ⚠️  No user found for: {app.get('businessName')} ({email})")
    
    print(f"\n✅ Updated {updated} Business Tax applications")
else:
    print("  ℹ️  No applications to update")

# Verification
print("\n" + "="*70)
print("VERIFICATION")
print("="*70)

personal_total = db["tax_planning_applications"].count_documents({})
personal_with_userId = db["tax_planning_applications"].count_documents({"userId": {"$ne": None}})
business_total = db["business_tax_applications"].count_documents({})
business_with_userId = db["business_tax_applications"].count_documents({"userId": {"$ne": None}})

print(f"\n📊 Personal Tax:")
print(f"   Total: {personal_total}")
print(f"   With userId: {personal_with_userId}")
print(f"   Without userId: {personal_total - personal_with_userId}")

print(f"\n📊 Business Tax:")
print(f"   Total: {business_total}")
print(f"   With userId: {business_with_userId}")
print(f"   Without userId: {business_total - business_with_userId}")

print("\n" + "="*70)
print("✅ UPDATE COMPLETE")
print("="*70)

client.close()
