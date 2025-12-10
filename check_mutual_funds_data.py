#!/usr/bin/env python3
"""Check mutual funds and SIP data in database"""

import sys
import os
sys.path.insert(0, r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend')

from bson import ObjectId
import pymongo
from dotenv import load_dotenv

# Load environment variables
load_dotenv(r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend\.env')
MONGODB_URL = os.getenv("MONGO_URL")
MONGODB_DB = os.getenv("MONGO_DB", "cashper_db")

print(f"MongoDB URL: {MONGODB_URL}")
print(f"MongoDB DB: {MONGODB_DB}")

# Connect to MongoDB
client = pymongo.MongoClient(MONGODB_URL)
db = client[MONGODB_DB]

print("\n" + "="*60)
print("CHECKING MUTUAL FUNDS DATA")
print("="*60)

# Check mutual fund applications
mf_apps = db["mutual_fund_applications"].find()
mf_count = db["mutual_fund_applications"].count_documents({})
print(f"\nTotal Mutual Fund Applications: {mf_count}")
if mf_count > 0:
    for app in db["mutual_fund_applications"].find().limit(3):
        print(f"\nApplication ID: {app.get('_id')}")
        print(f"  Name: {app.get('name')}")
        print(f"  Email: {app.get('email')}")
        print(f"  Investment Type: {app.get('investmentType')}")
        print(f"  Investment Amount: {app.get('investmentAmount')}")
        print(f"  SIP Amount: {app.get('sipAmount')}")
        print(f"  Status: {app.get('status')}")

# Check SIP applications
sip_apps = db["sip_applications"].find()
sip_count = db["sip_applications"].count_documents({})
print(f"\n\nTotal SIP Applications: {sip_count}")
if sip_count > 0:
    for app in db["sip_applications"].find().limit(3):
        print(f"\nSIP Application ID: {app.get('_id')}")
        print(f"  Name: {app.get('name')}")
        print(f"  Email: {app.get('email')}")
        print(f"  SIP Amount: {app.get('sipAmount')}")
        print(f"  Tenure: {app.get('tenure')}")
        print(f"  Status: {app.get('status')}")

# Check investments collection (for dashboard)
inv_count = db["investments"].count_documents({})
print(f"\n\nTotal Investments (dashboard): {inv_count}")
if inv_count > 0:
    for inv in db["investments"].find().limit(3):
        print(f"\nInvestment ID: {inv.get('_id')}")
        print(f"  Name: {inv.get('name')}")
        print(f"  Type: {inv.get('type')}")
        print(f"  Invested: {inv.get('invested')}")
        print(f"  Status: {inv.get('status')}")

print("\n" + "="*60)
