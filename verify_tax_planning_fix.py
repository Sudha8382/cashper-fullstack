"""
Verify Tax Planning Data Isolation Fix
यह script check करेगा कि:
1. Personal Tax Planning applications में userId field है
2. Business Tax Planning applications में userId field है
3. हर user केवल अपने applications ही देख पाए
"""

from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("cashper_backend/.env")

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["cashper_db"]

print("=" * 70)
print("TAX PLANNING DATA ISOLATION VERIFICATION")
print("=" * 70)

# Check users
users = list(db["users"].find(
    {"email": {"$in": ["bhoomi.sudha83@gmail.com", "kumuyadav249@gmail.com"]}},
    {"_id": 1, "email": 1, "fullName": 1}
))

print("\n📋 USERS:")
user_map = {}
for user in users:
    user_id = str(user["_id"])
    user_map[user_id] = user["email"]
    print(f"  • {user.get('fullName', 'N/A')} - {user['email']}")
    print(f"    ID: {user_id}")

# Check Personal Tax Planning Applications
print("\n" + "=" * 70)
print("PERSONAL TAX PLANNING APPLICATIONS")
print("=" * 70)

personal_tax_apps = list(db["personal_tax_applications"].find())
print(f"\nTotal Personal Tax Applications: {len(personal_tax_apps)}")

if personal_tax_apps:
    print("\nApplications by User:")
    by_user = {}
    for app in personal_tax_apps:
        user_id = app.get("userId", "No userId")
        if user_id not in by_user:
            by_user[user_id] = []
        by_user[user_id].append(app)
    
    for user_id, apps in by_user.items():
        email = user_map.get(user_id, "Unknown User")
        print(f"\n  👤 {email} (userId: {user_id}):")
        print(f"     Applications: {len(apps)}")
        for i, app in enumerate(apps, 1):
            print(f"     {i}. {app.get('fullName')} - {app.get('emailAddress')}")
            print(f"        PAN: {app.get('panNumber')}")
            print(f"        Status: {app.get('status')}")
else:
    print("  ⚠️  No Personal Tax applications found")

# Check Business Tax Planning Applications
print("\n" + "=" * 70)
print("BUSINESS TAX PLANNING APPLICATIONS")
print("=" * 70)

business_tax_apps = list(db["business_tax_applications"].find())
print(f"\nTotal Business Tax Applications: {len(business_tax_apps)}")

if business_tax_apps:
    print("\nApplications by User:")
    by_user = {}
    for app in business_tax_apps:
        user_id = app.get("userId", "No userId")
        if user_id not in by_user:
            by_user[user_id] = []
        by_user[user_id].append(app)
    
    for user_id, apps in by_user.items():
        email = user_map.get(user_id, "Unknown User")
        print(f"\n  👤 {email} (userId: {user_id}):")
        print(f"     Applications: {len(apps)}")
        for i, app in enumerate(apps, 1):
            print(f"     {i}. {app.get('businessName')} - {app.get('businessEmail')}")
            print(f"        PAN: {app.get('businessPAN')}")
            print(f"        Owner: {app.get('ownerName')}")
            print(f"        Status: {app.get('status')}")
else:
    print("  ⚠️  No Business Tax applications found")

# Verification Summary
print("\n" + "=" * 70)
print("VERIFICATION SUMMARY")
print("=" * 70)

# Check if userId field exists in all applications
personal_without_userId = [app for app in personal_tax_apps if not app.get("userId")]
business_without_userId = [app for app in business_tax_apps if not app.get("userId")]

if personal_without_userId:
    print(f"\n⚠️  WARNING: {len(personal_without_userId)} Personal Tax applications without userId")
else:
    print(f"\n✅ All Personal Tax applications have userId field")

if business_without_userId:
    print(f"⚠️  WARNING: {len(business_without_userId)} Business Tax applications without userId")
else:
    print(f"✅ All Business Tax applications have userId field")

print("\n" + "=" * 70)
print("🎯 NEXT STEPS:")
print("=" * 70)
print("1. अब Tax Planning forms fill करें दोनों users से")
print("2. bhoomi.sudha83@gmail.com से login करके Personal/Business Tax form भरें")
print("3. kumuyadav249@gmail.com से login करके Personal/Business Tax form भरें")
print("4. दोनों dashboards check करें - हर user केवल अपने applications देखेगा")
print("=" * 70)

client.close()
