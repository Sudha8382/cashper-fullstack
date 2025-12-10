#!/usr/bin/env python3
"""Check actual data in all collections"""

import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import json

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME', 'Cashper')

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    
    print("=" * 60)
    print("DATABASE CONTENT CHECK")
    print("=" * 60)
    
    # Check all collections
    collections = db.list_collection_names()
    print(f"\nAll collections in database ({len(collections)}):")
    for col in collections:
        print(f"  - {col}")
    
    print("\n" + "=" * 60)
    print("LOAN-RELATED COLLECTIONS:")
    print("=" * 60)
    
    loan_collections = [
        'admin_loan_applications',
        'short_term_loans',
        'Personal_loan',
        'Business_loan',
        'Home_loan',
        'LoanApplications'
    ]
    
    for col_name in loan_collections:
        if col_name in collections:
            col = db[col_name]
            count = col.count_documents({})
            print(f"\n{col_name}: {count} documents")
            
            if count > 0 and count <= 10:
                docs = col.find({}).limit(5)
                for doc in docs:
                    customer = doc.get('customer') or doc.get('customerName') or doc.get('name') or 'UNKNOWN'
                    loan_amt = doc.get('loanAmount') or doc.get('loan_amount') or 'N/A'
                    status = doc.get('status', 'N/A')
                    print(f"  • {customer} - ₹{loan_amt} - {status}")
    
    print("\n" + "=" * 60)
    print("VERIFICATION:")
    print("=" * 60)
    admin_col = db['admin_loan_applications']
    admin_count = admin_col.count_documents({})
    print(f"✓ Admin collection count: {admin_count}")
    
    if admin_count == 0:
        print("⚠ WARNING: admin_loan_applications is empty!")
        print("  The data might be in a different collection")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
finally:
    client.close()
