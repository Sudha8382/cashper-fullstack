#!/usr/bin/env python3
"""Seed sample mutual funds and SIP investments data"""

import sys
import os
sys.path.insert(0, r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend')

import pymongo
from dotenv import load_dotenv
from datetime import datetime, timedelta
from bson import ObjectId

# Load environment variables
load_dotenv(r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend\.env')
MONGODB_URL = os.getenv("MONGO_URL")
MONGODB_DB = os.getenv("MONGO_DB", "cashper_db")

# Connect to MongoDB
client = pymongo.MongoClient(MONGODB_URL)
db = client[MONGODB_DB]

# Sample mutual funds and SIPs data to seed
investments_data = [
    {
        "userEmail": "priya.sharma@example.com",
        "name": "Axis Growth Fund",
        "type": "Mutual Funds",
        "invested": 100000,
        "current": 115000,
        "returns": 15,
        "returnsType": "positive",
        "sipAmount": 5000,
        "nextSIP": (datetime.now() + timedelta(days=5)).strftime("%b %d, %Y"),
        "nav": 150.25,
        "units": 665.43,
        "startDate": (datetime.now() - timedelta(days=120)).strftime("%b %d, %Y"),
        "exitLoad": "0%",
        "riskLevel": "High",
        "fundManager": "Axis Asset Management",
        "aum": "₹5000 Cr",
        "status": "active",
        "createdAt": datetime.now()
    },
    {
        "userEmail": "kumuyadav249@gmail.com",
        "name": "HDFC Top 100 Fund",
        "type": "Mutual Funds",
        "invested": 50000,
        "current": 54500,
        "returns": 9,
        "returnsType": "positive",
        "sipAmount": 3000,
        "nextSIP": (datetime.now() + timedelta(days=3)).strftime("%b %d, %Y"),
        "nav": 200.50,
        "units": 249.75,
        "startDate": (datetime.now() - timedelta(days=90)).strftime("%b %d, %Y"),
        "exitLoad": "0%",
        "riskLevel": "Medium",
        "fundManager": "HDFC Asset Management",
        "aum": "₹8000 Cr",
        "status": "active",
        "createdAt": datetime.now()
    },
    {
        "userEmail": "jane.smith@example.com",
        "name": "ICICI Prudential Tech Fund",
        "type": "Mutual Funds",
        "invested": 75000,
        "current": 82000,
        "returns": 9.33,
        "returnsType": "positive",
        "sipAmount": 8000,
        "nextSIP": (datetime.now() + timedelta(days=8)).strftime("%b %d, %Y"),
        "nav": 175.75,
        "units": 429.34,
        "startDate": (datetime.now() - timedelta(days=150)).strftime("%b %d, %Y"),
        "exitLoad": "1%",
        "riskLevel": "High",
        "fundManager": "ICICI Prudential",
        "aum": "₹6500 Cr",
        "status": "active",
        "createdAt": datetime.now()
    },
    {
        "userEmail": "sudha.yadav@example.com",
        "name": "SIP in Axis Blue Chip",
        "type": "SIP",
        "invested": 54000,
        "current": 58500,
        "returns": 8.33,
        "returnsType": "positive",
        "sipAmount": 6000,
        "nextSIP": (datetime.now() + timedelta(days=10)).strftime("%b %d, %Y"),
        "nav": 125.50,
        "units": 466.00,
        "startDate": (datetime.now() - timedelta(days=100)).strftime("%b %d, %Y"),
        "exitLoad": "0%",
        "riskLevel": "Low",
        "fundManager": "Axis Asset Management",
        "aum": "₹7000 Cr",
        "status": "active",
        "createdAt": datetime.now()
    },
    {
        "userEmail": "riya.yadav@example.com",
        "name": "Mirae Asset Emerging Bluechip",
        "type": "Mutual Funds",
        "invested": 125000,
        "current": 138500,
        "returns": 10.8,
        "returnsType": "positive",
        "sipAmount": 10000,
        "nextSIP": (datetime.now() + timedelta(days=7)).strftime("%b %d, %Y"),
        "nav": 220.75,
        "units": 567.89,
        "startDate": (datetime.now() - timedelta(days=200)).strftime("%b %d, %Y"),
        "exitLoad": "0%",
        "riskLevel": "High",
        "fundManager": "Mirae Asset",
        "aum": "₹9000 Cr",
        "status": "active",
        "createdAt": datetime.now()
    }
]

# Clear existing investments (optional)
print("Clearing existing investments...")
db["investments"].delete_many({})

# Insert new investments
print(f"Inserting {len(investments_data)} investments...")
result = db["investments"].insert_many(investments_data)
print(f"✅ Successfully inserted {len(result.inserted_ids)} investments")

# Verify
count = db["investments"].count_documents({})
print(f"\n📊 Total investments in database: {count}")

# Show inserted data
print("\n" + "="*60)
print("INSERTED INVESTMENTS")
print("="*60)
for inv in db["investments"].find().sort("_id", -1).limit(5):
    print(f"\nID: {inv.get('_id')}")
    print(f"  Name: {inv.get('name')}")
    print(f"  User Email: {inv.get('userEmail')}")
    print(f"  Invested: ₹{inv.get('invested'):,.0f}")
    print(f"  Current: ₹{inv.get('current'):,.0f}")
    print(f"  Returns: +{inv.get('returns')}%")
    print(f"  Status: {inv.get('status')}")

print("\n" + "="*60)
print("✅ Seeding complete!")
