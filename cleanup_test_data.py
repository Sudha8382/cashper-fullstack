#!/usr/bin/env python3
"""
Cleanup script to remove test/sample data from collections
Only keeps data in admin_loan_applications collection
"""

import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME', 'Cashper')

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    
    print("=" * 60)
    print("CLEANUP: Removing Test Data from Collections")
    print("=" * 60)
    
    # Collections to check (excluding admin_loan_applications which is the source of truth)
    collections_to_check = [
        'short_term_loans',
        'mutual_funds',
        'insurance_inquiries'
    ]
    
    # Test data identifiers (customers that shouldn't be in prod)
    test_customer_names = [
        'Sudha Yadav',
        'test',
        'demo',
        'sample',
    ]
    
    total_deleted = 0
    
    for collection_name in collections_to_check:
        try:
            collection = db[collection_name]
            
            # Find test data by customer name
            for test_name in test_customer_names:
                result = collection.delete_many({
                    'customer': {'$regex': test_name, '$options': 'i'}
                })
                if result.deleted_count > 0:
                    print(f"✓ Deleted {result.deleted_count} '{test_name}' entries from {collection_name}")
                    total_deleted += result.deleted_count
            
            # Show remaining data
            count = collection.count_documents({})
            print(f"  Remaining documents in {collection_name}: {count}")
            
        except Exception as e:
            print(f"⚠ Error processing {collection_name}: {e}")
    
    # Show admin collection (should not be modified)
    admin_collection = db['admin_loan_applications']
    admin_count = admin_collection.count_documents({})
    print(f"\n✓ Admin Collection Status:")
    print(f"  admin_loan_applications: {admin_count} records (KEPT - this is source of truth)")
    
    print(f"\n✓ Total test records deleted: {total_deleted}")
    print("=" * 60)
    print("CLEANUP COMPLETE")
    print("=" * 60)
    
except Exception as e:
    print(f"ERROR: {e}")
    raise
finally:
    client.close()
