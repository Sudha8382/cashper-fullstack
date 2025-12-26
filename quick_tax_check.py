"""
Quick check - Tax Planning applications में userId field है या नहीं
"""

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("cashper_backend/.env")

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["cashper_db"]

print("\n📊 PERSONAL TAX APPLICATIONS:")
personal = list(db["personal_tax_applications"].find().limit(5))
print(f"Total: {db['personal_tax_applications'].count_documents({})}")
if personal:
    for app in personal:
        print(f"  - {app.get('fullName')} | userId: {app.get('userId', 'MISSING')}")

print("\n📊 BUSINESS TAX APPLICATIONS:")
business = list(db["business_tax_applications"].find().limit(5))
print(f"Total: {db['business_tax_applications'].count_documents({})}")
if business:
    for app in business:
        print(f"  - {app.get('businessName')} | userId: {app.get('userId', 'MISSING')}")

client.close()
print("\n✅ Done")
