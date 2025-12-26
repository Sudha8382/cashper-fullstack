"""
Check if ANY tax planning applications exist in database
"""

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("cashper_backend/.env")

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["cashper_db"]

print("\n" + "="*70)
print("ALL TAX PLANNING APPLICATIONS")
print("="*70)

# Check Personal Tax
personal_tax = list(db["tax_planning_applications"].find().sort("createdAt", -1).limit(10))
print(f"\n📊 Personal Tax Applications: {len(personal_tax)}")
if personal_tax:
    for i, app in enumerate(personal_tax, 1):
        print(f"\n{i}. Application ID: {app['_id']}")
        print(f"   Name: {app.get('fullName', 'N/A')}")
        print(f"   Email: {app.get('emailAddress', 'N/A')}")
        print(f"   PAN: {app.get('panNumber', 'N/A')}")
        print(f"   userId: {app.get('userId', 'MISSING')}")
        print(f"   Status: {app.get('status', 'N/A')}")
        print(f"   Created: {app.get('createdAt', 'N/A')}")
else:
    print("   ⚠️  No Personal Tax applications found")

# Check Business Tax
business_tax = list(db["business_tax_applications"].find().sort("createdAt", -1).limit(10))
print(f"\n📊 Business Tax Applications: {len(business_tax)}")
if business_tax:
    for i, app in enumerate(business_tax, 1):
        print(f"\n{i}. Application ID: {app['_id']}")
        print(f"   Business: {app.get('businessName', 'N/A')}")
        print(f"   Owner: {app.get('ownerName', 'N/A')}")
        print(f"   Email: {app.get('businessEmail', 'N/A')}")
        print(f"   PAN: {app.get('businessPAN', 'N/A')}")
        print(f"   userId: {app.get('userId', 'MISSING')}")
        print(f"   Status: {app.get('status', 'N/A')}")
        print(f"   Created: {app.get('createdAt', 'N/A')}")
else:
    print("   ⚠️  No Business Tax applications found")

print("\n" + "="*70)

client.close()
