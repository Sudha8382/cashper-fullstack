#!/usr/bin/env python3
"""Verify admin collection has correct data and no test data"""

import os
from dotenv import load_dotenv
from pymongo import MongoClient
import json

# Load env from backend directory
backend_path = r'c:\Users\ASUS\Desktop\payloan\full_proj\cashper_backend'
env_path = os.path.join(backend_path, '.env')
load_dotenv(env_path)

MONGO_URL = os.getenv('MONGO_URL')
MONGO_DB = os.getenv('MONGO_DB', 'cashper_db')

print("=" * 70)
print("VERIFY ADMIN COLLECTION - ENSURE NO TEST DATA")
print("=" * 70)

try:
    client = MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    admin_col = db['admin_loan_applications']
    
    # Get all documents
    all_docs = list(admin_col.find({}))
    print(f"\nTotal admin applications: {len(all_docs)}\n")
    
    # Check for any suspicious data
    suspicious_found = False
    
    for i, doc in enumerate(all_docs, 1):
        customer = doc.get('customer') or doc.get('customerName') or 'UNKNOWN'
        loan_type = doc.get('loanType') or doc.get('type') or doc.get('loan_type') or 'N/A'
        loan_amt = doc.get('loanAmount') or doc.get('loan_amount') or 'N/A'
        status = doc.get('status', 'N/A')
        email = doc.get('email', 'N/A')
        
        # Flag suspicious entries
        is_test = any(x in customer.lower() for x in ['sudha', 'test', 'demo', 'sample'])
        if is_test:
            suspicious_found = True
            print(f"⚠ SUSPICIOUS [{i}] {customer}")
        else:
            print(f"✓ [{i:2d}] {customer:20s} | {loan_type:15s} | ₹{str(loan_amt):10s} | {status}")
    
    print("\n" + "=" * 70)
    print("VERIFICATION RESULT:")
    print("=" * 70)
    
    if suspicious_found:
        print("⚠ WARNING: Test data found in admin collection!")
    else:
        print("✓ CLEAN: No test data (Sudha Yadav, etc.) found in admin collection")
    
    print(f"✓ Admin collection contains {len(all_docs)} legitimate loan applications")
    
    # Also check other collections for Sudha Yadav
    print("\n" + "=" * 70)
    print("SEARCH FOR SUDHA YADAV IN ALL COLLECTIONS:")
    print("=" * 70)
    
    all_collections = db.list_collection_names()
    found_locations = []
    
    for col_name in all_collections:
        col = db[col_name]
        count = col.count_documents({'customer': {'$regex': 'Sudha Yadav', '$options': 'i'}})
        if count > 0:
            found_locations.append((col_name, count))
    
    if found_locations:
        print("⚠ Sudha Yadav found in:")
        for col_name, count in found_locations:
            print(f"  • {col_name}: {count} document(s)")
    else:
        print("✓ Sudha Yadav not found in any collection")
    
    client.close()
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
