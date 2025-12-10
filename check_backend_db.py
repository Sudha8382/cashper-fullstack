#!/usr/bin/env python3
"""Check backend database connection directly"""

import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load env from backend directory
backend_path = r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend'
env_path = os.path.join(backend_path, '.env')
load_dotenv(env_path)

MONGO_URL = os.getenv('MONGO_URL')
MONGO_DB = os.getenv('MONGO_DB', 'cashper_db')

print("=" * 60)
print("BACKEND DATABASE CONNECTION CHECK")
print("=" * 60)
print(f"MONGO_URL: {MONGO_URL[:50]}..." if MONGO_URL else "MONGO_URL: NOT SET")
print(f"MONGO_DB: {MONGO_DB}")

try:
    client = MongoClient(MONGO_URL, connectTimeoutMS=5000, serverSelectionTimeoutMS=5000)
    db = client[MONGO_DB]
    
    # Test connection
    db.command('ping')
    print(f"\n✓ Connected to database: {MONGO_DB}")
    
    # List all collections
    collections = db.list_collection_names()
    print(f"\nCollections ({len(collections)}):")
    for col in collections:
        count = db[col].count_documents({})
        print(f"  • {col}: {count} documents")
    
    # Check admin collection specifically
    print("\n" + "=" * 60)
    print("ADMIN COLLECTION DETAILS:")
    print("=" * 60)
    
    admin_col = db['admin_loan_applications']
    admin_count = admin_col.count_documents({})
    print(f"admin_loan_applications: {admin_count} documents")
    
    if admin_count > 0:
        print("\nSample records:")
        docs = admin_col.find({}).limit(3)
        for i, doc in enumerate(docs, 1):
            customer = doc.get('customer') or doc.get('customerName') or 'UNKNOWN'
            loan_amt = doc.get('loanAmount') or doc.get('loan_amount') or 'N/A'
            print(f"  {i}. {customer} - ₹{loan_amt}")
    
    client.close()
    
except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()
