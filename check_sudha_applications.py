"""
Check all applications for sudha@gmail.com (current logged in user)
"""

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("cashper_backend/.env")

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["cashper_db"]

print("\n" + "="*70)
print("SUDHA@GMAIL.COM APPLICATIONS CHECK")
print("="*70)

# Get user
user = db["users"].find_one({"email": "sudha@gmail.com"})
if not user:
    print("\n❌ User not found!")
    client.close()
    exit()

user_id = str(user["_id"])
print(f"\n👤 User: {user.get('fullName', 'N/A')}")
print(f"📧 Email: {user['email']}")
print(f"🆔 User ID: {user_id}")
print(f"🔑 Is Admin: {user.get('isAdmin', False)}")

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
    count_by_userId = db[collection_name].count_documents({"userId": user_id})
    
    print(f"\n📊 {service_name}:")
    print(f"   Applications: {count_by_userId}")
    
    if count_by_userId > 0:
        apps = list(db[collection_name].find({"userId": user_id}))
        for i, app in enumerate(apps, 1):
            print(f"   {i}. ID: {app['_id']}")
            if 'fullName' in app:
                print(f"      Name: {app.get('fullName')}")
            if 'businessName' in app:
                print(f"      Business: {app.get('businessName')}")
            if 'loanAmount' in app:
                print(f"      Amount: ₹{app.get('loanAmount')}")
            print(f"      Status: {app.get('status', 'N/A')}")
            print(f"      Created: {app.get('createdAt', 'N/A')}")
    
    total_count += count_by_userId

print("\n" + "="*70)
print(f"✅ TOTAL APPLICATIONS WITH userId: {total_count}")
print("="*70)

# Also check applications without userId
print("\n" + "="*70)
print("APPLICATIONS WITHOUT userId (BY EMAIL)")
print("="*70)

orphan_count = 0
for service_name, collection_name in collections_to_check:
    # Check by email fields
    query = {
        "userId": None,
        "$or": [
            {"emailAddress": "sudha@gmail.com"},
            {"businessEmail": "sudha@gmail.com"},
            {"email": "sudha@gmail.com"}
        ]
    }
    
    count_orphan = db[collection_name].count_documents(query)
    if count_orphan > 0:
        print(f"\n⚠️  {service_name}: {count_orphan} applications without userId")
        orphan_count += count_orphan

if orphan_count == 0:
    print("\n✅ No orphan applications found")

print("\n" + "="*70)
print(f"📈 SUMMARY")
print("="*70)
print(f"With userId: {total_count}")
print(f"Without userId: {orphan_count}")
print(f"TOTAL: {total_count + orphan_count}")
print("="*70)

client.close()
